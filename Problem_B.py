
# define functions
def convert_string():

    # Open files read and write mode
    fileA = open("/opt/python-app/Output_Problem_A.txt", "r")
    fileB = open("/opt/python-app/tmp_file_B.txt", "w+")

    # read contents from file and striping and replacing comma with newline
    data = fileA.readlines()
    for line in data:
        words = line.strip().replace(",", "\n")
        #print(words)
        fileB.write(words) 
    fileA.close()
    fileB.close() 
# calling function
convert_string()

# define functions
def string_type():
    # Open files read and write mode
    fileB = open("/data/Output_Problem_B.txt", "w+")
    file = open("/opt/python-app/tmp_file_B.txt", "r")
    data1 = file.readlines()

    for line in data1:
        word = line.strip()
        if (word.isalpha()) == True:
           strword = word + " - " + " alphabetical strings"
           fileB.write(strword + "\n")
           #print(strword)
        elif (word.isdigit()) == True:
            strword = word + " - " + " integer "
            fileB.write(strword + "\n")
            #print(strword)
        elif (word.isalnum()) == True:
            strword = word + " - " + " alphanumeric "
            fileB.write(strword + "\n")
            #print(strword)
        elif "." in word:
            f = float(word)
            chk_float = isinstance(f, float)
            if (chk_float) == True:
               strword = word + " - " + " real numbers "
               fileB.write(strword + "\n")
               #print(strword)
        else: 
         print(type(word))
 
    #close files
    fileB.close()
    file.close()

# calling function
string_type()
