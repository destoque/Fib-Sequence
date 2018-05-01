#Version of Python 3.5.2 
#
import sys

def fib(n):
    if(n <= 1):
        return n
    else:
        return(fib(n-1) + fib(n-2))
    
   


try:
  n =int(input("How many terms would you like in your Fibonacci sequence?"))
  
except ValueError:
    print ("You didn't enter a integer")
    sys.exit() #Getting out of the code
else:
    print("Fibonacci range:")

def main():  
    fib(n)
    for numbers in range(n):
        print (fib(numbers))
main()
