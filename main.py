users = [
    {"Name": "Matthew", "location": "Warszawa", "posts": 500},
    {"Name": "Zofia", "location": "Poznań", "posts": 400},
    {"Name": "Jakub", "location": "Biała Podlaska", "posts": 300},
    {"Name": "Michał", "location": "Krasnystaw", "posts": 200},

]

for user in users:
    print(f"Twój znajomy  {user["Name"]}, z miejscowości {user["location"]} opublikował {user["posts"]} postów")
