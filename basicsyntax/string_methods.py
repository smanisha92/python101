first = "New"[0]
print(first)
city = "York"
ft = city[0]
print(ft)
print("**************")
sng = "This is A Mixed Case String"
print(sng)
print(sng.lower())
print(sng.upper())
print(len(sng))
print(sng + " " + str(2))
print("Hello" + " " + "World")
print(first + "" + city)
print("_____________________________")
# replace method
a = "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC', 1))
# sub strings
# starting index is inclusive, Ending Index is exclusive
stg = a[1]
print(stg)
st = a[1:8]
print(st)
step = a[1:8:3]
print(step)
srg = a[:]  # it uses complete string characters because no start and end point is provided
print(srg)
stn = a[1:]  # it skips the 0 position character and prints rest.
print(stn)
s = a[::-1]  # this is reverse string process
print(s)

a = "one two three"
print(a.split())
