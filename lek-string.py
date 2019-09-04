firstName = "Patrick"
middleName = "James"
lastName = "Dougherty"

nickName = "Pebble"


# för.efternamn
# patrick.dougherty
# firstName[3].lastName[3]

# print(f"{firstName[0:3].lower()}{(lastName[0:3].lower()}"19")
# userName = "firstName[0:3].lower()lastName[0:3].lower()19"
userName = firstName[0:3].lower()
userName += lastName[0:3].lower()
userName += "19"

print(userName)

# bygg en skolmail sträng firstName.lastName@elev.ga.ntig.se
domän = "ntig"

skolmail = firstName.lower()
skolmail += middleName.lower()
skolmail += "."
skolmail += lastName.lower()
skolmail += "@elev.ga."
skolmail += domän.lower()
skolmail += ".se"

print(skolmail)












print(firstName.upper())
print(middleName.lower())
print(lastName.strip())






















tecken = """() paranteser
[] hakparanteser 
{} måsvingar
: kolon
; semikolon
, komma
\" dubbelfnutt 
\' enkelfnutt"""

print(tecken[13:37])