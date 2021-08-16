import requests
import json
from collections import OrderedDict
from numpy.lib.function_base import append

with open('C:\\Users\\q\\Desktop\\Python\\SummitMinds Task\\prize.json') as data_file:
    data = OrderedDict(json.load(data_file))


def main_function():
    print('1. Search a Nobel prize winner by name.')
    print('2. Find out Nobel prize winner in a year input by him.')
    print('3. Search Prize winner based on the year and category (Peace/Chemistry/Physics etc...)')
    print('4. Show a list of all Winners in Alphabetical order (With year and category against the name)')
    print('5. To Stop.')
    option_number = input("Enter Option Number: \n")
    if option_number == str('1'):
            nb_winner = input("Search by name: \n")
            # print(data['prizes'])
            for prize in data['prizes']:
                for name in prize['laureates']:
                    if nb_winner in name['firstname']+ ' ' +name['surname']:
                        print(name['firstname'] + ' ' +name['surname'] )
                        print(prize['year'])
                        print(prize['category'])
            main_function()        
    if option_number == str('2'):
            nb_winner_year = input("Find by year : \n")
            # print(data['prizes'])
            for prize in data['prizes']:
                    if nb_winner_year in prize['year']:
                        for name in prize['laureates']:
                            print(name['firstname'] + ' ' +name['surname'] )
                            print(prize['year'])
                            print(prize['category'])
            main_function()
    if option_number == str('3'):
            nb_winner_year,nb_winner_category = input("Search Prize winner based on the year and category : \n").split()
            # print(data['prizes'])
            for prize in data['prizes']:
                    if nb_winner_year in prize['year'] and nb_winner_category in prize['category']:
                        for name in prize['laureates']:
                            print(name['firstname'] + ' ' +name['surname'] )
                            print(prize['year'])
                            print(prize['category'])
            main_function()
    if option_number == str('4'):
            names, year, category= [], [], []
            for prize in data['prizes']:
                    for name in prize['laureates']:
                        
                        names.append(name['firstname'] + ' ' +name['surname'])
                        year.append(prize['year'])
                        category.append(prize['category'])

            final_deatils = [{"name": n,"year": y, "category":c} for n, y, c in zip(names, year, category)]
            final_data = sorted(final_deatils, key=lambda k: k["name"])
            for details in final_data:
                        print(details['name'] )
                        print(details['year'])
                        print(details['category'])
            main_function()
    
    if option_number == str('5'):
        quit()
            
    else:
            print("Please Select Option Out of 5 ")
            main_function()
main_function()

    