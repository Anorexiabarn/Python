#print("välkommen till min miniräknare som kan addera")
#tal1 = int(input("tal 1: "))
#tal2 = int(input("tal 2: "))
#summa = int(tal1 + tal2)

#print("summan: " + str(summa))




#räknesätt = input('välj räknesättet ("+ - * / ")') 
#tal1 = int(input("tal 1: "))
#tal2 = int(input("tal 2: "))
#if räknesätt == "*":
#    summa = str(tal1 * tal2)
#    print("summa: " + summa)

#elif räknesätt == "-":
#    summa = str(tal1 - tal2)
#    print("summa: " + summa)

#elif räknesätt == "+":
#    summa = str(tal1 + tal2)
#    print("summa: " + summa)

#elif räknesätt == "/":
#    summa = str(tal1 / tal2)
#    print("summa: " + summa)




print("välkommen till mitt program där du kan addera")
operator = input("välj räknesätt(+, -, *, /): ")
try:
    Num1 = int(input("skriv in ett heltal: "))
except:
    print("du måste skriva ett heltal")
    Num1 = 0
try:
    Num2 = int(input("du måste skriva ett till heltal: "))
except:
    print("du måste skriva in en siffra")
    Num2 = 0 

if operator == "+":
    Total = str(Num1 + Num2)
    print("summan är: " + Total)
elif operator == "-":
    Total = str(Num1 - Num2)
    print("summan är: " + Total)

elif operator == "*":
    Total = str(Num1 * Num2)
    print("summan är: " + Total)

elif operator == "/":
    try:
        Total = str(Num1 / Num2)
    except( ZeroDivisionError):
        print("Det går inte att dela med 0")
        Total = ('error')
    print("summan är: " + Total)


else:
    print("Fel")

