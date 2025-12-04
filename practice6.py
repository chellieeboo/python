# python strings
txt = "Hello World"
print(txt)
print(txt[0])  # H
print(txt[2:8])  # llo Wo
print(txt[1:])  # ello World!
print(txt * 2)  # Hello World!Hello World!
print(txt + " Test")  # Hello WorldTest

#python join method
# iterable string or tuple
str = '.'. join('NLAC')
print(str)  # N.L.A.C

for s in str:
    print(s+ ".")

    str = "I love NLAC. I'ts more fun in NLAC"
    strcount = str.count('e',10,15) 

    address = "Artacho, Sison, Pangasinan"
    #first occurrence of Sison
    addrr = address.find("a")
    print(addrr)  

    #python string split method
    address = "Artacho, Sison, Pangasinan"
    addr = address.split()
    print(addr)  # ['Artacho', 'Sison', 'Pangasinan']

    addr = address.split(",")
    print(addr)  # ['Artacho', ' Sison', ' Pangasinan']

    addr = address.split(",", 1)
    print(addr)  # ['Artacho', ' Sison, Pangasinan']

    #python list
    a = [5, 10, 15, 20, 25, 30, 35, 40]
    print(a[2])
    print(a[0:3])
    print(a[5:])

    #output
    
    #list append()
    fruits = ["banana", "apple", "Mango"]

    fruits.append("Orange")
    print(fruits)

    for f in fruits:
        print(f)

        colors = ["red", "yellow"]
        colors.append(fruits)
        print(colors)
        #output
        #['banana', 'apple', 'Mango', 'Orange'] 
       








  




    
