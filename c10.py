# This code reads a file and prints the letters in decreasing order of frequency.

f = open("desktop/text.txt")                                       # opens the file from directory

d = {}                                                             # create an empty dictionary 

for i in f:                                                        # loop through file, iterate each line (i)
   i.rstrip()                                                      # right strip the line to remove whitespaces    
   words = i.split()                                               # split the line to the list of words of line
   for i in words:                                                 # iterate through elements(words) of list
       for j in i:                                                 # iterate through letters of each word
          j=j.lower()                                              # convert all the letters to lower case
          if j >="a" and j <= "z":                                 # check if the char is a letter ("a" to "z")
             d[j] = d.get(j, 0) + 1                                # using get function add all letters to the dictionary and count them   

            
# one line code for printing out the letters in each line one letter with it's frequency in decreasing order        

print(sorted( [ (i, j) for (j, i) in d.items()], reverse=True)) 







 


         


























