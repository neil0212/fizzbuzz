my_input = input("Enter a number:")

n=1

try:
    while n<(int(my_input)):
        
        if n%15==0:
            print("fizz buzz")
        elif n%5==0:
            print("buzzes")
        elif n%3==0:
            print("fizzes")
        else:
            print(n)
        n+=1  
    
    print("Fizz buzz counting up to"+" "+ my_input) 
   
    
except ValueError:
    print("number should be int")




    
   