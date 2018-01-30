'''
Created on Jan 30, 2018

@author: nataliemorel
'''
f=open("poem.txt", "r")
#print(f.read())
# print(f.readline())
text = f.read()
Words= text.split()
print(Words)
print(len(Words))
f.close()
#fw stands for file write
#fw= open("new.txt","w")
#fw.write("hello world!")
fw=open("new.txt","a")
fw.write("Hello ITA!")
f=open("number.txt", "r")
#print(f.read())
x = f.read() #set a variable equal to the file read function
Numbers= x.split()
print(Numbers)
print(len(Numbers))

#write to a new file called "number_write.txt" that includes numbers 0 to 100 
fw=open("numberchallenge.txt", "w")

for y in range (0,101):
    fw.write(str(y) +  " ")

    