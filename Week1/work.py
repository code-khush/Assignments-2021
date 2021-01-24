import math
import numpy as np

 

def demo(x):
    return x*x

x=4
print (demo(x))
    
   

def is_palindrome(string):

	for i in range(0, int(len(string)/2)): 
		if string[i] == string[len(string)-i-1]:
			return True

s = "civic"
if (is_palindrome(s)):
	print("True")
else:
	print("False")
   

def sqrt_of_numbers(num):
    return pow(num,1/2)

num=5
print (sqrt_of_numbers(num))
    



arr=[12, 45, 2, 41, 31, 10, 8, 6, 4]
    
length = len(arr) 
arr.sort() 
Max1 = arr[length-1]
Max2 =  arr[1]
print("Maximum number, Second minimum number (", Max1, ",", Max2, ")")


def sort_arr(arr, arr_len): 
      
    l, r = 0, arr_len - 1
    k = 0
    
    while(l < r):  
        while(arr[l] % 2 != 0): 
            l += 1
            k += 1
              
         
        while(arr[r] % 2 == 0 and l < r): 
            r -= 1
              

        if(l < r): 
            arr[l], arr[r] = arr[r], arr[l] 
              

    odd = arr[:k] 
    even = arr[k:] 
    
    even.sort()
    odd.sort() 
      
    even.extend(odd) 
      
    return even 
      

arr_len = 5
arr = [15, 2, 6, 88, 7] 
result = sort_arr(arr, arr_len) 
for i in result: 
    print(str(i) + " ") 
  



A = np.array([[1,3], [2, 4]])
B = np.array([5,6])
x = np.linalg.solve(A, B)

print(x)
