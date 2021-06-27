empty_list = []
print(empty_list)
cars = ["BMW", "HONDA", "AUDI"]
print(cars)
print(cars[0])
num_list = [1,2,3]
sum_num = num_list[1] + num_list[2]
print(sum_num)
more_cars = ["BMW", "HONDA", "AUDI"]
print(more_cars[2])
more_cars[2] = "HYUNDAI"  # to replace the value of the index
print(more_cars[2])
print(more_cars)
print("*" * 20)
car = ["BMW", "HONDA", "AUDI"]
length = len(car)   # to fetch the length of the list
print(length)
car.append("BENZ")  # to Append more values to list
print(car)
car.insert(1, "JEEP")  # to insert more values at any index in between the list
print(car)
x = car.index("AUDI")  # to find out the index of particular value in a list
print(x)
y = car.pop()  # to remove the last item from the list
print(y)
print(car)
car.remove("BMW")
car.insert(0, "HYUNDAI")
print(car)
slicing = car[0:2]  # slicing of list
a = car[1:3]
print(slicing)
print(a)
print(car)
car.sort()  # Sort of list in asc order
print(car)
print("*" * 20)
I = [1,2,4,2,3,1,5,3,6,4,4,4,4,4,4,4,4,7,4,6,8]  # to find the count of a value existing in list
print(I.count(4))