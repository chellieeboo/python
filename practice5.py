# def function name (parameters):
#     """docstring""" 
#     statement(s)| 

#call function
#def my_function():
    #"""This is a docstring."""
    #print("Hello World!")

    #def my_function(fname):
   # print("hello , fname")
    #my_function1("merl")

 #arbitrary arguments *args
# tuple a list of values


def my_function(*pets):
 print(pets[0])
my_function("2020", "Yuki" "Tommy")

def my_function(box3, box2, box1):
    print("The largest box is " + box3)
my_function(box1 = "Oven Toaster", box2 = "Stand Fan", box3 = "Washing Machine")

#kwargs may keyword
#dictionary json format
def my_function(**fruits):
   print("red", fruits["red"])
my_function(blue = "banana", red = "apple", green = "grapes")
#output red apple

#default parameter value
def my_function(name, age=18):
    print(f"{name}: {age}")

my_function("Heartlene", 16)
my_function("Delbert")
my_function("Keith")
my_function("Mirmel", 20)


#output
#heartlene: 16 
#Delbert: 18

#passing a list as an argument

def my_function7(prutas):
  for f in prutas:
     print(f)
    
fruits = ["banana", "apple", "mango"]
my_function7(fruits)
    #output
    #banana
    #apple

def my_function8(score):
       return score + 2
    
print(my_function8(13))
print(my_function8(15))
print(my_function8(19)) 

def my_function():
     pass






 

