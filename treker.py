def newtask():
    file = open("test.txt", "a")
    content = input()
    file.write(content + "\n")
    file.close()
def outtasks():
    file = open('test.txt', 'r')
    line = 0
    print("Your Tasks: \n")
    for lines in file:
        line += 1
        print(line,". ",lines.strip(), sep="")
    file.close()
def marktask():
    print("Enter num task or enter 0 if you dont")
    file = open("test.txt", 'a+')
    file.seek(0)
    line = int(input())
    if line != 0:
        lines = file.readlines()
        del lines[line-1]
        file.close()
        file = open("test.txt", 'w')
        file.writelines(lines)
    file.close()
enter = 1
while True:

    print("1. Out all tasks\n" \
    "2. New task\n" \
    "3. Mark complete task\n" \
    "0. Exit")
    enter = int(input())
    match enter:
        case 1:
            outtasks()
        case 2:
            newtask()           
        case 3:
            marktask()
        case 0:
            break
    print("\n")
    print("--------------------------------------------------------")
    print("hello world")