def triangle(a,b,c):
    if a == b and b == c and c == a:
        print("Il est possible de construire un triangle")
        print("Ce triangle sera équilatéral")
    elif a + b > c and a + c > b and b + c > a:
        print("Il est possible de construire un triangle")

    if (a==b or b==c or c==a) and (a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b):
        print("ce triangle est rectangle et isocèle")
    elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
        print("ce triangle est rectangle")
    elif a==b or b==c or c==a:
        print("ce triangle est isocèle")
    else :
        print("ce triangle est quelconque")
