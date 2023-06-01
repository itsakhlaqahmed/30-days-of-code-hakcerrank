# day 08
# dictionaries 

phonebook = dict()
n = int(input())
for _ in range(n):
    name, num = input().split()
    phonebook[name] = num

# a = input()
for _ in range(n):
    a = input()
    if a in phonebook.keys():
        print(a + '=' + phonebook[a])
    else:
        print('Not found')