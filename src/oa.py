#!/usr/src/python3
# Given a bib file, this script will seach the
# titles of all papers on google scholar
# and try to fetch the eprint/url of the first match
# And save it to output path.


import bibtexparser
import time
from scholarly import scholarly
from scholarly import ProxyGenerator
import requests
import os.path
import sys

def latex_strip(text):
    unwanted = "\{\}\\\(\)\""
    for char in unwanted:
        text = text.replace(char,"")
    return text

def remove_unwanted_chars(text):
    unwanted = "\{\};:,.-_\%\(\)\\\'\""
    for char in unwanted:
        text = text.replace(char,"")
    return text

def get_eid_from_title(title):
    eid = title.split(" ")[0].lower()
    return remove_unwanted_chars(latex_strip(eid))

def get_firstauthor_from_authors(author):
    author = author.lower()
    author = author.split("and")[0]
    if len(author.split(" ")) > 1:
        author = author.split(" ")[1]
    return remove_unwanted_chars(latex_strip(author))

def download_pdf(url,file_name):
    """
    if not url.endswith(".pdf"):
        print("No pdf url: ",url)
        print("File name: ",file_name)
        print()
        return
    """
    try:
        print("Downloading url: ",url)
        req = requests.get(url)
        file = req.content
    except Exception as err:
        print(sys.stderr, err)
        return

    if file[:5] != b'%PDF-':
        print("No pdf at url: ",url)
        print("    File name: ",file_name)
        return
    else:
        print("Got new pdf  : ",file_name)
    with open(file_name, "wb") as fd:
        for chunk in req.iter_content(chunk_size=128):
            fd.write(chunk)

def query_google_scholar(title,author=None,useproxy=False):
    url = None
    try:
        if useproxy:
            pg = ProxyGenerator()
            pg.FreeProxies()
            scholarly.use_proxy(pg)
        print("Query title: ",title)
        print("     author: ",author)
        search_query = scholarly.search_pubs(title)
        sr = next(search_query)
        print(sr)
        print()
        if "eprint" in sr.__dict__["bib"]:
            url = sr.__dict__["bib"]["eprint"]
        elif "url" in sr.__dict__["bib"]["url"]:
            url = sr.__dict__["bib"]["url"]
        else:
            print("No URL in response")
        return url
    except Exception as err:
        print(sys.stderr, err)
        return None

def fetch_eprints_from_bib(bib_path,output_path):
    with open(bib_path) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    for entry in bib_database.entries:
        title = latex_strip(entry["title"])
        author = get_firstauthor_from_authors(entry["author"])
        year = entry["year"]
        filename=output_path + "/" + author + year + get_eid_from_title(title) + ".pdf"

        if os.path.isfile(filename):
            # check if we have the file already
            print("Already have paper: ",title)
            print("            author: ",author)
            print("          filename: ",filename)
            print()
            continue
        url = query_google_scholar(title,author)
        if url is None:
            time.sleep(60)
            continue
        print(url)
        download_pdf(url=url,file_name=filename)
        print("\n")
        time.sleep(60)
    return

def main(bib_path,output_path):

    fetch_eprints_from_bib(bib_path=bib_path,output_path=output_path)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(sys.stderr, "\nUsage: {} FILE_NAME OUTPUT_DIR\n".format(sys.argv[0]))
        sys.exit(1)

    sys.exit(main(sys.argv[1], sys.argv[2]))

