b = 0
while (a := int(input())) > 0 :
    b += a
    if (b>21) :
        break
else:
    b = a;
print(b)
