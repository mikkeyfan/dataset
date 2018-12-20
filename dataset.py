import csv
dataset = {}

#Программа создаёт словарь формата (Говорд: рестораны в нём: средняя цена в каждом ресторане)
#


def add(city, restaurant, voice):
    if city in dataset:
        dataset[city][restaurant] = voice
    else:
        dataset[city] = {restaurant: voice}


with open("C:\Dekstop_new\zomato.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, quotechar='|')
    next(reader, None)
    for row in reader:
        try:
            add(row[3], row[1], row[-11])
        except IndexError:
            print("Data for restaurant " + row[0] + " is incomplete!")
            continue

print(dataset)

list_price = []

for citys in dataset:
    for restiks in dataset[citys].keys():
        list_price.append(dataset[citys][restiks])



list_price.sort()

list_price = list_price[:20]
print(list_price)


for i in list_price:
    for city in dataset:
        for restos in dataset[city]:
            if i in dataset[city][restos]:
                print(restos)
