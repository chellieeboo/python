
def first_function(**fruits):
    print(f'First function call Red="{fruits["red"]}", yellow="{fruits["yellow"]}", green="{fruits["green"]}", orange="{fruits["orange"]}"')

def second_function(**fruits):
    print(f'Second function call yellow="{fruits["yellow"]}", green="{fruits["green"]}", orange="{fruits["orange"]}", red="{fruits["red"]}"')

def third_function(**fruits):
    print(f'Third function call green="{fruits["green"]}", red="{fruits["red"]}", yellow="{fruits["yellow"]}"')


color = input("Enter color (Red, Yellow, Green): ")

if color not in {"red","yellow","green"}:
    print("No color invalid")
elif color == "red":
    first_function(red="apple", yellow="banana", green="kiwi", orange="Orange")
elif color == "yellow":
    second_function(red="cherry", yellow="mango", green="honeydew", orange="melon")
elif color == "green":
    third_function(red="dragon fruit", yellow="lemon", green="papaya")













   
