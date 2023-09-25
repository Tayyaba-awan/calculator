def add(n1,n2):
    return n1+n2
def subract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations={"+":add ,"-":subract,"*":multiply,"/":divide}
def calculator():
    num1=float(input("what's the first number "))
    for i in operations:
            print(i)
    should_continue=True
    while should_continue:
        operation_symbol=input("pick an opertion ")
        num2=float(input("what's the next number "))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)
        print(f"{num1}{operation_symbol}{num2}={answer}")
        calculate=input(f"type 'y' to calculating with {answer},or type 'n' to restart the calculation ")
        if calculate=="y":
            num1=answer
        else:
            should_continue=False
            calculator()
calculator()
        
