# Import Random

import random

categories = {
    "cricket": [
        "Cristiano Ronaldo",
        "Virat Kohli",
        "Lionel Messi",
        "Shahid Afridi",
        "Roger Federer",
        "Serena Williams",
        "Babar Azam",
        "Neymar Jr",
        "LeBron James",
        "Kylian Mbappe",
    ],
    "politics": [
        "Imran Khan",
        "Donald Trump",
        "Narendra Modi",
        "Joe Biden",
        "Nawaz Sharif",
        "Shehbaz Sharif",
        "Xi Jinping",
        "Vladimir Putin",
        "Boris Johnson",
        "Justin Trudeau",
    ],
    "showbiz": [
        "Tom Cruise",
        "Angelina Jolie",
        "Atif Aslam",
        "Ali Zafar",
        "Mahira Khan",
        "Dwayne Johnson",
        "Taylor Swift",
        "Selena Gomez",
        "Brad Pitt",
        "Shahrukh Khan",
    ],
    "media": [
        "BBC News",
        "CNN",
        "ARY News",
        "Geo News",
        "Al Jazeera",
        "Fox News",
        "Dawn News",
        "The New York Times",
        "Reuters",
        "The Guardian",
    ],
    "regions": [
        "Lahore",
        "Karachi",
        "Islamabad",
        "New York",
        "Dubai",
        "London",
        "Paris",
        "Beijing",
        "Tokyo",
        "Sydney",
    ],
    "business": [
        "Elon Musk",
        "Bill Gates",
        "Jeff Bezos",
        "Apple Inc.",
        "Microsoft",
        "Google",
        "Meta",
        "Samsung",
        "Tesla",
        "Alibaba",
    ],
}

# Actions: what they do
actions = [
    "rides",
    "eats",
    "kisses",
    "fights with",
    "hugs",
    "jumps over",
    "buys",
    "dances with",
    "steals",
    "throws",
]

# Objects: funny things, animals, random objects
objects = [
    "a cat",
    "a UFO",
    "a burger",
    "a flying carpet",
    "a giant balloon",
    "a robot",
    "a magic wand",
    "a dinosaur",
    "a TikTok star",
    "a camel",
]

# Configurable headline prefix
headline_prefix = "BREAKING NEWS"

# Loop to iterate
headline_list = []

while True:
    category_input = input(
        "Select a category cricket, politics, showbiz, media, regions, business:\n"
    )
    if category_input in categories:
        subjects = categories[category_input]
        subject = random.choice(subjects)
        obj = random.choice(objects)
        action = random.choice(actions)

        headline = f"{headline_prefix}: {subject} {action} {obj}"
        user_input = (
            input("Do you want to regenerate the headline again? (yes/no): ")
            .strip()
            .lower()
        )
        headline_list.append(headline)
        if user_input == "no":
            break
    else:
        print("Invalid category. Please try again.")

text_file = (
    input("Do you want to save the headlines to a text file? (yes/no): ")
    .strip()
    .lower()
)

if text_file == "yes":
    file_path = "headlines.txt"
    with open(file_path, "w") as file:
        for h in headline_list:
            file.write(h + "\n")
    print("Headlines saved successfully")

print("Thank you for using the Fake News Generator.")
