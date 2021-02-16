#!/usr/bin/env python3.7
if True:
	print("was True")

name = "Ash"
if len(name) >= 6:
	print("name is long")
elif len(name) == 5:
	print("name is 5 characters")
elif len(name) >= 4:
	print("name is 4 or more")
else:
	print("name is short")


name1=""
not name1
if not name1:
	print("name not given")


# OR Operation
first=""
last="Mannem"
if first or last:
	print(f"The user has first or last name {first} {last}")

orvar=""
orvar_val=orvar or "Doe"
print(orvar_val)

print(0 or 1)
print(1 or 2)

# AND operation
firstn="Ashok"
lastn="Mannem"
if firstn or lastn:
	print(f"Full name: {firstn} {lastn}")
elif firstn:
	print(f"First name: {firstn}")
elif lastn:
	print(f"Last name: {lastn}")


print(0 and 1)
print(1 and 2)
print((1==1) and print("something"))
print((1==2) and print("something"))

# while loop
count=1
while count <= 4:
	print("while loop")
	count+=1


count1=0
while count1<10:
	if count1%2 == 0:
		count1+=1
		continue
	print(f"we're counting odd numbers: {count1}")
	count1+=1


count2=1
while count2<10:
        if count2%2 == 0:
                count2+=1
                break
        print(f"we're counting odd numbers: {count2}")
        count2+=1

# for loop
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
	print(color)

colors1 = ['blue', 'green', 'red', 'purple']
for col in colors1:
	if col == 'blue':
		continue
	elif col == 'red':
		break
	print(col)

point = (2.1, 3.4, 5.6)
for value1 in point:
	print(value1)

ages = {"Ashok": 27, "Swathi": 23}
for key in ages:
	print(key)
	print(ages[key])

for letter in "my_string":
	print(letter)

list_of_points = [(1,2), (2,3), (4,5)]
for x,y in list_of_points:
	print(f"x: {x}, y: {y}")

ages_d = {"Ashok": 27, "Swathi": 23, "Kishore": 26}
for name, age in ages_d.items():
	print(f"Person Named: {name}")
	print(f"Age of: {age}")
