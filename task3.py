import csv
import matplotlib.pyplot as plt

with open('cleaned_data.csv', 'r') as f:
    reader=csv.reader(f)
    data=list(reader)

headers = data[0]
rows = data[1:]

for row in rows:
    names=row[0]
    years=row[1]
    price=row[2]
    kms=row[3]

plt.bar(names, price, color='skyblue')
plt.xlabel('Car Model')
plt.ylabel('Selling Price (₹)')
plt.title('Selling Price of Different Cars')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('bar_chart.png')
plt.show()

plt.hist(price, bins=5, color='orange', edgecolor='black')
plt.xlabel('Price Range (₹)')
plt.ylabel('Number of Cars')
plt.title('Distribution of Selling Prices')
plt.savefig('histogram.png')
plt.show()

for name in names:
    brands = name.split()
    brand_counts = {}
    for b in brands:
        brand_counts[b] = brand_counts.get(b, 0) + 1

plt.figure(figsize=(6,6))
plt.pie(brand_counts.values(), labels=brand_counts.keys(), autopct='%1.1f%%', startangle=90)
plt.title('Market Share by Brand')
plt.savefig('pie_chart.png')
plt.show()
