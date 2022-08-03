#  "data structures"
#  "list"

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





# Tuple - "Krotka"


# person = ("John", "Rambo", "Marines", 39, "Brown", 177)
# print(person)
# print(len(person))
# print(person.count("Rambo"))


# Set - Zbior

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

names_set1 = {"Mama", "Tata", "Dziadek"}
names_set2 = {"Ciocia", "Kuzynka", "Mama", "Tata"}

names_set3 = names_set1.update(names_set2)
# print(names_set1)

names_set3 = names_set1.difference(names_set2)
