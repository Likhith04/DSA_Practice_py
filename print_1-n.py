
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n)

def print_n_to_1(n):
    if n == 0:
        return 
    print(n)
    print_n_to_1(n-1)

number = int(input("Enter a Number : "))
print_1_to_n(number)

print_n_to_1(number)