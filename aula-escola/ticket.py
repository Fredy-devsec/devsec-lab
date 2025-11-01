print("Ciao, benvenuto alla stazione Alitalia.")
print("Il prezzo del biglietto è di 0.20 €/km.")

try:
    km = float(input("Quanti chilometri vuoi percorrere con il treno? "))

    if km < 1:
        print("Chilometraggio non valido. Hai inserito meno di 1 km.")
        exit()

except ValueError:
    print("Hai inserito un valore non valido. Riprova usando solo numeri.")
    exit()

risposta = input("Appartieni a una di queste categorie speciali: studente, pensionato o militare? (si / no) ").strip().lower()

# Caso NÃO tenha desconto
if risposta != "si":
    prezzo = km * 0.20
    print(f"Il prezzo finale è: {prezzo:.2f} €")
    exit()

# Caso tenha desconto
categoria = input("Di quale categoria fai parte (studente / pensionato / militare)? ").strip().lower()

if categoria not in ["studente", "pensionato", "militare"]:
    print("Categoria non valida. Questa categoria non esiste.")
    exit()

# Calcula desconto dependendo da categoria
prezzo_base = km * 0.20

if categoria == "studente":
    prezzo_finale = prezzo_base * 0.85   # 15% di sconto
elif categoria == "militare":
    prezzo_finale = prezzo_base * 0.75   # 25% di sconto
else:  # pensionato
    prezzo_finale = prezzo_base * 0.80   # 20% di sconto

print(f"Il prezzo finale è: {prezzo_finale:.2f} €")

