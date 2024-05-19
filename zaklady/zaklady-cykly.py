#veta = input("Zavolej něco: ")
for _ in range(3):
    print(f"Jak je ti Rakousko?")

print()

for i in range(1, 11):
    print(i)

print()

for i in range(10, 0, -1):
    print(i)

print()

for r in range(8):
    for c in range(8):
        print("  " if (r + c) % 2 == 0 else "XX", end = "")


    print()

# echo ( ($r + $c) % 2 ? "<td class='black' />" : "<td class='white' />" );