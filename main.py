# zepta se na jmeno a vek
jmeno= input("zadejte vase jmeno: ")
vek = input("zadejte svuj vek: ")

# vypis pomoci f-stringu
print(f"ahoj, jmenuji se {jmeno} a je mi {vek} let:")


# zepta se na dve desetina cisla
cislo1 = float(input("zadejte prvni desetinne cislo: "))
cislo2= float (input("zadejte druhe desetinne cislo: "))

#vypocty
soucet = cislo1 + cislo2
rozdil = cislo1 - cislo2
soucin = cislo1 * cislo2
if cislo2 != 0:
    podil = cislo1 / cislo2
else:
    podil = "neni mozne delit nulou"

#vypis vysledku s presnosti na dve desetina mista
print(f"soucet: {soucet:.2f}")
print(f"rozdil: {rozdil:.2f}")
print(f"soucin: {soucin:.2f}")
print(f"podil: {podil:.2f}" if isinstance(podil, float) else podil)
