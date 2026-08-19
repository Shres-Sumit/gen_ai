#List

#empty list 
my_list = []
my_list =list()


#with values
fruits = ["apple", "banana", "cherry"]
numbers = [1,2,3,4,5]
random_list = ["abc",1,1.0,True]


#Adding elements to a list 
fruits.append("orange") 
fruits.insert(1,"mango")
fruits.extend(["kiwi","grapes"])


#removing elements from a list
fruits.remove("banana")
print(fruits)
fruit = fruits.pop()
print(fruit)
fruit = fruits.pop(1)
print(fruit)
fruits.clear()

#Accessing and searching
fruits = ['apple', 'banana', 'orange', 'banana']
print(fruits[0])
print(fruits[-1])
print(fruits.index("apple"))
print(fruits.count("banana"))


#sorting
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
reversed = fruits.reverse()
print(reversed)

#copying
copy_fruits = fruits.copy()
print(copy_fruits)
slice_copy_fruits = fruits[:]
print(slice_copy_fruits)


#Tuple(Immutable, Ordered, Allow Duplicates)
my_tuple = ()
my_tuple = tuple()

#with values
datas = (5,10)
single_data = (5,)
print(datas)
print(single_data)
colors = ("black","white","blue","white")
print(colors)


#accessing
color = colors[1]
print(color)
#searching
color = colors.index("black")
count = colors.count("white")
print(color, count)

#Tuple Unpacking
coordinates = (400,500)
x , y = coordinates
print(x,y)


roll = (1,2,3,4,5)
x , *rest = roll
print(x)
print(*rest)




#Set
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}

#Adding
set1.add(6)
set1.update([7,8,9,10])
print(set1)


#remove
set1.remove(2)
print(set1)
set1.discard(18)
print(set1)
pop1 = set1.pop()
print(pop1)
set1.clear()
print(set1)

set3 = set1.copy()
print(set3)




#Dictionary
my_dict = {}
my_dict = dict()

person = {
    "name" : "sumit",
    "roll" : 10,
    "age" : 15
}

print(person)
person = dict(name="sumit",age=10,roll = 15)
print(person)

#Accessing Values
person = {'name': 'John', 'age': 30, 'city': 'New York'}
print(person["name"])
print(person.get("age"))
print(person.get("salary",0))

#Updating or adding value
person["email"] = "sumit@gmail.com"
person["age"] = 30

print(person)

person.update({'name' : "sumit" , "city":"bhaktapur"})
print(person)

keys = person.keys()
print(keys)

values = person.values()
print(values)

items = person.items()
print(items)