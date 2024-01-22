#Alaina Werge
#1/11/24
#To do list Part 2 (5-7)

#Inital
list = []
#Main
def todolist():
    while True:
        print(''' To do List
    1. Add a task to to-do List
    2. View current to-do List
    3. Mark Task as complete
    4. Remove task from to-do List
    5. Remove all items from to-do List
    6. Sort the to-do List alphabetically
    7. Print the number of items in the to-do List
    8. Exit program ''')
        option = int(input("Option: "))
        if option == 1:
            addtask = str(input("Enter Task: "))
            list.append(addtask)
        if option == 2:
            print(list)
        if option == 3:
            complete = str(input("Mark Complete: "))
            list.remove(complete)
            list.append(complete + "X")
            print('''   
                            (::::::'              )
                            |`-----._______.-----'|
                            |              :::::::|
                           .|               ::::::!-.
                           \|               :::::/|/
                            |               ::::::|
                            |      Congrats!   :::|
                            |    You completed :::|
                            |        A Task! :::::|
                            |              .::::::|
                            J              :::::::F
                             \            :::::::/
                              `.        .:::::::'
                                `-._  .::::::-'
                                    |  """|"
                                    |  :::|
                                    F   ::J
                                   /     ::\                                        
                              __.-'      :::`-.__
                             (_           ::::::_)
                               `"""---------"""' ''')
        
        if option == 4:
            remove = str(input("Remove Task: "))
            list.remove(remove)
        if option == 5:
            list.clear()
        if option == 6:
            list.sort()
            print(list)
        if option == 7:
            print(len(list))
        if option == 8:
            break
        if option > 8:
            print("Input Invalid")
        if option < 1:
            print("Input Invalid")

todolist()