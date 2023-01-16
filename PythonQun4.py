num = int(input("Entre a number to divide:"))
range = list(range(1,num+1))
List = []

for number in range:
    if num % number == 0:
        List.append(number)
print(List)