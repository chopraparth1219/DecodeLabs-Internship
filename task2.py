import csv

with open('data_collection.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data[0]
rows = data[1:]

for row in rows:
    row[1] = int(row[1])
    row[2] = int(row[2])
    row[3] = int(row[3])

print("Original rows:")
for row in rows:
    print(row)

missing = False
for row in rows:
    for val in row:
        if val == '':
            missing = True
            break
    if missing:
        break

if not missing:
    print("\nNo missing values found.")
else:
    print("\nMissing values found – will be handled.")
    for row in rows:
        for i in range(4):
            if row[i] == '':
                if i in [1,2,3]:
                    row[i] = 0
                else:
                    row[i] = 'Unknown'

rows1 = []
s = set()
duplicate_count = 0

for row in rows:
    row_name = row[0]
    clean_name = row_name.strip().lower()
    
    if clean_name not in s:
        s.add(clean_name)
        rows1.append(row)
        print("No duplicate found...")
    else:
        duplicate_count += 1
        print(f"DUPLICATE removed: {row_name}")

for row in rows1:
    row[0] = row[0].strip().title()

with open('cleaned_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows1)

print("\nCleaned data saved to 'cleaned_data.csv'")
print("\nCleaned rows:")
for row in rows1:
    print(row)
