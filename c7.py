# This code calculates the average spam confidence in email box.


filename = input("Enter the file name: ")             # user enters the file name
fileopen = open(filename)                             # opens the file in python

count = 0                                             # set the count variable, number of spam confidence
total = 0                                             # set the total variable, amount of all spam confidence   

for i in fileopen:                                    # loop through file, iterate each line (i)
    i = i.rstrip()                                    # right strip the line to remove whitespaces
    if i.startswith("X-DSPAM-Confidence:"):           # check if the line starts with X-DPSAM, only these lines may contain spam confidence information
        pos = i.find(":")                             # find the : possition, after which digits for confidence value come 
        n = float(i[pos+2:])                          # cut and convert digits(which are string type in file) to float type 
        count += 1                                    # count every spam confidence in the loop
        total += n                                    # add every spam confidence value to total variable 

average = total/count                                 # calculate average spam confidence by deviding total and count variables 
print("The average spam confidence is: ", average)    # print out the result 




































