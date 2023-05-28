# if n is odd or if n is even but in range 6 to 20 then its weird else its not


def isWeird(n):
    
    isOdd = n%2
    
    if isOdd:
        print("Weird")
    elif not isOdd and n in range (6,21):
        print("Weird")
    else:
        print("Not Weird")