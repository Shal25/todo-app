from functions import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

todos = []
while True:
    b = input("Enter show,add,edit,complete and exit:")

    if b.startswith("add"):
        c = b[4:]

        todos = get_todos()

        todos.append(c + "\n")

        write_todos(todos)

    elif b.startswith("show"):
        todos = get_todos()

        for x, y in enumerate(todos):
            y = y.strip('\n')
            row = f"{x + 1}-{y}"
            print(row)

    elif b.startswith("edit"):
        try:
            x = int(b[5:])
            x = x - 1

            todos = get_todos()
            new = input("Enter new todo:")
            todos[x] = new + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif b.startswith("complete"):
        try:
            x = int(b[9:])
            todos = get_todos()
            index = x - 1
            todos_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todos {todos_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is not item with that number")
            continue

    elif b.startswith("exit"):
        print("Bye!")
        break
    else:
        print("Command is not valid.")
