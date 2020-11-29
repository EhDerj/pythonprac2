l = list(eval(input()))

# I use insertion sort
for i in range(1, len(l)):
    for j in reversed(range(i)):
        if (l[j] * l[j]) % 100 > (l[j+1] * l[j+1]) % 100:
            l[j], l[j+1] = l[j+1], l[j]
        else: break

print(l)
