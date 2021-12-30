
#Import module

import random
import string

#Open file in write mode
file = open("/opt/python-app/Output_Problem_A.txt", "w+")

#Variable declare
num_str = 50
num_char = 10

for i in range(num_str):
    #Generating alphabetical
    alphabetical = string.ascii_lowercase
    alpha = str(''.join(random.choice(alphabetical) for i in range(num_char)) + ',')
    file.write(alpha)

   #Generating integer
    integer = string.digits
    num = str(''.join(random.choice(integer) for i in range(num_char)) + ',')
    file.write(num)

   #Generating alphanumeric
    alphanumeric = string.ascii_lowercase + string.digits
    alphanu = str( ''.join(random.choice(alphanumeric) for i in range(num_char)) + ',' )
    file.write(alphanu)

   #Generating real numbers
    realnum = str( random.uniform(1,1312)) + " ,"
    file.write(realnum)
#Close file
file.close()
