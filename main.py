import tasks
enter = 1
def main():
    while True:

        print("1. Out all tasks\n" \
        "2. New task\n" \
        "3. mark a task as completed\n" \
        "0. Exit")
        enter = input()
        
        if enter == '1':
            tasks.displaytasks()
        elif enter == '2':
            tasks.newtask()           
        elif enter == '3':
            tasks.marktask()
        elif enter == '0':
            print("Goodbye!")
            break
        else:
            print("wrong choice")
        print("\n")
        print("--------------------------------------------------------")
main()