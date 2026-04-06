import random
dest={

    "city":["Paris","New York","Tokyo","Sydney","Rome"],
    "mountains" : ["Alps","Rockies","Himalayas","Andes","Appalachians"],
    "beach" : ["Maldives","Bora Bora","Maui","Phuket","Santorini"]
}
joke=[
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]
while True: 
    user=input("Where would you like to go on vacation? (city/mountains/beach or you want to hear a joke? or quit): ").strip().lower()
    if user=="dest": 
        choice=input("Great! Do you prefer city, mountains, or beach? ").strip().lower()
        print(random.choice(dest.get(choice, ["Sorry, we don't have suggestions for that category."])))             
    elif user=="joke": 
        print(random.choice(joke))
    elif user=="quit":
        print("Thanks for chatting! Have a great day!")
        break
    else:
        print("Sorry, I didn't understand that. Please choose 'city', 'mountains', 'beach', 'joke', or 'quit'.")