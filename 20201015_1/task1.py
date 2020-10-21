a = input().lower()
print(len({a[i:i+2] for i in range(len(a)-1) if a[i:i+2].isalpha()}))