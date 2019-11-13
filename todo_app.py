# Need to make something to hold todos
todos = []

# Need to add functions for each path
def quit():
    raise NameError

def print_todo():
    print("Current todos:")
    for i in range(len(todos)):
        print(f"{i}. {todos[i]}")

def add_todo():
    user_input = input("What do you wish to add to your todo list? ")
    todos.append(user_input)

def complete_todo(todos=todos):
    if len(todos) == 0:
        print("No todos.")
    else:
        try:
            todo_to_remove = int(input("Which todo do you want to remove? "))
            del todos[todo_to_remove]
        except IndexError:
            print("Sorry, we couldn't find that one.")
        except ValueError:
            print("We only accept integers here.")

# Need to make functional way to start and quit
while True:

# Need to make nice main menu
    choice = input("""
        Todo App
========================
0. quit
1. print todo
2. add a todo
3. complete a todo

""")
    try:
        if choice == "0":
            quit()
        elif choice == "1":
            print_todo()
        elif choice == "2":
            add_todo()
        elif choice == "3":
            complete_todo()
    except NameError:
        print("Bye!")
        break

# Need to handle errors of out of range things
# Done :)