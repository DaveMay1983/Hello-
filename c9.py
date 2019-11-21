print("Exercise 9.2")

fn = input("Enter a file name: ")
fil = open(fn)

d = {}

for i in fil:
   if i.startswith("From "):
       i.rstrip()
       l = i.split()
       w = l[2]
       d[w] = d.get(w, 0) + 1 

print(d)



print("Exercise 9.3")



fn = input("Enter a file name: ")
fil = open(fn)
 

bararan = {}

for i in fil:
   if i.startswith("From "):
       i.rstrip()
       l = i.split()
       w = l[1]
       bararan[w] = bararan.get(w, 0) + 1 

print(bararan)





print("Exercise 9.4")



fn = input("Enter a file name: ")
fil = open(fn)
 

bar = {}

for i in fil:
   if i.startswith("From "):
       i.rstrip()
       l = i.split()
       w = l[1]
       bar[w] = bar.get(w, 0) + 1 

mval = None
mail = None

for i, j in bar.items():
    if mval == None:
       mval = j
       mail = i
    elif j > mval:
       mval = j
       mail = i  
        

print(mail, mval)




print("Exercise 9.5")


fn = input("Enter a file name: ")
fil = open(fn)

dic = {}

for i in fil:
   if i.startswith("From "):
       i.rstrip()
       l = i.split()
       w = l[1]
       f = w.find("@")
       m = w[f+1:]
       dic[m] = dic.get(m, 0) + 1 

print(dic)










































