import datetime

print("Vypisuji součty cifer v datu pro následujících 7 dní:")
today = datetime.date.today()
for i in range(7):
    print(str(today) + " - " + str(today.year+today.month+today.day))
    today += datetime.timedelta(1)
