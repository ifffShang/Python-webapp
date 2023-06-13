from function import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:&M:%S")
print(now)
print('second edition')
print('third edition')

while True:
    filepath = "todos.txt"
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    todos = []

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos(filepath)
        todos.append(todo)
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos(filepath)
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            todos = get_todos(filepath)
            new_todo = input("Enter a new todo: ") + '\n'
            todos[number - 1] = new_todo
            write_todos(filepath,todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos(filepath)
            todos_to_remove = todos[number - 1].strip('\n')
            todos.pop(number - 1)
            write_todos(filepath,todos)
            message = f"{todos_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print("Bye")