"""n = float(input("enter the money bob has:"))
c = float(input("enter the price of chocolate:"))
m = int(input("enter no of wrappers bob has:"))
chocolates = int(n // c)+m
print(f"Bob can eat {chocolates} chocolates.")"""
# 2 -------------------------------------------------------------------------------------
"""n = int(input("enter the line to be deleted:"))
try:
    with open("input1.txt", "r") as f:
        r = f.readlines()
except Exception as e:
    print(f"an error occured {e}")
else:
    if 0 < n <= len(r):
        r.pop(n-1)
        with open("input1.txt", "w") as f:
            f.writelines(r)
        for i in r:
            print(i, end='')
    else:
        print("Invalid line number.")"""
# -------------------------------------------------------------------------------------
"""queue = deque()
for i in range(5):
    n = int(input("Enter a number:"))
    queue.append(n)
for i in queue:
    print(i, end=' ')
print("\n")
for i in range(2):
    n = queue.popleft()
    queue.append(n)
for i in queue:
    print(i, end=' ')"""
# ----------------------------------------------------------------------------------------
"""n1 = input(
    "Enter the real and imaginary parts of the complex number format(real space imaginary): ")
n2 = input(
    "Enter the real and imaginary parts of the complex number format(real space imaginary): ")
a = n1.split()
b = n2.split()
c = complex(int(a[0])+int(b[0]), int(a[1])+int(b[1]))
print(f"The sum of the complex numbers is: {c}")"""
# --------------------------------------------------------------------------------------
