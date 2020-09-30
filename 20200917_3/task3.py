i = 2
while (i:= i+1) <= 6:
    j = 2
    while (j:= j+1) <= 6:
        if j*i//10 + j*i%10 == 6:
            print(':=)', end=' ')
        else:
            print(j*i, end=' ')
    print()
