import csv
import matplotlib.pyplot as plt

with open('cleaned_data.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

headers = data[0]
rows = data[1:] 

carnames = []
years = []
prices = []
kms = []

for row in rows:
    carnames.append(row[0])        
    years.append(int(row[1]))         
    prices.append(int(row[2]))        
    kms.append(int(row[3]))
    
plt.figure(figsize=(10, 5))                       
plt.bar(carnames, prices, color='skyblue')       
plt.xlabel('Car Model')                           
plt.ylabel('Selling Price (₹)')                   
plt.title('Selling Price of Different Cars')      
plt.xticks(rotation=45, ha='right')             
plt.tight_layout()                                
plt.savefig('bar_chart.png')                    
plt.show()              

plt.figure(figsize=(8, 5))                        
plt.hist(prices, bins=5, color='orange', edgecolor='black') 
plt.xlabel('Price Range (₹)')                     
plt.ylabel('Number of Cars')
plt.title('Distribution of Selling Prices')
plt.savefig('histogram.png')
plt.show()

brand_counts = {}
for name in carnames:
    if  name.strip() == "":          
        continue
    else:
        brand = name.split()[0]
        brand_counts[brand] = brand_counts.get(brand, 0) + 1

print("Brand counts:", brand_counts)              
plt.figure(figsize=(6, 6))
plt.pie(brand_counts.values(),
        labels=brand_counts.keys(),
        autopct='%1.1f%%',
        startangle=90)                      
plt.title('Market Share by Brand')
plt.savefig('pie_chart.png')
plt.show()
