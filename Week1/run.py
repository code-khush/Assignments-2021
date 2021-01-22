## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5,99,36,54,88]
for x in arr:
    
    if x % 2 != 0:
        print (x)

'''
Problem - 1
Print all the prime numbers from 0-100
'''
 
for i in range(0,100):
  if i>1:
    for j in range(2,i):
        if(i % j==0):
            break
    else:
        print(i)  

'''
Problem - 2
Print the reverse of a string
'''
def reverse(string): 
    string = string[::-1] 
    return string 
  
string = 'Reverse Me!'
  

print (reverse(string)) 


