from services.studytracker_service import studytracker_service

def main():
    print("-- Opintojenseuranta-app --")
    while True:
        if studytracker_service.user == None:
            choice = input("Syötä 1 kirjautuaksesi sisään tai 2 luodaksesi käyttäjätunnuksen: ")
            try:
                if choice == "1":
                    print("Sisäänkirjautuminen")
                    username = input("Käyttäjätunnus: ")
                    password = input("Salasana: ")
                    studytracker_service.login(username, password)
                elif choice == "2":
                    print("-- Käyttäjätunnuksen luominen --")
                    username = input("Anna väh. 4 merkkiä pitkä käyttäjätunnus: ")
                    password = input("Anna väh. 5 merkkiä pitkä salasana: ")
                    studytracker_service.create_user(username, password)
                else:
                    print("-- Virheellinen syöte --")
            except Exception as e:
                print(e)
                continue
        if studytracker_service.user:
            print("-- Olet kirjautunut sisään --")
            choice = input("Syötä 1 uloskirjautuksesi: ")
            if choice == "1":
                studytracker_service.logout()
                break






if __name__ == "__main__":
    main()