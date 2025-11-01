print("Benvenuto nel mercato di zio Zé!")
print("Il salame e il pane oggi sono in offerta: pane a 4.50€/kg e salame a 32€/kg")

prezzi = {"pane": 4.50, "salame": 32}

prodotto = input("Cosa vorresti comprare al mercato di zio Zé, pane o salame? ").strip().lower()
if prodotto not in prezzi:
    print("Non abbiamo questo prodotto nel nostro mercato!")
    exit()

try:
    peso = float(input("Quanto ne vuoi acquistare? "))
except ValueError:
    print("Errore: quantità non valida! Inserisci un numero (es: 1.5 o 2)")
    exit()

unità = input("Hg oppure Kg? ").strip().lower()
if unità not in ("hg", "kg"):
    print("Errore: peso non valido! Devi inserire (Hg) o (Kg).")
    exit()

# Conversione in kg se necessario
if unità == "hg":
    peso *= 0.1

prezzo_totale = peso * prezzi[prodotto]
print(f"Il prezzo totale è: {prezzo_totale:.2f}€")
