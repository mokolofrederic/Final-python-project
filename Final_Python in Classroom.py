def main():
    try:
        userfile= grabfile()
        readfile(userfile)
    except AttributeError:
        print("No access to the file you are requesting.")
        print("Please contact an IT Support")

def grabfile():
    QuitLoop=False
    while QuitLoop==False:
        try:
            enter_file = input(("PLEASE ENTER YOUR PATHFILE "))
            enter_file = open(enter_file,"r")
            return enter_file
        except FileNotFoundError:
            print("Your file was not found.")

        except PermissionError:
            QuitLoop=True

def readfile(theFile):
    a = 0
    endofsentence = 0 
    report=theFile.read() 
    count = len(report) 
    for a in range(0, count):
        if report[a] == '.' or report[a] == ',' or report[a] == '!' or report[a] == ';' or report[a] == '?' or report[a] == '-' or report[a] == '_' or report[a] == '<' or report[a] == '>':
            endofsentence += 1 
    words = report.split() 
    print(words) 
    validwords = 0 
    testword = 0
    b = 0
    for a in words: 
        testword = words[b]
        testword = len(testword)
        if testword >= 3:
            validwords += 1
        b += 1
       

    numberwords = len(words)
    print("Your number of words is", len(words), "Your total number of valid words is", validwords)
    print("Your total number of sentences is ", endofsentence)
    print("Your average number of words per sentence is", validwords / endofsentence)
main()
