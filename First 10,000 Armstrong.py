for no in range(1,10000):
    real = no
    real1 = no
    sum1 = 0
    count = 0
    while real1 > 0:
        real1 = real1 // 10
        count = count + 1

    while no > 0:
        rem = no % 10
        sum1 = sum1 + rem ** count
        no = no // 10

    if sum1 == real:
        print(real,"is Armstrong number")
    # else:
        # print(real,"is Not Armstrong number")