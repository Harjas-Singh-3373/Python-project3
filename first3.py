
#Task1
file1=input("Enter your file name : ")
if file1== "sample.txt" :
    file1=open('sample.txt' , 'r')
    reading_file1=file1.readline()
    print("Line 1: " , reading_file1)
    reading_file2=file1.readline()
    print("Line 2: " , reading_file2)

else:
    print("Error: The file 'sample.txt' was not found")


#task 2 
a=input("Enter text to write to the file: ")

file1=open('output.txt' , 'w')
writing_file= file1.write(a)
file1.close()
print("Data successfully written to output.txt")

b=input("Enter additional text to append : ")
file1=open('output.txt' , 'a')
appending_file= file1.write("\n"+b)
file1.close()
print("Data successfully appended. ")
file1=open('output.txt', 'r')
reading_file=file1.read()
print("Final content of output.txt:")
print(reading_file)
