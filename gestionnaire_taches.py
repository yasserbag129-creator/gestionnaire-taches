taches = []

def afficher_taches(taches):
    print("\n--- Liste des tâches ---")
    for i, task in enumerate(taches, start=1):
        statue = "Fait" if task["done"] else "Non fait"
        print(f"{i}. {task['tache']} [{statue}]")
    print()

def ajouter_tache(taches):
    task = input("Quelle est la tâche à ajouter : ")
    etat = input("L'as-tu faite ? (oui/non) : ")
    taches.append({"tache": task, "done": etat.lower() == "oui"})
    print("Tâche ajoutée !\n")

def modifier_tache(taches):
    afficher_taches(taches)
    while True:
        try:
            num = int(input("Saisir le numéro de la tâche à modifier : "))
            if 1 <= num <= len(taches):
                task = input("Quelle est la nouvelle tâche : ")
                etat = input("L'as-tu faite ? (oui/non) : ")
                taches[num-1] = {"tache": task, "done": etat.lower() == "oui"}
                print("✏️ Tâche modifiée !\n")
                return
            else:
                print("Numéro non valide, réessaie.")
        except ValueError:
            print("Merci de saisir un nombre valide.")

def supprimer_tache(taches):
    afficher_taches(taches)
    while True:
        try:
            num = int(input("Entrez le numéro de la tâche à supprimer : "))
            if 1 <= num <= len(taches):
                del taches[num-1]
                print("Tâche supprimée !\n")
                return
            else:
                print("Numéro invalide. Réessaie.")
        except ValueError:
            print("Merci de saisir un nombre valide.")


while True:
    print("--- MENU ---")
    print("1. Ajouter une tâche")
    print("2. Modifier une tâche")
    print("3. Supprimer une tâche")
    print("4. Voir la liste")
    print("5. Quitter")

    choix = input("Que veux-tu faire ? (1-5) : ")

    if choix == "1":
        ajouter_tache(taches)
    elif choix == "2":
        modifier_tache(taches)
    elif choix == "3":
        supprimer_tache(taches)
    elif choix == "4":
        afficher_taches(taches)
    elif choix == "5":
        print("👋 Bye !")
        break
    else:
        print("Choix invalide, réessaie.\n")
