from helpers import *
import tkinter
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

my_url = "https://jobs.dou.ua/vacancies/?category=Python&beginners="

file_id = "idees.txt"
file_test = "idees2.txt"

# get list of html blocks
vacancies = parse_jobs(my_url)
# parse each vacancy id
idees = get_idees(vacancies)

# ids already in file
old_ids = idees_from_file(file_id)
test_ids = idees_from_file(file_test)

new_ids = find_new_ids(test_ids, old_ids)

stripped_new = ['{0}'.format(line.strip()) for line in new_ids]

# ['{0}\n'.format(line) for line in list]

print(new_ids)
# for id in old_ids:
#     print(id.strip())

#
# # append id to file
# idees_to_file(file_id, fresh_ids)







# for vacancy in vacancies:
#     sign = vacancy.div.div.a.string
#     city = vacancy.div.div.findAll("span", {"class": "cities"})[0].text
#     company = vacancy.div.div.strong.get_text()
#     vac_id = vacancy.div["_id"]
#
#     idees.append(vac_id)
#
#     print(sign)
#     print(company)
#     print(city)
#     print()





