from scripts.import_data import import_csv
from scripts.analysis import run_analysis
from scripts.update_data import update_embarked_and_rescued, increase_age
from scripts.complex_queries import youngest_passengers, second_class_not_survived
from scripts.delete_data import delete_unknown_age_not_survived, delete_empty_ticket
from scripts.bonus_regex import find_doctors

if __name__ == "__main__":
    print("""
--- MENU ---
1. Importer CSV
2. Analyse simple
3. Mise à jour des données (Ex 3)
4. Requête complexe (Ex 4)
5. Suppression (Ex 5 et 7)
6. Mise à jour âge (Ex 6)
7. Regex - Bonus
8. Quitter
""")
    while True:
        choice = input("Choix (1-8): ")
        if choice == "1":
            import_csv()
        elif choice == "2":
            run_analysis()
        elif choice == "3":
            update_embarked_and_rescued()
        elif choice == "4":
            youngest_passengers()
            second_class_not_survived()
        elif choice == "5":
            delete_unknown_age_not_survived()
            delete_empty_ticket()
        elif choice == "6":
            increase_age()
        elif choice == "7":
            find_doctors()
        elif choice == "8":
            break
        else:
            print("Choix invalide.")
