# Enter first number: 10
# Enter second number: 5

# Result: 15

def calculate(n1,op,n2):
    #add
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2    
    elif op == "/":
        if n2 != 0:
            return n1 / n2
        else:
            return None  
    else:
        return None

while True:
    choice=input("q to quit and u to use").lower()
    
    
    if choice=="u":
        n1=float(input("enter first no"))
        op=input("enter operator")
        n2=float(input("enter second no"))
        result = calculate(n1, op, n2)
        print("Result:", result)
    if choice=="q":
        break
    elif choice != "u":
        print("Invalid choice")

# def greet():
#     print("Hello")

# greet()