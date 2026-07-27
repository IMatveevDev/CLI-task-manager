def newtask(filename):
    print("Choice the task or press 0 to cancel the action.")
    file = open(filename, "a")
    content = input()
    if content != '0':
        file.write(content + "\n")
    file.close()

def displaytasks(filename):
    file = open(filename, 'r')
    line = 0
    print("Your Tasks: \n")
    for lines in file:
        line += 1
        print(line,". ",lines.strip(), sep="")
    file.close()

def marktask(filename):
    print("Choice the task number or 0 to cancel the action.")
    file = open(filename, 'a+')
    file.seek(0)
    line = int(input())
    if line != 0:
        lines = file.readlines()
        del lines[line-1]
        file.close()
        file = open(filename, 'w')
        file.writelines(lines)
    file.close()