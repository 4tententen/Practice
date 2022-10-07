#####  File-Save-Read  Pliki-Zapis-Odczyt #####



file = open("countries_and_capitals.txt", "w+")

countries_and_capitals = {"Poland": "Warsaw", "Germany": "Berlin", "Russia": "Moscow"}

for country, capital in countries_and_capitals.items():
    file.write(country + " " + "-" + " " + capital + "\n")

file.close


#####

file = open("countries_and_capitals.txt")
for line in file.readlines():
    print(line.strip())

file.close()


