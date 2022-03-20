import random
mylist = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(mylist)
random_number = mylist.pop()

while True:
    if random_number == 1:
        #1
        print("The number which is neither a prime number nor a composite number?")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")
        #2
        print("The number which has only one factor?")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")

        #3
        print("It is the first number in natural number")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! You loss")
            break

    elif random_number == 2:
        #1
        print("It is the smallest prime number")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")
        #2
        print("It is the only even prime number")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")

        #3
        print("It is the only number whose factorial is prime")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! You loss")
            break
    elif random_number == 3:
        #1
        print("It is the greatest number of consecutive integers that can be pair wise relatively prime")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")
        #2
        print("It is the only prime followed by a square")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")

        #3
        print("It is the only triangular number that is also prime")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! You loss")
            break
    elif random_number == 4:
        #1
        print("It is the only compositorial square")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")
        #2
        print("It is the only positive number that is both the sum and the product of the same two integers")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")

        #3
        print("It is the order of the smallest non-cyclic group")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! You loss")
            break
    elif random_number == 5:
        #1
        print("It is the smallest number of queens needed to attack every square on a standard chess board")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")
        #2
        print("It is the only prime which is the difference of two squares of primes")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")

        #3
        print("It is the only prime that is a member of 2 pairs of twin primes")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! You loss")
            break
    elif random_number == 6:
        #1
        print("It is the only even evil perfect number")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")
        #2
        print("It is the smallest perfect number")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")

        #3
        print("It is the only square-free perfect number")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! You loss")
            break
    elif random_number == 7:
        #1
        print("It is the smallest number that cannot be represented as a sum of 3 squares")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")
        #2
        print("It is the smallest integer that is not the difference of two primes")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")

        #3
        print("It is the only prime followed by a cube")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! You loss")
            break
    elif random_number == 8:
        #1
        print("It is the only composite cube in the Fibonacci sequence")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")
        #2
        print("It is the dimension of the octonions and is the highest possible dimension of a normed division algebra")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")

        #3
        print("It is the smallest number (except 1) which is equal to the sum of the digits of its cube")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! You loss")
            break
    elif random_number == 9:
        #1
        print("It is the smallest odd composite number")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")
        #2
        print("It is the maximum number of cubes that are needed to sum to any positive integer")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")

        #3
        print("It is the only non-trivial square consisting of only odd digits")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! You loss")
            break
    elif random_number == 10:
        #1
        print("It is the base of our number system")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")
        #2
        print("It is the only semi-prime number with the property that the sum as well as the difference of its prime divisors are primes (2 + 5 = 7 and 5 - 2 = 3)")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! Try again")

        #3
        print("It is the smallest no quotient, a number that can not be expressed as the difference between any integer and the total of coprimes below it")
        n = int(input("Enter You Guess:"))
        if n == random_number:
            print("Correct")
            break
        else:
            print("Wrong!! You loss")
            break