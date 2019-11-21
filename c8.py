fileopen = open("desktop/tex.txt")

count = 0

for i in fileopen:
   i = i.rstrip()
   if i.startswith("From "):
      count += 1
      line = i.split()
      email = line[1] 
      print(email)

print("The number of email addresses: ", count)










































