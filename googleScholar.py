from scholarly import scholarly
from fp.fp import FreeProxy
import os.path
from slugify import slugify

def get_authors_names():
    authors_names = []
    for filename in os.listdir(os.path.abspath(os.getcwd())+"/_team"):
        author_file = open(os.path.abspath(os.getcwd())+"/_team/"+filename, "r")

        for line in author_file.readlines():
            if "first_name" in line:
                first_name = line.split(':')[1].lstrip().rstrip("\n")
            if "last_name" in line:
                last_name = line.split(':')[1].lstrip().rstrip("\n")
            if "tier" in line:
                tier = line.split(':')[1].lstrip().rstrip("\n")
        if (tier.upper() == "GRADUATE STUDENTS"):
            authors_names.append(first_name + " " + last_name + ", University of Virginia")

    return authors_names

def set_new_proxy():
    print("Searching proxy")
    while True:
        proxy = FreeProxy(rand=True, timeout=1).get()
        proxy_works = scholarly.use_proxy(http=proxy, https=proxy)
        if proxy_works:
            break
    print("Found a working proxy:", proxy)
    return proxy

def get_author(author_name):
    print("Searching: " + author_name+'\n')

    while True:
        try:
            author_query = scholarly.search_author(author_name)
            author = next(author_query)
            break
        except Exception as e:
            print("Trying new proxy")
            set_new_proxy()

    while True:
        try:
            filled_author = author.fill()
            print("Author found\n")
            break
        except Exception as e:
            print("Trying new proxy")
            set_new_proxy()

    return filled_author

def get_author_with_tor(author_name):
    scholarly.use_tor(tor_sock_port=9050, tor_control_port=9051, tor_pw="google_scholar_password")

    author_query = scholarly.search_author(author_name)
    filled_author = next(author_query).fill()
    
    return filled_author

def get_publication(publication_name):
    print("Searching: " + publication_name + '\n')

    while True:
        try:
            publication_query = scholarly.search_pubs(publication_name)
            publication = next(publication_query)
            break
        except Exception as e:
            print(e)
            print("Trying new proxy")
            set_new_proxy()

    while True:
        try:
            filled_publication = publication.fill()
            break
        except Exception as e:
            print(e)
            print("Trying new proxy")
            set_new_proxy()
    return filled_publication

def get_publication_with_tor(publication_name):
    scholarly.use_tor(tor_sock_port=9050, tor_control_port=9051, tor_pw="google_scholar_password")

    publication_query = scholarly.search_pubs(publication_name)
    filled_publication = next(publication_query).fill()
    
    return filled_publication

def check_if_publication_exists(publication_name):
    return os.path.isfile(os.path.abspath(os.getcwd())+"/_publications/"+slugify(publication_name)+".md")

def convert_authors_string(authors_string):
    final_authors = ""
    authors_string = authors_string.replace(',', '')
    # split the name using and
    individual_authors = authors_string.split(" and ")
    for i in range(len(individual_authors)):
        author = individual_authors[i]
        names = author.split(" ")
        full_name = ""
        for n in reversed(names):
            if len(full_name) > 0:
                full_name += " "
            full_name += n
        if len(final_authors) > 0:
            if i == len(individual_authors) - 1:
                final_authors += " and "
            else:
                final_authors += ", "
        final_authors += full_name
    
    return final_authors

def save_publication(publication, debug = False):
    if not debug:
        publication_file = open(os.path.abspath(os.getcwd())+"/_publications/"+slugify(publication.bib['title'])+".md", "w")
        publication_file.write("---"+"\n")
        publication_file.write("title: '"+publication.bib['title']+"'\n")
        publication_file.write("abstract: "+publication.bib['abstract']+"\n")
        publication_file.write("date: "+publication.bib['year']+"\n")
        publication_file.write("venue: "+publication.bib['venue']+"\n")
        publication_file.write("paperurl: "+publication.bib['url']+"\n")
        publication_file.write("authors: "+convert_authors_string(publication.bib['author'])+"\n")
        publication_file.write("---")
        publication_file.close()
    else:
        print("---"+"\n")
        print("title: '"+publication.bib['title']+"'\n")
        print("abstract: "+publication.bib['abstract']+"\n")
        print("date: "+publication.bib['year']+"\n")
        print("venue: "+publication.bib['venue']+"\n")
        print("paperurl: "+publication.bib['url']+"\n")
        print("authors: "+convert_authors_string(publication.bib['author'])+"\n")
        print("---")
    print("Saved!\n")

# Start Running the Script
set_new_proxy()

authors = get_authors_names()

for author in authors:
    
    filled_author = get_author(author)
    publications = [pub.bib['title'] for pub in filled_author.publications]
    for publication in publications:
        if check_if_publication_exists(publication):
            continue
        filled_publication = get_publication(publication)
        print(filled_publication)
        save_publication(filled_publication, True)