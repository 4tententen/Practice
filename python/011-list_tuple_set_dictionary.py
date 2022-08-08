#  "data structures"
##########  "list" - Lista ###########

# name_list = []
# name_list.append("Marian")
# name_list.append("zbyszek")
# name_list.append("Juzef")
# name_list.append("Staszek")

# print(name_list)

# names_list = ["Zbyszek", "Zbyszek", "Juzek", "Staszek", "Adam", "Mateusz", "Bartek", "Daniel"]
# names_list2 = ["Anna", "Barbara", "Celina", "Danuta", "Ela", "Justyna"]
# names_list.reverse()
# names_list.sort()

# for name in names_list:
    # print(name)

# print(names_list[0])

# print(names_list.count("Zbyszek"))

# print(len(names_list))

# print(names_list)
# print()
# print(names_list.pop(0))
# print()
# print(names_list)

# names_list.remove("Zbyszek")
# print() 
# print(names_list) 
# print()

# names_list.clear()
# print(names_list)

# names_list3 = names_list + names_list2 
# # print(names_list3)

# names_list3.sort(reverse=True)
# print(names_list3)

########### Tuple - "Krotka"  ##########


# person = ("John", "Rambo", "Marines", 39, "Brown", 177)
# print(person)
# print(len(person))
# print(person.count("Rambo"))


##########  Set - Zbior  ##########

# names_set = {"Marek", "Juzek", "Bartek", "Juzek"}
# # print(names_set)

# names_set2 = set()
# names_set2.add("Dorota")
# names_set2.add("Monika")
# names_set2.add("Justyna")
# names_set2.add("Weronika")
# # print(names_set2)

# names_set2.remove("Dorota")
# names_set2.discard("Monika")
# # print(names_set2)

# # for name in names_set2:
#     # print(name)

# names_set3 = names_set.union(names_set2)
# # print(names_set3)

# for name in names_set3:
#     print(name)

# names_set1 = {"Mama", "Tata", "Dziadek", "Babcia"}
# names_set2 = {"Ciocia", "Kuzynka", "Mama", "Tata", "Dziadek"}

# # names_set3 = names_set1.update(names_set2)
# # print(names_set3)

# # names_set3 = names_set1.difference(names_set2)
# # print(names_set3)

# # names_set3 = names_set1.difference(names_set2)
# names_set3 = names_set1.symmetric_difference(names_set2)
# names_set3.clear()

# for name in names_set3:
#     print(name)
# names_list = ["Gnome", "Bronco", "Brawo"]
# names_list.extend(names_set2)
# print(names_list)


##########  Dictionary  ##########

countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin", "Russia": "Moscow"}
countries_and_capitals["Czechia"] = "Prague"

# print(countries_and_capitals)

# for country, capital in countries_and_capitals.items():
#     print(country + "-" + capital)

# print(countries_and_capitals["Poland"])
# print(countries_and_capitals.get('Poland'))

countries_and_capitals["Poland"] = "Cracow"
# print(countries_and_capitals.pop("Germany"))
# print(countries_and_capitals)
# print(countries_and_capitals.popitem())

if "Poland" in countries_and_capitals:
    print("jest")
elif"":
    print("nie_ma")
else:
    print("dupa")

if "Germany" in countries_and_capitals:
    print("jest")
else:
    print("niema")

