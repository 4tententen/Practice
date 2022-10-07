#####  exceptions - wyjatki  #####



countries_and_capitals = {"Poland": "Warsaw", "Czechia": "Prague", "Germany": "Berlin"}

try:
    # print(2 / 0)
    print(countries_and_capitals["USA"])
except KeyError:
    print("Niema klucza: ")
# except ZeroDivisionError:
    # print("Nie dzielimy przez Zero!")
finally:
    print("To wykona sie zawsze")

print("Jestem Tutaj")





