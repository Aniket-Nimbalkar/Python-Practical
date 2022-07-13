# Finding roots of Quadratic Equation
a = float(input("Enter value of a:- "))
b = float(input("Enter value of b:- "))
c = float(input("Enter value of c:- "))
delta = (b*b - 4*a*c) ** 0.5
root1 = (- b + delta) / 2*a
root2 = (- b - delta) / 2*a
print("Roots of given quadratic equation are", root1, "and", root2)
