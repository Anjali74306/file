
# c=open("file_question.txt","w")
# c.write("rishabh - meerut\nimtiyaz - delhi\nnilima - cochin\nrati - shimla\nayishan - delhi\nraghu - shimla\naseer - kanpur\nkarthikeyan - delhi\nsalma - jaipur\npankaj - delhi\nbrijesh - delhi\ngovind - delhi\npuneet - shimla\nsiddhi - delhi\nsuman - jaipur\nrajeev - shimla\nmohinder - delhi\nrajendra - jaipur\npriyanka - shimla\nneela - delhi\nsashi - jaipu\nrsarika - delhi\ndeepti - shimla\nharshad - delhi\ntrishna - raipur\npradeep - jaipur\nsekhar - delhi\nnand - delhi\nanoop - delhi\nbalwinder - tokyo")
# c.close()



a=open("file_question.txt","r")
for i in a:
    if "delhi" in i:
        p=open("delhi.txt","a")
        p.write (i)
    elif "shimla" in i:
        t=open("shimla.txt","a")
        t.write(i)
    else:
        s=open("others.txt","a")
        s.write(i)
a.close()








# import os
# t=open("file_question.txt","r")
# ulist=[]
# for i in t:
#     city=""
#     for k in i[::-1]:
#         if k=="-":
#             break
#         if k=="\n":
#             continue
#         else:
#             city+=k
#     if city[::-1] not in ulist:
#         ulist.append(city[::-1])
#         # if os.path.exists(city[::-1]+".txt")==True:
#         #     t=open(city[::-1]+".txt","a")
#         #     t.write(i)
#         # else:
#         d=open(city[::-1]+".txt","w")
#             # d.write(i)
# # for j in ulist:
# #     d=open(j+".txt","w")
# x=open("file_question.txt","r")
# for j in ulist:
#     for s in x:
#         if j in s:
#             p=open(j+".txt","a")
#             p.write(s) 





