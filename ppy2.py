#zad1
# name = input("Podaj imie: ")
# birthday = input("Podaj date ur: ")
# email = input("Podaj email: ")
# tel = input("Podaj tel: ")
#
# l=[name,birthday,email,tel]
# t=(name,birthday,email,tel)
# d={"name":name,"birth":birthday,"email":email,"tel":tel}
#
# print(l) #list
# print(t) #tuple
# print(d) #dictionary

#zad2
liczby = []
print("Podaj 20 liczb z zakresu od -20 do 20:")

while len(liczby) < 20:
    try:
        liczba = int(input(f"Liczba {len(liczby)+1}: "))
        if -20 <= liczba <= 20:
            liczby.append(liczba)
        else:
            print("Liczba musi byc od -20 do 20. Sprobuj ponownie.")
    except ValueError:
        print("To nie jest poprawna liczba. Sprobuj ponownie.")

print("\nTwoje liczby to:")
print(liczby)

liczbyCopy = liczby.copy()






