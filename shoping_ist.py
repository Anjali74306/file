# s=open("shoping_list.txt","w")
# s.write("shoes-50\n")
# s.write("dress-500\n")
# s.write("coldrink-120\n")
# s.write("chocolate-430\n")
# s.close()
t=open("shoping_list.txt","r")
p=t.readlines()
sum=0
for i in p:
    num=""
    for j in i:
        if j.isnumeric()==True:
            num+=j
        else:
            continue
    sum+=int(num)
print(sum)