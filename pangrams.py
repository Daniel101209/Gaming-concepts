def pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
    letters_in_sentence = set(s.lower())
    
    return alphabet.issubset(letters_in_sentence)

user_input = input("Enter a sentence: ")

if pangram(user_input):
    print("This is a pangram.")
else:
    print("This is not a pangram.")
