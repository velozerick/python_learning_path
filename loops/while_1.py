 #syntax

'''
while condition:
    code goes here


count = 0

while count < 5:
    print (count)
    count = count + 1 #prints from 0 to 4 

print("First program end...")


# ELSE


while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

print("Second program end...")

#Brake

while count < 5:
    print(count)
    count = count + 1

    if count == 3:
        break
print("Third program end...")

'''
count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count = count + 1

print("Fourth program end...")
