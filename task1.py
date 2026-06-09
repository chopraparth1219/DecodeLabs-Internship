import csv
data = [
    ['Name', 'Year', 'Selling Price', 'KM Driven'],
    ['Maruti 800 AC', 2007, 60000, 70000],
    ['Tata Indigo Grand Petrol', 2014, 240000, 60000],
    ['BMW 3 Series 320 Sport Line', 2013, 1550000, 75800],
    ['Mahindra Scorpio', 2014, 1050000, 50000],
    ['Tata Indigo CR4', 2011, 150000, 155500]
]

with open('data_collection.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("Data loading is successful")

with open('data_collection.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    r = list(reader)

headers = r[0]
rows = r[1:]
l=len(headers)

for i in range(l):
    print("The columns are:", headers[i])
    print("The data type is:", type(data[1][i]))
    i=i+1

l1=len(rows)
print("size of the file is:", l1,"*", l)




