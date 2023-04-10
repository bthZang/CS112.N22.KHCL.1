from src.checkPrime import checkPrime

def printPrime(n: int):
    print("So nguyen to tu 2 den", n, "la: ")
    for i in range(2, n + 1):
        if(checkPrime(i)):
            print(i)
    
    