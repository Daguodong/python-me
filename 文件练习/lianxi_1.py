with open('test.txt') as readwhole:
    contents=readwhole.read()
    print(contents.rstrip())

with open('test.txt','w') as writefile:
    writefile.write("\n1 2 3\n")
    writefile.write("4 5 6\n")


with open('test.txt','a') as writefile:    #写入文件  附加在原有文件
    writefile.write("7 8 9\n")

with open('test.txt','w') as writefile:   # #写入文件  清空原有文件
     writefile.write("0\n")