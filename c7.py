
print("Exercise 7.1")

"""

name = input("Enter the file name: ")
fil = open(name)

for i in fil:
    i = i.upper()
    print(i)

"""

print("Exercise 7.2")


"""
name = input("Enter the file name: ")
fil = open(name)

con = 0
tot = 0

for i in fil:
    i = i.rstrip()
    if i.startswith("X-DSPAM-Confidence:"):
        pos = i.find(":")
        n = float(i[pos+2:])
        con += 1
        tot += n

ave = tot/con
print("The average spam confidence is ", ave)

"""



print("Exercise 7.3")


name = input("Enter the file name: ")

try: 
   fil = open(name)
except:
   if name == "na na boo boo":
      print("NA NA BOO BOO TO YOU - You have been punk'd!")
   else:
      print("File cannot be opened: ", name)
   quit() 

count = 0

for i in fil:
   count += 1

print("There are ", count, " lines in the file")


























