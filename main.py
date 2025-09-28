
# Task1 
n=input("Enter student's name:")
dict= {'Alice': 83 , 'Mike': 95 , 'Sam': 45 , 'Karl': 63}
if n== 'Alice':
    print("Alice's marks: " , dict['Alice'])
elif n=='Mike':
    print("Mike's marks: " ,dict['Mike'])
elif n=='Sam':
    print("Sam's marks: " ,dict['Sam'])
elif n=='Karl':
    print("Karl's marks: " ,dict['Karl'])
else:
    print("Student not found")
print("Thank's for using python")



#Task2

list=[1,2,3,4,5,6,7,8,9,10]
print("Extract first five elements:" , list[0:5:])
list.reverse()
print("Reversed extracted elements:", list[5:10])
