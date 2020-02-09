#! python3
import math, csv, time

print('Prime Number Generator')
#validate input is an integer a number
while True:    
    try:
        num = int(input('Enter a positive integer: '))
        if num <= 0:
            print('That is not a positive integer, please input a positive integer')
            continue
        break
    except ValueError:
        print('This is not a valid input.  Please enter a positive integer')
#validate input is an integer and a number
while True:
    try:
        usin = int(input('How many odd numbers forward would you like to try? '))
        if usin <= 0:
            print("Please input a positive number")
            continue
        break
    except ValueError:
        print('This is not a valid input.  Please enter a positive integer')

nstart = num
primecount = 0
start_time = time.time()
count = 1
plist = []
# the next two if statements are to solve the #2 being a bring number issue
print('Prime Numbers: ')
if num == 1:
    plist.append(1)
    plist.append(2)
    num += 2
    primecount += 2
    count += 2
if num == 2:
    plist.append(2)
    num += 1
    primecount += 1
    count += 1
if num % 2 == 0:
            print('Number is even and therefore not a prime number, starting at next odd number', num + 1)
            num = num + 1

def primeTest (num)
    global primecount
    while True:
        n = 3
        notPrime = False
        while n <= math.sqrt(num): # Started with just '<' which gave 25 as a prime number because sqrt(25)=5 which it then didn't test.  I wonder if any other number would have caused this?
            p = num % n
            # tnum = int(str(num)[1:])# converts to string and slices the first digit to check if it is 5 to skip all odd numbers that end in 5 for speed
            # if num != 5 and tnum == 5:
            #     notPrime = True
            #     break
            #print('remainder',p,'Divided', n , 'Number', num) This tests to see if the number is divisible by the factor 'n'
            if p == 0:
                #print('not prime:', num, 'Tested', n, 'Factor', num/n ) # This displays the the number, and the two factors when they are found.
                notPrime = True
                break
            elif p != 0:
                n = n + 2
                continue
        if notPrime == True:
            break
        prime = num
        plist.append(prime)
        primecount += 1
        #outfile.write(wr)
        #print ('Time to find prime: ', end_time-start_time )
        break
while count < usin:
    primeTest(num)
    num += 2
    count += 1
print(plist)
try:
    percentPrime = (primecount/(num-nstart))*100 # calculates the number of prime numbers found by the last number tested
except:
    percentPrime = 0
end_time = time.time()
print('Report: ')
print('Total Prime Numbers: ', primecount, ' Percent prime: ', round(percentPrime, 2), '%')
primetime = (end_time - start_time)
print('Total time taken: ', primetime, 'Prime/Second', primecount/primetime)


with open('prime.csv', 'w', newline='') as myfile:
      wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
      wr.writerow(plist)