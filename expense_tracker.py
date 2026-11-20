expenses = []


def add_expense():
    description = input("Description : ")
    amount = float(input("Montant: "))
    expenses.append({
        "description": description,
        "amount": amount,
    })
    print("Depense ajoutee !")
   


def show_expenses():
    if not expenses:
        print("Aucune depense enregistree.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - {expense['amount']:.2f}")
    

def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total: {total:.2f}")

def delete_expense():
    if not expenses:
        print("Aucune depense a supprimer.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']}")
    choice = input("Numero de la depense a supprimer: ")
    if not choice.isdigit():
        print("Numero de depense invalide.")
        return
    index = int(choice) - 1
    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Supprime : {removed['description']}")
    else:
        print("Numero de depense invalide.")


def main():
    while True:
        print("\n===== SUIVI DES DEPENSES =====")
        print("1. Ajouter une depense")
        print("2. Afficher les depenses")
        print("3. Afficher le total")
        print("4. Quitter")
        print("5. Supprimer une depense")
        choice = input("Votre choix: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Au revoir !")
            break
        elif choice == "5":
            delete_expense()
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()


