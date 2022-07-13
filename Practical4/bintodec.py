bin = int(input("Enter the Binary Number: "))
deci = 0
i = 1
while bin!=0:
    rem = bin%10
    deci = deci + (rem*i)
    i = i*2
    bin = int(bin/10)

print("\nEquivalent Decimal Value =", deci)