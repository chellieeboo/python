name = input("Enter employee name: ") 
salary = input("Enter salary name:")
company = input("Enter company name:")

print("\n")
print("Printing Employee Details:")
print(" Name: ", name)
print(" Salary: ", salary)
print(" Company: ", company)

age = (input("Enter your age: "))
print("Your age is: " + age)

name, add, age, gpa = "Rochelle Bayogbog", "Sison, Pangasinan", 19, 98.2 
print(f"My name is {name} and i live in {add}. I am {age} years old".format(name, add, age))

num = 12345678.98765432

#fromatting float number
print("Rounded off to the nearest integer: {:.0f}".format(num)) #12345679
print("Format 2 decimal places: {:.2f}".format(num)) #12345678.99
print("Format 4 decimal places: {:.4f}".format(num)) #12345678.9877

#Separator
print("Thousand separator: {:,}".format(num)) #12,345,678.98765432
#separator and floating value
print("Thousand separator with 2 decimal places: {:,.2f}".format(num)) #12,345,678.99
#if-string with separator and floating value
print(f"Thousand separator with 2 decimal places: {num:,.2f}") #12,345,678.99
#if -string with separator and floating value, right aligned
print(f"Right aligned: {num:>20,.2f}") 
#if -string with separator and floating value, left aligned
print(f"Left aligned: {num:<20,.2f}")

#if -string with separator and floating value, centered
print(f"Centered: {num:^20,.2f}")