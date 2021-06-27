d = {}  # creating Empty Dictionary
print(d)
car = {'Make':'BMW','Model':'550I','Year':2018}  # Creating Dictionary with Key:Values
print(car)
print(car['Make'])
model = car['Model']
print(model)
d['one'] = 1  # Creating dictionary with values
d['two'] = 2
print(d)
sum_1 = d['two'] + 10
print(sum_1)
print(d)
d['two'] = d['two'] + 12  # Updating Dictionary Key Values data while performing operations
print(d)
print("******************NESTED DICTIONARY EXAMPLES***************************")
""" Nested Dictionary 
d = {'K1':{'nestkey1':'nestvalue1','nestkey2':'nestvalue2'}}
d[K1][nestkey1]"""
cars = {'BMW': {'MODEL': '550I', 'YEAR': 2016}, 'BENZ': {'MODEL': 'E50', 'YEAR': 2006}}
car_year = cars['BMW']['YEAR']
print(car_year)
print(cars['BENZ']['MODEL'])
print("****************  DICTIONARY METHODS EXAMPLES  *****************")
""" Running different methods on dictionary"""
car = {'Make': 'BMW', 'Model': '550I', 'Year': 2018}
cars = {'BMW': {'MODEL': '550I', 'YEAR': 2016}, 'BENZ': {'MODEL': 'E50', 'YEAR': 2006}}
print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())
print(cars.items())
print(car.pop('Year'))
print(car)
car_copy = car.copy()
print(car_copy)
print(len(cars))
