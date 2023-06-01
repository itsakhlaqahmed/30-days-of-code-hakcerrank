# task 01
# print table

n = int(input().strip())

for i in range(1,11):
    print(f'{n} x {i} = {n*i}');


# task 03
# even and odd

s = input();

even = ''
odd = ''

for i, l in enumerate(s):
    if (i%2):
        odd += l
    else:
        even += l
        
print(even,' ',odd);



# task 03 
# reverse array
n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
arr.reverse();
for i in arr:
    print(i, end=' ')
