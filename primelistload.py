import csv
with open('prime.csv', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)
f.close()