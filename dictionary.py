myself={
    "name":"Daniel",
    "age":15,
    "city":"Plovdiv",
    "Country":"Bulgaria"
}

print(myself)

print(myself["city"])

print(myself.keys())

print(myself.values())

for i in myself.keys():
    print(i,myself[i])

if "Country" in myself:
    print(myself["Country"])
else:
    print("Key doesn't exist")

myself["fav color"]="yellow"
myself["hobby"]="astronomy"
print(myself)

del(myself["city"])
print(myself)

myself["fav color"]="cyan"
print(myself)