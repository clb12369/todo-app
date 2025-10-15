# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = (input("Type 'add/new', 'edit, 'show', 'complete', or 'exit': "))
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo.capitalize() + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo.capitalize() + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Command is not valid. Please enter the number of the todo to be edited.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no todo with that number.")
            continue
    elif user_action.startswith('exit'):
        break
    else: # when none of the previous cases match
        print("Invalid command\nPlease enter 'add or new', 'show', 'edit', or 'complete'")

print('Goodbye.')

