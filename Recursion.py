import turtle


def factorial(num):
    if num==1 or num==0:
        return 1
    return num*factorial(num-1)

def fibonacci(num):
    if num==1:
        return 1
    elif num==0:
        return 0

    return fibonacci(num - 1) + fibonacci(num - 2)

def tree(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        tree(branch_length - 15, t)
        t.left(40)
        tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)


while True:
    print("1. Calculate Factorial")
    print("2. Find Fibonacci Number")
    print("3. Draw a Recursive Fractal Tree")
    print("4. Exit")
    choice = int(input("Please enter a choice:"))

    if choice == 1:
        num=int(input("Please enter a number:"))
        ans=factorial(num)
        print("factorial of ",num," is ", ans)
    if choice == 2:
        num = int(input("Please enter a number:"))
        ans = factorial(num)
        fibonacci(num)
        print(f"The {num}th Fibonacci number is {fibonacci(num)}.")
    if choice == 3:
        print("Drawing fractal tree")
        screen = turtle.Screen()
        t = turtle.Turtle()
        t.left(90)
        t.speed(0)
        tree(100, t)
        screen.exitonclick()
    if choice == 4:
        print("Thanks for using, see you soon!")
        break
    print("--"*30)