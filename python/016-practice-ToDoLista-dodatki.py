

user_choice = -1
tasks = [] 

def show_tasks ():
        task_index = 1
        for task in tasks:
            print("[" + str(task_index) + "]" + " " + task) 
        task_index += 1 

def add_task():
        task = input("Wpisz zadanie: ")
        tasks.append(task)
        print("Dodano Zadanie!")

def delete_task():
        task_index = int(input("Podaj indeks zadania do skasowania: "))

        if task_index < 0 or task_index > len(tasks) - 1:
            print("Zadanie o tym indexie nie istnieje")
            return

        tasks.pop(task_index)
        print("Skasowano zadanie!")

def save_tasks_to_file():
        file = open("tasks-dodatki.txt", "w")
        for task in tasks:
            file.write(task+"\n")
        file.close()
    
def load_tasks_from_file():
    try:
        file = open("tasks-dodatki.txt")

        for line in file.readlines():
            tasks.append(line.strip())
        
        file.close() 
    except FileNotFoundError:
            return

load_tasks_from_file()

while user_choice != 5:
       
    if user_choice == 1:
        show_tasks()
    
    if user_choice == 2:
        add_task()    

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_tasks_to_file() 

    if user_choice > 5:
        print("Niema Takiej Opcji! - Wybierz od 1 do 5")


    print()     
    print("1. Pokaz zadania")
    print("2. Dodaj zadanie")
    print("3. Usun zadanie")
    print("4. Zapisz zmiany do pliku")
    print("5. Wyjdz")
    print()

    user_choice = int(input("Wybierz liczbe: "))
    print()