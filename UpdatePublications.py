import requests
import bibtexparser
import os
import time
from scholar import ScholarQuerier, SearchScholarQuery, ScholarSettings

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

    if last_name.upper() == "DWYER" or last_name.upper() == "ELBAUM":
        continue
       
    # Get the bib
    if uri is not None:
        print("Processing: " + first_name + " " + last_name)

        resp = requests.get(uri)
        bib_database = bibtexparser.loads(resp.text)

        bib_num = 0
        while bib_num < len(bib_database.entries):


            bib = bib_database.entries[bib_num]
            bib_num += 1

            title           = cleanstring(get_details(bib, 'title')).title()
            bibsource       = cleanstring(get_details(bib, 'bibsource'))
            biburl          = cleanstring(get_details(bib, 'biburl'))
            doi             = cleanstring(get_details(bib, 'doi'))
            year            = cleanstring(get_details(bib, 'year'))
            publisher       = cleanstring(get_details(bib, 'publisher'))
            pages           = cleanstring(get_details(bib, 'pages'))
            venue           = cleanstring(get_details(bib, 'booktitle'))
            author          = convert_authors_string(cleanstring(get_details(bib, 'author')))
            ENTRYTYPE       = cleanstring(get_details(bib, 'ENTRYTYPE'))
            ID              = cleanstring(get_details(bib, 'ID'))

            # Check we have no already added this:
            already_have = False
            for pubname in os.listdir(os.path.abspath(os.getcwd())+"/_publications"):
                pub_file = open(os.path.abspath(os.getcwd())+"/_publications/"+pubname, "r")
                for line in pub_file.readlines():
                    if "title:" in line:
                        existing_title = line[8:-2]
                        break
                if existing_title.upper() == title.upper():
                    already_have = True
                    print("We already have the paper: " + title)
                    break

            if already_have:
                continue

            # Use scholar.py to get the abstract
            querier = ScholarQuerier()
            settings = ScholarSettings()
            querier.apply_settings(settings)
            query = SearchScholarQuery()
            query.set_phrase(title + " " + author)
            querier.send_query(query)

            # Find if its too many articles
            found = False
            for art in querier.articles:
                art_title = get_details(art, 'title')
                if title.upper() == art_title.upper():
                    url             = cleanstring(get_details(art, 'url').replace('http://scholar.google.com/', ''))
                    abstract        = cleanstring(get_details(art, 'excerpt')).replace('"', "'")
                    found = True
                    break

            if len(querier.articles) == 0 or found == False:
                print("Oop something when wrong, could not find the google scholar page for this site")
                print("We found: " + str(len(querier.articles)) + " articles with the name - " + str(title + " " + author))
                x = input("Please change your VPN and press enter to continue, type `s` and press enter to skip\n")
                if x.upper() != "S":
                    bib_num -= 1
                continue


            print("Found: " + title)
            # print("url: " + url)
            # print("year: " + year)
            # print("publisher: " + publisher)
            # print("venue: " + venue)
            # print("author: " + author)
            # print("abstract: " + abstract)
            
            markdown_title = first_name + "_" + str(title.split(" ")[0]) + title.split(" ")[1] + ".md"
            # print("Saved as: " + markdown_title)
            # print("---")

            publication_file = open(os.path.abspath(os.getcwd())+ "/_publications/" + markdown_title, "w")
            publication_file.write('---\n')
            publication_file.write('title: "' + title + '"\n')
            publication_file.write('abstract: "' + abstract + '"\n')
            publication_file.write('date: ' + year + '-01-01\n')
            publication_file.write('venue: "' + venue + '"\n')
            publication_file.write('paperurl: ' + url + '\n')
            publication_file.write('authors: "' + author + '"\n')
            publication_file.write('awards: "' + '"\n')
            publication_file.write('---')
            publication_file.close()

            # Please the Google gods
            time.sleep(1)

        print("")
        print("-----------")

            
            
# keys: 'bibsource', 'biburl', 'timestamp', 'doi', 'url', 'year', 'publisher', 'pages', 'booktitle', 'title', 'author', 'ENTRYTYPE', 'ID