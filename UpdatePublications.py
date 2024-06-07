import re
import os
import time
import requests
import bibtexparser


def remove_special_chartacters(in_string):
    out_string = re.sub('[^A-Za-z0-9 ]+', '', in_string)
    return out_string

def make_yaml_safe(in_string):
    in_string = in_string.replace("\\", "")
    in_string = in_string.replace('"', "'")
    return in_string

def cleanstring(in_string):
    in_string = in_string.replace("\n", " ")
    in_string = in_string.replace("\r", " ")
    in_string = in_string.replace("\t", " ")
    in_string = in_string.replace("{", "")
    in_string = in_string.replace("}", "")
    return in_string

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def convert_authors_string(authors):
    authors = cleanstring(authors)
    authors = authors.replace(" and ", ", ")
    authors = rreplace(authors, ", ", " and ", 1)
    return authors

def get_details(dict_in, key_in):
    try:
        data = dict_in[key_in]
    except KeyError as e:
        return ""
    return data

def main():

    # Check if there is a publications folder
    if not os.path.exists('_publications'):
        os.makedirs('_publications')

    # Go through each team member
    for filename in os.listdir(os.path.abspath(os.getcwd())+"/_team"):
        author_file = open(os.path.abspath(os.getcwd())+"/_team/"+filename, "r")

        uri = None
        for line in author_file.readlines():
            if "first_name" in line:
                first_name = line.split(':')[1].lstrip().rstrip("\n")
            if "last_name" in line:
                last_name = line.split(':')[1].lstrip().rstrip("\n")
            if "dblp_uri" in line:
                uri = line[len("dblp_uri: "):].rstrip("\n")
            if "tier" in line:
                tier = line[len("tier: "):].rstrip("\n")

        if tier == "Previous Members":
            print("Skipping (previous member): " + first_name + " " + last_name)
            continue
        
        # Get the bib
        if uri is not None:
            print("Processing: " + first_name + " " + last_name)
            
            if len(uri) <= 0:
                continue
            
            # Get all the entries for the person
            resp = requests.get(uri)
            bib_database = bibtexparser.loads(resp.text)

            # Go through each entry
            bib_num = 0
            while bib_num < len(bib_database.entries):

                # Extract the entry
                bib = bib_database.entries[bib_num]
                bib_num += 1

                # Get the details for the entry (include cleaning)
                title           = cleanstring(get_details(bib, 'title')).title()
                bibsource       = cleanstring(get_details(bib, 'bibsource'))
                biburl          = cleanstring(get_details(bib, 'biburl'))
                doi             = cleanstring(get_details(bib, 'doi'))
                year            = cleanstring(get_details(bib, 'year'))
                publisher       = cleanstring(get_details(bib, 'publisher'))
                pages           = cleanstring(get_details(bib, 'pages'))
                venue           = cleanstring(get_details(bib, 'booktitle'))
                author          = convert_authors_string(remove_special_chartacters(cleanstring(get_details(bib, 'author'))))
                ENTRYTYPE       = cleanstring(get_details(bib, 'ENTRYTYPE'))
                ID              = cleanstring(get_details(bib, 'ID'))

                # Confirm that we are looking at an article or paper
                if ((ENTRYTYPE.upper() != "ARTICLE") and (ENTRYTYPE.upper() != "INPROCEEDINGS")):
                    continue

                # Check we have not already added this entry from another author:
                already_have = False
                for pubname in os.listdir(os.path.abspath(os.getcwd())+"/_publications"):
                    pub_file = open(os.path.abspath(os.getcwd())+"/_publications/"+pubname, "r")
                    for line in pub_file.readlines():
                        # Extract the original title
                        if "title:" in line:
                            existing_title = line[8:-2]
                            break
                    # Compare the titles
                    if existing_title.upper() == title.upper():
                        already_have = True
                        print("We already have the paper: " + title)
                        break

                # If we already have this entry move on
                if already_have:
                    continue

                # create the url from the doi
                url = ''
                if len(doi) > 1:
                    url = "https://doi.org/" + doi

                # Otherwise add this entry to the publications folder
                print("Found: " + title)
            
                # Create and save the publication
                clean_title = remove_special_chartacters(title)
                clean_title_split = clean_title.split(" ")
                if len(clean_title_split) == 1:
                    clean_title_split.append('')
                markdown_title = first_name + "_" + str(clean_title_split[0]) + clean_title_split[1] + ".md"

                publication_file = open(os.path.abspath(os.getcwd())+ "/_publications/" + markdown_title, "w")
                publication_file.write('---\n')
                publication_file.write('title: "' + make_yaml_safe(title) + '"\n')
                publication_file.write('date: ' + make_yaml_safe(year) + '-01-01\n')
                publication_file.write('venue: "' + make_yaml_safe(venue) + '"\n')
                publication_file.write('paperurl: ' + make_yaml_safe(url) + '\n')
                publication_file.write('authors: "' + make_yaml_safe(author) + '"\n')
                publication_file.write('---')
                publication_file.close()

            print("")
            print("-----------")

if __name__ == "__main__":
    main()