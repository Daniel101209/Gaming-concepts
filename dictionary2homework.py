textbook_prices = {
    "Math": 250,
    "Physics": 220,
    "Chemistry": 280,
    "Biology": 260
}

textbook_prices["Physics"] = 200

textbook_prices["Computer Science"] = 250
textbook_prices["History"] = 230

book_name = input("Enter the name of the book: ")
if book_name in textbook_prices:
    print(f"The cost of {book_name} is {textbook_prices[book_name]}")
else:
    print("Book not found in the inventory.")

print("\nList of all textbooks and their costs:")
for book, price in textbook_prices.items():
    print(f"{book}: ${price}")