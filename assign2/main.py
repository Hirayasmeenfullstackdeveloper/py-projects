text : str = "hello world"
numbers : int = 10
decimal_value : float = 10.5
boolean : bool = True
mutable_collection_of_data : list[int] = [1,2,3,4,5]
immutable_collection_of_data : tuple[int,str,float] = (1,"hello",3.14)
object_data : dict[str,str] = {"name":"Hira Yasmeen","father_name":"Abdul Wahid"} #its not uses indexes call with its value
person_data : list[str] = ["Hira Yasmeen","Abdul Wahid","19"]
unique_values :set[int]= {1,1,12,33,45,55,2,2,3} # set is unorder and also muetable
immutable_uniques_values :frozenset[int] = {1,1,12,33,45,55,2,3,3} #when you make a set immutable use FrozenSet

#jo hum nai numbers diye hein usko range batata h hum just start or end point dai diya
numbers_list:list[int] = range(1,20)
for num in range(1,20):
    print(num)
    print(chr(99)) #chr by default function

a = 6
b = a
b = 7
print(id(a)) # id is a function
print(id(b))

c=8
print(c)
print(type(c))
str(c)
print(type(str(c)))

khan = 7
if type(khan) == int:
    print("khan is an integer")
else:
    print("c is not an integer")

b:int = 0
print(isinstance(b,int))  
print(isinstance(b,float))  

# ----------------OPERATORS-----------------------
#Add +
a = 5
print(5+2)

#sub -
b = 6
print(6-3)

#Multiply *
c = 7
print(7*8)

#Division /
d = 20 
print(20 / 5)

#Modules % reminder deta h 
e = 7
print(7 % 4)

# //{floor division} agey sai . value remove krdeta h 
f = 56
print(56 // 6)

#**
g = 2
print(2**2)

a = 7
b = 8
print(a is not b)
#   ----------------------IDENTITY OPERATORS-------------------------------  [is or is not]
a = True
print (a is True)
print (a is not True)
# --------------------------MEMBERSHIP OPERATORS------------------------------ [in or not in]
names : list[str] = ["Yousma", "Hira", "Amna"]
result = "Amna" in names
result1 = "Amna" not in names
print(result)
print(result1)

# Comparison Operators

X = 10

Y = 4

print("X is equal to Y:", X == Y) # False (X is not equal to Y)

print("X is not equal to Y:", X != Y) # True (X is not equal to Y)

print("X is greater than Y:", X > Y) # True (X is greater than Y)

print("X is less than Y:", X < Y) # False (X is not less than Y)

print("X is greater than or equal to Y:", X >= Y) # True (X is greater than Y)

print("X is less than or equal to Y:", X <= Y) # False (X is not less than Y)


#Logical Operators

x = True

y = False

print("x and y is:", x and y) # False (x and y both are not true)

print("x or y is:", x or y) # True (x is true)

print("not x is:", not x) # False (x is true so not x is false)

#Bitwise_Operators

# NOT (~):

# This operator inverts the bits of the number (also called the bitwise complement).

# It changes all 1 bits to 0 and all 0 bits to 1.

a = 5 # (0101 in binary)

result = ~a #~0101 = 1010 (binary), which is -6 (decimal)

print(result) # Output: -6



b = 7 # (0111 in binary)



result = b # ~0111 = 1000 (binary), which is -8 (decimal)

print(result)   # Output: -8