import tasks
from pathlib import Path

filename = Path("tasks.txt")
if not filename.is_file():
    with open("tasks.txt", 'w') as f:
        f.write("")
choice = 0
def main():
    while True:

        print("1. Out all tasks\n" \
        "2. New task\n" \
        "3. mark a task as completed\n" \
        "0. Exit")
        choice = input()
        
        if choice == '1':
            tasks.displaytasks(filename)
        elif choice == '2':
            tasks.newtask(filename)           
        elif choice == '3':
            tasks.marktask(filename)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("wrong choice")
        print("\n")
        print("--------------------------------------------------------")
main()