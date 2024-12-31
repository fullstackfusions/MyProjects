def decorator_one(function):
    print("I am in decorator 1")
    def inner():
        num = function()
        return num * (num**num)
    return inner

def decorator_two(function):
    print("I am in decorator 2")
    def inner():
        num = function()
        return (num**num)/num
    return inner
@decorator_one
@decorator_two  # this will be called first
def number():
    return 4

print(number())
# The above decorator returns the following code
# x = pow(4, 4)/4
# print(x*(x**x))