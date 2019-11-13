# Need to make something to hold todos
todos = ["There is some stuff", "and", "some other"]

# Need to add functions for each path
def quit():
    raise ValueError

def print_todo():
    print("Current todos:")
    for i in range(len(todos)):
        print(f"{i}. {todos[i]}")

def add_todo():
    user_input = input("What do you wish to add to your todo list? ")
    todos.append(user_input)

# def complete_todo(todos=todos):
#     if len(todos) == 0:
#         print("No todos.")
#     else:
#         todo_to_remove = int(input("Which todo do you want to remove? ")
#         del todos[todo_to_remove]
# complete_todo()
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
        # elif choice == "3":
        #     complete_todo()
    except ValueError:
        print("Bye")
        break

# Need to handle errors of out of range things