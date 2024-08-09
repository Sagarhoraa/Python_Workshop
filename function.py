def summ(a, b):
    c = a + b
    return c

def mul(a, b):
    c = a * b
    return c

def sub(a, b):
    c = a - b
    return c

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    c = a / b
    return c

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = input("What operation to perform? (sum/mul/sub/div): ")

if c == "sum":
    print(summ(a, b))
elif c == "mul":
    print(mul(a, b))
elif c == "sub":
    print(sub(a, b))
elif c == "div":
    print(div(a, b))
else:
    print("Invalid operation")
