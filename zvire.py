zvirata= []
pocet= int(input("kolik chcete zadat zviřat?"))

for i in range(pocet):
    zvire = input (f"zadejte zvire{i+1}:")
    zvirata.append(zvire)

if "tapír" in zvirata:
    print("super")
elif "mýval" in zvirata:
    print("super")
elif "kocka" in zvirata:
    print("super")
else:
    print("nic moc")
