#count the occurence of vovels in a sentence entered by the user
sentence=input("Enter a sentence: ")
vovels = {
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}

for i in sentence:
    if i in vovels:
        vovels[i]+=1
print(vovels)

#count the occurence for each alphabet in the string entered by the user

sentence=input("Enter the sentence: ")
charcount={}
for j in sentence:
    if j.isalpha():
        if j in charcount:
            charcount [j] +=1
        else:
            charcount[j]=1
for i in charcount.keys():
    print(i,charcount[i])

#pangram or not
number=input("Enter a number: ")
count= {
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0,
    "0":0
}
for i in number:
    if i in count:
        count[i] +=1
pangram=True
for j in count.values():
    if j ==0:
        pangram=False
    
if pangram:
    print("Entered number is a pangram")
else:
    print("Entered number is not a pangram")