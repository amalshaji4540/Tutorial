import csv
# with open('items.csv','r') as file:
#     reader=csv.reader(file)
#     print(reader)
#     for item in reader:
#         print(item)

# with open('items.csv','r') as file:
#     reader=csv.DictReader(file)
#     print(reader)        
#     for item in reader:
#         print(item)
    
with open('items.csv','r') as file:
    reader=csv.DictReader(file)
    items=list(reader)
    for item in items:
        print(item.get("Name"))
        print(item.get("price"))
        print(item.get("quantity"))