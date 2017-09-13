from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

my_url = "https://jobs.dou.ua/vacancies/?category=Python&beginners="

# connect to url
Client = urlopen(my_url)

# get raw html
page_html = Client.read()

# disconnect
Client.close()

# parse that dada as html
page_soup = soup(page_html, "html.parser")

# list of vacancies at the page
vacancies = page_soup.findAll("li", {"class": "l-vacancy"})

for vacancy in vacancies:
    sign = vacancy.div.div.a.string
    city = vacancy.div.div.findAll("span", {"class": "cities"})[0].text
    company = vacancy.div.div.strong.get_text()
    print(sign)
    print(company)
    print(city)
    print()

