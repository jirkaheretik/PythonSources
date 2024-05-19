def smajlik():
    smajlik = input("Zadej smajlíka: \n")
    if smajlik[0] == ":":
        znak = smajlik[1]
        if znak == "-":
            znak = smajlik[2]
        if znak == ")":
            print("Tvůj smajlík je veselý")
        elif znak == "(":
            print("Tvůj smajlík je smutný")
        elif znak == "*":
            print("Tvůj smajlík je zamilovaný")
        elif znak == "P":
            print("Tvůj smajlík je s vyplazeným jazykem")
        else:
            print("Tvůj smajlík je neznámý")
    else:
        print("Tvůj smajlík je neznámý")

def maly_test_pandas():
    extrima_df = object()
    odpovidajici_extrem = extrima_df.loc[(extrima_df["Datetime"] > row[datetime_column]) & (
            extrima_df["Předchozí Datetime"] <= row[datetime_column]), "Value"].iloc[0]

def smajlik_test():
    print("Tvůj smajlík je " + ("veselý" if (z := input("Zadej smajlíka:\n").upper()[-1]) == ")" else "smutný" if z == "(" else "zamilovaný" if z == "*" else "s vyplazeným jazykem" if z == "P" else "neznámý"))

if __name__ == '__main__':
    smajlik_test()