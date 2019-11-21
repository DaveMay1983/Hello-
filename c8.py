# This code calculates the number of email addresses in mail inbox and prints out all emails.

fileopen = open("desktop/tex.txt")                         # opens the file from directory

count = 0                                                  # set the count variable, number of email addresses

for i in fileopen:                                         # loop through file, iterate each line (i)
   i = i.rstrip()                                          # right strip the line to remove whitespaces 
   if i.startswith("From "):                               # check if the line starts with "From ", only these lines may contain inbox email address
      count += 1                                           # count every email address in the loop
      line = i.split()                                     # split the line and create list of words, one of them contains the email address
      email = line[1]                                      # take email address name from the list 
      print(email)                                         # print out email address

print("The number of email addresses: ", count)            # print out the total number of email addresses











































