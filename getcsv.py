#! python3
import numpy as np, csv

myData = np.genfromtxt('prime.csv', delimiter=',', encoding='utf8')
print(myData)