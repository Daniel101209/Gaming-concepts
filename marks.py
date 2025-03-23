from random import randint
bad = []
medium = []
good = []

for i in range (20):
    mark = randint(0,100)
    if (mark <= 30):
        bad.append(mark)
    elif ((mark > 30) and (mark <= 69)):
        medium.append(mark)
    else:
        good.append(mark)
print("All marks under 30: ",bad)
print("All marks between 30 and 69: ",medium)
print("All marks above 69: ",good)