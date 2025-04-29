def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy  {user["Name"]}, z miejscowości {user["location"]} opublikował {user["posts"]} postów")


def add_user(users_data: list) -> None:
    new_name = input('podaj imie nowego uzytkownika: ')
    new_location = input('podaj nową lokalizację: ')
    new_post = int(input('podaj ilość postów: '))
    users_data.append({"Name": new_name, "location": new_location, "posts": new_post})


def remove_user(users_data: list) -> None:
    uzytkownik_do_usunięcia = input('podaj uzytkownika do usunięcia: ')

    for user in users_data:
        if user['Name'] == uzytkownik_do_usunięcia:
            users_data.remove(user)



def update_user(users_data: list) -> None:


    uzytkownik_do_edycji = input('podaj uzytkownika do edycji: ')
    for user in users_data:
        if user['Name'] == uzytkownik_do_edycji:
            user['Name'] = input('Podaj nowe imie uzytkownika: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = int(input('Podaj nową liczbę postów: '))
