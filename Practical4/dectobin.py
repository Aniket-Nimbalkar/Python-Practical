deci = int(input("Enter Decimal Number: "))
bin = 0
mul = 1
while deci > 0:
    rem = deci % 2
    bin = bin + (rem * mul)
    mul = mul * 10
    deci = int(deci / 2)

print("\nEquivalent Binary Value =", bin)