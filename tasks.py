def newtask():
    print("Enter the task or press 0 to cancel the action.")
    file = open("test.txt", "a")
    content = input()
    if content != '0':
        file.write(content + "\n")
    file.close()
    
def displaytasks():
    file = open('test.txt', 'r')
    line = 0
    print("Your Tasks: \n")
    for lines in file:
        line += 1
        print(line,". ",lines.strip(), sep="")
    file.close()

def marktask():
    print("Enter the task number or 0 to cancel the action.")
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