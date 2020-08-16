from itertools import product

charset = "abcdefghijklmnopqrstuvwxyz0123456789"
maxrange = 5


def solve_password(password, maxrange):
    for i in range(maxrange+1):
        for attempt in product(charset, repeat=i):
            #Here do the Bruteforce
            #The attempt is converted to string
            stringAttempt = ''.join(attempt)
            #Uncomment to see all attemps
            #print(stringAttempt)
            if(stringAttempt == password):
                print("Success!!! Password is: "+stringAttempt)
                break
                

solved = solve_password('crack', maxrange)
