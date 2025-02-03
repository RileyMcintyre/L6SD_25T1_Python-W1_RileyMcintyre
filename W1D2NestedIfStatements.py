# input number to be checked
while  True :
    value = float(input("number   "))

# check if the number is negitive, positive or zero
    if (value) < 0:
        print ("negitive")
        answer = input("more Yes/No  ")
        if (answer) == ("Yes"):
            continue
        else:
            break
    elif (value) > 0:
        print ("positive")
        answer = input("more Yes/No  ")
        if (answer) == ("Yes"):
            continue
        else:
            break
    else:
        print ("zero")
        answer = input("more Yes/No   ")
        if (answer) == ("Yes"):
            continue
        else:
            break
