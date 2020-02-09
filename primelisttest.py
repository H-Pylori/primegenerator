#! python3
import math, csv, time, numpy as np


print('Prime Number Generator')
#validate input is an integer a number
# while True:    
#     try:
#         num = int(input('Enter a positive integer: '))
#         if num <= 0:
#             print('That is not a positive integer, please input a positive integer')
#             continue
#         break
#     except ValueError:
#         print('This is not a valid input.  Please enter a positive integer')
# #validate input is an integer and a number
while True:
    try:
        usin = int(input('How many prime numbers forward would you like to output? '))
        if usin <= 0:
            print("Please input a positive number")
            continue
        break
    except ValueError:
        print('This is not a valid input.  Please enter a positive integer')
start_time = time.time()
num = 3
nstart = num
primecount = 0
count = 0
plist = [1, 2]
print("List of Primes Found: ")
def primeTest (num):
    global primecount
    while True:
        #isPrime = None
        remainders = []
        while True: 
            divideList = np.array(plist) # Converts plist into a NumPy
            sqrtDivide = divideList[divideList[:] <= np.sqrt(num)] #this shortens the testing list to a range from 2 to the sqrt of num to minimize the division
            remainders = num % sqrtDivide[3:]
            rtest = 0 in remainders #this tests the remainders list for a division with a remainder of 0 meaning it has a factor
        
            if rtest == True: #if the above remainder test finds a factor 
                break
            elif rtest == False:
                prime = num
                plist.append(prime)
                primecount += 1
                print(primecount, end="\r")
                break
        break
        #outfile.write(wr)
        #print ('Time to find prime: ', end_time-start_time )
while count < usin:
    primeTest(num)
    num += 2
    count += 1
end_time = time.time()
print(plist)
try:
    percentPrime = (primecount/(num-nstart))*100 # calculates the number of prime numbers found by the last number tested
except:
    percentPrime = 0
print('Report: ')
print('Total Prime Numbers: ', primecount, ' Percent prime: ', round(percentPrime, 2), '%')
primetime = (end_time - start_time)
report = 'Total time taken: ', primetime, 'Prime/Second', primecount/primetime, 'Final Number Tested', num
print('Total time taken: ', primetime, 'Prime/Second', primecount/primetime, 'Final Number Tested', num)


with open('prime.csv', 'w', newline='') as outFile:
      wr = csv.writer(outFile, delimiter=',')
      #wr.writerow(report)
      wr.writerow(plist)  
outFile.close()