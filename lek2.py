# variabler för att komma ihåg namn och ålder
restriction = "hellow"
minimum = 18
# läsa in namn
firstName = input("Skriv in ditt förstanamn: ")
lastName = input("skriv in ditt efternamn: ")
# läsa in ålder
age = int(input("Hur gammal är du: "))

if age < minimum:
    restriction = "later kiddo"
# skriva ut hej namn och du är x gammal
print("tjenixen", firstName, lastName, restriction)
print("du är ", age, "gammal")
# skriva ut om du är 18 eller inte


