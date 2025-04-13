group_records = []

for i in range(5):
    print(f"\nEnter the details of the group {i + 1}:")
    name = input("Enter the group Name: ")
    size = int(input("Enter the size of the Group: "))
    date = input("Enter the date of competition: ")
    venue = input("Enter the venue: ")
    medal = input("Enter the type of medal (gold/silver/bronze/none): ")

    record = (name, size, date, venue, medal)
    group_records.append(record)

print("\nAll Group Competition Records:")
for i, record in enumerate(group_records, start=1):
    print(f"Group {i}: {record}")
