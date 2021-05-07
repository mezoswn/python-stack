import random
def randInt(nummin=0, nummax=100):
    num = nummax - nummin    #This will make our staring point 50 for example if our min number is set to 50.
    return round(random.random() * num + nummin)    # We add our min number here because above we subtracted it from the max, Here we can put the range correctly between the true max and starting at the true min.
print(randInt())    # should print a random integer between 0 to 100
print(randInt(nummax=50))    # should print a random integer between 0 to 50
print(randInt(nummin=50))    # should print a random integer between 50 to 100
print(randInt(nummin=50, nummax=500))    # should print a random integer between 50 and 500

