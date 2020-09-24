for i in range(3,7):
    for j in range(3,7):
        if j*i//10 + j*i%10 == 6:
            print(':=)', end=' ')
        else:
            print(j*i, end=' ')
    print()
