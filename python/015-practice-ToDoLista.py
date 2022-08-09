user_choice = -1



tasks = [] 
tasks.append("Umyj Auto")
tasks.append("Sprzatac Kotlownie")

while user_choice != 5:
    if user_choice == 1:
        print(tasks)
    if user_choice == 2:
        task = input("Wpisz Zadanie: ")
        tasks.append(task)
    if user_choice == 3:
        task

    print()     
    print("1. Pokaz zadania")
    print("2. Dodaj zadanie")
    print("3. Usun zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdz")
    user_choice = int(input("Wybierz liczbe: "))




