# This code records the domain names and figures out which domain has the most messages in the file.

filename = input("Enter a file name: ")                    # user enters the file name
fileopen = open(filename)                                  # opens the file in python 
 
bar = {}                                                   # create an empty dictionary 

for i in fileopen:                                         # loop through file, iterate each line (i)
   if i.startswith("From "):                               # check if the line starts with "From ", only line contains email addresses
       i.rstrip()                                          # right strip the line to remove whitespaces
       l = i.split()                                       # split the line to list, which contains all the words in the line 
       w = l[1]                                            # take the word with email address
       f = w.find("@")                                     # find the possition of "@" char in email address string
       m = w[f+1:]                                         # slice domain part of email address
       bar[m] = bar.get(m, 0) + 1                          # use get function to add domain names and count them 

# In second part of the code we find out domain with maximum messages in inbox.    

mval = None                                                # set None type mval variable                                            
mail = None                                                # set None type mail variable                                            

for i, j in bar.items():                                   # loop through list of tuples of created dictionary 
    if mval == None:                                       # set the values for mval, mail variables as first value-key pair of dictionary 
       mval = j
       mail = i
    elif j > mval:                                         # find the domain with the maximaum value 
       mval = j
       mail = i  
        
print("Domains with their values: ", bar)                  # print out dictionary with domain values
print("Maximal domain and it's value: ", mail, mval)       # print out max domain and value  






































