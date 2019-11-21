print("Exercise 10.1")

"""
fn = input("Enter a file name: ")
fil = open(fn)

d = {}

for i in fil:
    if i.startswith("From "):
        i.rstrip()
        l = i.split() 
        w = l[1]
        d[w] = d.get(w, 0) + 1

t = []

for i, j in d.items():
    t.append((j, i))

t = sorted(t, reverse = True)

for i, j in t:
    print(j, i)

print("Most common: ")
print(t[0][1], t[0][0])

"""

"""
print("Exercise 10.2")
 

fn = input("Enter a file name: ")
fil = open(fn)

d = {}

for i in fil:
    if i.startswith("From "):
        i.rstrip()
        l = i.split() 
        time = l[5]
        hour = time.split(":")
        w = hour[0]
        d[w] = d.get(w, 0) + 1

t = sorted(d.items())

for i, j in t:
    print(i, j)

"""

print("Exercise 10.3")


f = open("desktop/tex.txt")

d = {}

for i in f:
   i.rstrip()
   words = i.split()
   for i in words:
       for j in i:
          j=j.lower() 
          if j >="a" and j <= "z":
             d[j] = d.get(j, 0) + 1



         
print(sorted( [ (i, j) for (j, i) in d.items()], reverse=True))









 


         


























