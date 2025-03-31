import random
from operator import truediv

# Tworzenie talii kart (52 karty)
kolory = ['♠', '♥', '♦', '♣']
wartosci = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
talia = [f'{wartosc}{kolor}' for kolor in kolory for wartosc in wartosci]


#gracze

g = int(input("Ilu jest graczy (wybierz od 3 do 6)?: "))

while True:
  print("Podałeś nieprawidłową ilość graczy! ")
  print("Spróbuj ponownie: ")
  if g<3 or g>6:
    break
g = int(input("Ilu jest graczy (wybierz od 3 do 6)?: "))
k=1
while g >=3 and g<=6 and k<=g:
  print(f"Podaj imię {k} gracza ")
  gracz = input()

# Losowanie kart graczy
  ilosc_kart = 2
  wylosowane_karty = random.sample(talia, ilosc_kart)
  print("Wylosowane karty :", wylosowane_karty)

  k +=1
# Losowanie kart na stole
ilosc_kart = 3
wylosowane_karty_3 = random.sample(talia, ilosc_kart)
print("Wylosowane karty na stole :", wylosowane_karty_3)

print ("Czy wyłożyć 4 kartę(Jeżeli jesteś gotowy wciśnij Enter )? ")
tak = True

input()
if tak:

  ilosc_kart = 1
  wylosowana_karta_4 = random.sample(talia, ilosc_kart)
  print("Wylosowana karta 4 na stole to :", wylosowana_karta_4)
  print("Wylosowane karty na stole :", wylosowane_karty_3, wylosowana_karta_4)

print ("Czy wyłożyć 5 kartę(Jeżeli jesteś gotowy wciśnij Enter )? ")

input()
if tak:
  ilosc_kart = 1
  wylosowana_karta_5 = random.sample(talia, ilosc_kart)
  print("Wylosowana karta 5 na stole to :", wylosowana_karta_5)
  print("Wylosowane karty na stole :", wylosowane_karty_3, wylosowana_karta_4, wylosowana_karta_5 )