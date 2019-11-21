print("Exercise 8.4")


fil = open("desktop/rom.txt")

l = list()

for i in fil:
   i = i.rstrip()
   line = i.split()
   for i in line:
      if i not in l:
         l.append(i)

l.sort()
  
print(l)


print("Exercise 8.5")


fil = open("desktop/tex.txt")

count = 0

for i in fil:
   i = i.rstrip()
   if i.startswith("From "):
      count += 1
      line = i.split()
      email = line[1] 
      print(email)

print(count)



print("Exercise 8.6")


l = list()

while True:
   n = input("Enter a number: ")
   if n == "done":
      break
   else:
      nb = float(n)
      l.append(nb)
      
print("Maximum: ", max(l))
print("Minimum: ", min(l))




































