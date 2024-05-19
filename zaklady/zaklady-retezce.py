vstup = " C++ je [kolikrat] KRÁT lepší! "
vystup = vstup.strip().lower().replace("c++", "Python")
print(vystup)
print(vystup.startswith("Python"))
print("krát" in vystup)
print(vystup.replace("[kolikrat]", str(3 * len(vystup))))