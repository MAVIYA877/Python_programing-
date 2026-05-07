#if conditional 
age = 20
if age > 18:
    print("you are adult")


#if-else conditional 
age = 15 
if age > 18:
    print("you are adult")
else:
    print("you are minor")


#elif conditional
marks = 90
if marks > 80:
    print("excellent")
elif marks > 50:
    print("passed")
else:
    print("failed")


#nested-if 
temperature = 30
if temperature > 0:
    if temperature > 25:
        print("it is hot outside:")
    else:
        print("temperature is positive")
else:
        print("weather is normal")