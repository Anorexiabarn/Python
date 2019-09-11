import random  # laddar in random klassen så vi kan använda den

print("Rulla tärningen") # meddelande till användaren

# försök läsa in sides som en int, vid fel sätt sides till 1
try:
    sides = int(input("hur många sidor?"))
except:
    print ("Skriv in ett heltal")
    sides = 1

run = "y" # vi ger run värdet y som standerd

# så länge run == y kör loopen
while run.lower() == "y":
    x = randomNumber = random.randint(1, sides) # slumpa ett tal mellan 1 och slides
    print(x) # skriv ut

    # fråga om användaren vill forsätta rulla
    run = input("vill du rulla en gång till?[y/n]: ")