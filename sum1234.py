# sum1=open("sum.txt","w")
# k=sum1.write("1\n2\n3\n4\n5")
s=open("sum.txt","r")
d=s.read()
# print(type(d))
sum=0
for i in d:
    if i=="\n":
       "\n".join
    else: 
      sum=sum+int(i)
print(sum)
