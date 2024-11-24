from services.studytracker_service import studytracker_service

def run():
    print("\n**Opintojenseuranta-app**")
    while True:
        if studytracker_service.user is None:
            print("\n-Toiminnot-\n1-Kirjaudu sisään\n2-Luo uusi käyttäjätunnus\n3-Sulje sovellus")
            choice = input(
                "Valitse toiminto: ")
            try:
                if choice == "1":
                    print("\n-Sisäänkirjautuminen-")
                    username = input("Käyttäjätunnus: ")
                    password = input("Salasana: ")
                    if studytracker_service.login(username, password):
                        print("\n-Olet kirjautunut sisään-")
                elif choice == "2":
                    print("\n-Käyttäjätunnuksen luominen-")
                    username = input(
                        "Syötä väh. 4 merkkiä pitkä käyttäjätunnus: ")
                    password = input("Syötä väh. 5 merkkiä pitkä salasana: ")
                    if studytracker_service.create_user(username, password):
                        print("\n-Käyttäjätunnuksen luominen onnistui-")
                elif choice == "3":
                    break
                else:
                    print("\n-Virheellinen syöte-\n")
            except ValueError as e:
                print(f"\n{e}")
                continue
        if studytracker_service.user:
            print("\n***Valinnat***\n1-Luo uusi tehtävä\n2-Katsele lisättyjä tehtäviä\n3-Kirjaudu ulos")
            choice = input("Valitse toiminto: ")
            try:
                if choice == "1":
                    topic = input("Syötä aihe: ")
                    category = input("Syötä kategoria: ")
                    deadline = input("Syötä deadline muodossa \"d.m.yyyy\": ")
                    studytracker_service.create_task(topic, category, deadline)
                    print("\nTehtävä lisätty!")
                elif choice == "2":
                    print("\n*Tehtävälistaus*\n---")
                    tasks = studytracker_service.find_users_tasks()
                    if not tasks:
                        print("\nEi lisättyjä tehtäviä")
                        continue
                    for task in tasks:
                        print(f"Aihe: {task.topic}\nKategoria: {task.category}\nDeadline: {task.deadline}\nDone: {task.done}\n---")
                elif choice == "3":
                    studytracker_service.logout()
                    print("\n-Olet kirjautunut ulos-")
                else:
                    print("\n-Virheellinen syöte-")
            except ValueError as e:
                print(f"\n{e}")
                continue

