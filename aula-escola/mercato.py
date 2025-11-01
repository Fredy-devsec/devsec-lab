print("benvenuto nel mercato di zio zé")
print("Il salame e il pane oggi sono in offerta: pane a 4.50€/kg e salame a 32€/kg")
prodotto = (input("Cosa vorresti comprare al mercato di zio zé, pane o salame? ").strip().lower())
if prodotto != "salame" and prodotto != "pane":
    print("Non abbiamo questo prodotto nel nostro mercato!")
else:
    try:
        peso = float(input("Quanto ne vuoi acquistare? "))
    except ValueError: 
        print("Errore: quantita non valido! Devi inserire una quantita valida! es: ( 1.50 ) o ( 2 ) ")
        exit()
Hg_Kg = input("Hg oppure kg?").strip().lower()
if Hg_Kg != "hg" and Hg_Kg != "kg":
    print("Errore: peso non valido! Devi inserire un peso valido! (Hg) o (Kg).")
    exit()
if prodotto == "salame" and Hg_Kg == "hg":
    prezzo = peso * 0.1 * 32
    print(f"Il prezzo totale é: {prezzo}€")
elif prodotto == "salame" and Hg_Kg == "kg":
    prezzo = peso * 32
    print(f"Il prezzo totale é: {prezzo}€")
if prodotto == "pane" and Hg_Kg == "hg":
    prezzo = peso * 0.1 * 4.50
    print(f"Il prezzo totale é: {prezzo}€")
elif prodotto == "pane" and Hg_Kg == "kg":
    prezzo = peso * 4.50
    print(f"Il prezzo totale é: {prezzo}€")