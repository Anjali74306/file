my_file3=open("people1-exercise.txt",mode='r')
# number_of_words=0
# number_of_chars=0
# number_of_lines=0
# for lines in my_file3:
#     number_of_lines+=1
#     line=line.strip("/n")
#     number_of_chars+=len(lines)
#     list=line.split()
#     number_of_words+=len(list+1)
# my_file3.close()
# print("numbers of lines:",number_of_lines)
# print("numbers of chars:",number_of_chars)
# print("number of lines:",number_of_words)
s=my_file3.read()
count=0
for i in s:
    count=count+1
print(count)
my_file3.close()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    