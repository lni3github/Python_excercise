myInput = int(input("Enter your number: "))

def isPrime(number):
    if (number == 0 or number == 1):
        return "not prime number"
    else:
        for i in range(2, number):
            if number % i == 0 and i != number:
                return "not prime number"
        return "prime number"
    
print(isPrime(myInput))
    