# input 2 numbers

start = int(input("input start number : "))
end = int(input("input end number : "))

if end < start:
    start, end = end, start

for i in range(start, end + 1):
    if i <= 1:
        continue
    for k in range(2, i):
        if i % k == 0:
            break
    else:
        print(i, end = ' ')
