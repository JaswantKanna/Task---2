# Task 2
 Input :
def fibonacci(c) :
    p = 0
    q = 1
    
    if c<= 0 :
        print ("Fibonacci series is impossible")
        
    elif c == 1 :
        print (p)
    
    else :
        print (p)
        print (q)
        
        for i in range (2,c) :
            r = p + q
            p = q
            q = r
            print (r)
            
c = int(input("Enter the number of 'fibonacci numbers' to be printed :\n"))
print ("\nThe fibonacci series of first " + str (c) + " numbers is :  in the sequence\n")
fibonacci (c)

Output :
Enter the number of 'fibonacci numbers' to be printed :
13

The fibonacci series of first 13 numbers is in the sequence :

0
1
1
2
3
5
8
13
21
34
55
89
144

Continued...
