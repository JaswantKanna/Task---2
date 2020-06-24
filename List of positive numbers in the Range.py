# To print all positive numbers in the range
 Input :
c = int(input ("Enter number of elements in the list\n "))
list = []
output = []

for p in range (1,c+1) :
    element = int(input ("\nEnter the respective number " + str(p) + " of the list :\n"))
    list.append(element)
    
print ("\nList is :\n" ,list)

for x in range (0,c) :
    
    if list [x] >= 0 :
        output.append(list [x])
    
    else :
        continue
        
print ("\nPositive numbers in the above List is :\n" ,output)

Output :
Enter number of elements in the list
 4

Enter the respective number 1 of the list :
7

Enter the respective number 2 of the list :
6

Enter the respective number 3 of the list :
2

Enter the respective number 4 of the list :
1

List is :
 [7, 6, 2, 1]

Positive numbers in the above List is :
 [7, 6, 2, 1]

