for number in range(200, 20, -1):
    if (number/3 == number//3) or not(number/5 == number//5):
        continue
    print(number)
