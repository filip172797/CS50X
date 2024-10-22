""" 1 Name string """
# name = input("name?: ")
# name = name.strip()
# name = name.capitalize() # Sets first charachter to uppercase
# name = name.title()      # Sets first charachter in each word to upper case
"""  Prevoius code can be written as name.strip().capitalize().title()
                            or name = input("name?: ").strip().capitalize().title()""" 
# first, last = name.split(" ")
# print(f"hello, {first} wwww {last}")

""" 2 Input """
# x = int(input("x: "))
# y = int(input("y: "))
# print(x+y)
# round(number[, ndigits])'
"""  brackets means optional parameter""" 
# print(round(x/y, 2))
# print(f"{x/y:.2f}")

"""3 Function """
def hello(ss):
    print("hello fucker", ss)

name = input("name: ")
hello(name)


"""
    hello this is a fucking comment
    parameter is what you can put in to a function
    variables is what you actually put in to a function
    sep = separator
    in print, end is a "named parameter"
    name is a string then name.strip(), strip is a method  
"""