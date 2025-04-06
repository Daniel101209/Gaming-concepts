#Creating a taple
myself = ('Daniel',15,'yellow','Astronomy')

#create a tuple as adress info
adress=("154","Bul. Maritsa","Plovdiv","Plovdiv region","4000")

#Printing the taple elements till the end
for x in adress:
    print(x,end=" \n")

#Naming the taple elements
houseno, street, city, region, pincode = adress

#Printing one element from the taple
print()
print('House number =',houseno)

#Creating a taple
fruits =('Apple','Banana','Pear','Orange','Pineapple','Grapes','Watermelon','Avocado','Grapefruit','Pomelo','Dragon fruit','Litchi','Jack fruit','Star fruit','Blueberry','Strawberry','Raspberry')

#Naming the taple elements
fruit1, fruit2, fruit3, fruit4, fruit5, fruit6, fruit7, fruit8, fruit9, fruit10, fruit11, fruit12, fruit13, fruit14, fruit15, fruit16, fruit17 = fruits

#Printing certain elements from the taple
print('My favorite fruits from this list are: ',fruit1,fruit2,fruit5,fruit6,fruit11,fruit12,)

#Empty lists/dictionaries

empty1 = []
empty2 = {}

print('empty',empty1,'dictionary')
print('empty',empty2,'list')

my_tuple=1,25,"Biology"
print(my_tuple)

n_tuple=("cat",[2,4,6],[1,3,5])
print(n_tuple[0][1])
print(n_tuple[2][1])

m=('d','a','n','i','e','l')
print(m[1:4])
print(m[:-4])
print(m[4:])