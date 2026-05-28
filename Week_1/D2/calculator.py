def calculator(operation, num1, num2):


    def add(num1, num2):
        return num1 + num2
    def sub(num1, num2):
        return num1-num2
    def div(num1,num2):
        return num1/num2
    def mul(num1,num2):
        return num1*num2
    
    
    if(operation == "add"):
        return add(num1,num2)
    elif(operation == "sub"):
        return sub(num1,num2)
    elif(operation == "div"):
        return div(num1,num2)
    elif(operation == "mul"):
        return mul(num1,num2)
    else:
        return "Invalid Operation"
        
    
    
num1= 2 
num2=  6

operation = input("which operation to perform:")
print(calculator(operation, num1, num2))
