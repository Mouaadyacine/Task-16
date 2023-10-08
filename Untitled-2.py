a=input("entrer le 1er coefficient")
b=input("entrer le 2eme coefficient")
c=input("entrer le 3eme coefficient")
D=b**2-4*a*c
if D<0:
    print("lequation na pas de solution")
elif D==0:
    print("le solution:",-b/2*a)
else:
    print("x1=",-b-sqrt(D)/2*a,"and x2=",-b+sqrt(D)/2*a)