from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def parse_jobs(url):
    ''' parse all vacancies '''
    # connect to url
    client = urlopen(url)
    # get raw html
    page_html = client.read()
    # disconnect
    client.close()
    # parse that dada as html
    page_soup = soup(page_html, "html.parser")
    # list of vacancies at the page
    vacancies = page_soup.findAll("li", {"class": "l-vacancy"})
    return vacancies

def get_idees(vac_list):
    ''' returns list of id's from vacancies'''
    idees = []
    for vacancy in vac_list:
        vac_id = vacancy.div["_id"]
        idees.append(vac_id)
    return idees

def idees_from_file(file):
    '''compares id's in file with parsed id's'''
    with open(file) as fout:
        # Work with your open file
        file_ids = fout.readlines()
    return file_ids


def find_new_ids(list_file, list_parsed):
    new_idees = []
    for id in list_parsed:
        if id not in list_file:
            new_idees.append(id)
    return new_idees

def idees_to_file(file, list):
    with open(file, "a") as outf:
        lines = ['{0}\n'.format(line) for line in list]
        outf.writelines(lines)
    return list


