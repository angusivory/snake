#test

listb = [50, 49, 38, 13, 34,  56, 50, 109,  50, 49, 34,34, 12, 13, 67, 34]

x1 = 50
y1 = 49

print(listb.count(x1))
for x in range(0, len(listb), 2):
    if listb[x] == x1:
        if listb[x + 1] == y1:
            print("problem")