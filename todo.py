
todolist = []

def view_task():
    for index, item in enumerate(todolist):
        print(f"{index + 1}. {item}")


def add_task():
    new_task = input('What task do you want to add? ')
    todolist.append(new_task)
    
def delete_task():
    del_task = input('What task do you want to delete? ')
    todolist.delete(del_task)

def menu():
    print('Menu: \n1. View list \n2. Add task \n3. Delete task')

menu()
number = int(input())

while number < 4 and number >= 1:

    if number == 1:
        view_task()
        menu()
    elif number == 2:
        add_task()
        menu()
    elif number == 3:
        delete_task()
        menu()

    number = int(input())