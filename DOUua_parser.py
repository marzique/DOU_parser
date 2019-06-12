from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


def get_vacancies():
    my_url = "https://jobs.dou.ua/vacancies/?category=Python&exp=0-1"

    Client = urlopen(my_url)
    page_html = Client.read()
    Client.close()

    page_soup = soup(page_html, "html.parser")

    vacancies_list = page_soup.findAll("li", {"class": "l-vacancy"})
    vacancies = []
    for vacancy in vacancies_list:
        name = vacancy.div.div.a.get_text()
        city = vacancy.div.div.findAll("span", {"class": "cities"})[0].get_text()
        company = vacancy.div.div.strong.get_text()
        if city in ["Киев", "Київ", "Kyiv"]:
            vacancy = {}
            vacancy["name"] = name
            vacancy["company"] = company
            vacancies.append(vacancy)

    print(vacancies)


get_vacancies()
