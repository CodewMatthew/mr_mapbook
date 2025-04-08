from Utils.controller import get_user_info
from Utils.model import users


def main():
    while True:
        print("===========menu=========")
        print("0 - zamknij aplikacje")
        print("1 - wyswietl co u znajomych ")
        print("2 - dodaj nowego uzytkownika")
        print("3 - usun uzytkownika")
        print("3 - edytuj uzytkownika")
        print("===========menu=========")

    choice = input("wybierz opcje menu")

    if choice =="0":
        break
    if choice =="1":
        get_user_info(users)





    if __name__ == "__main__":
        main()

