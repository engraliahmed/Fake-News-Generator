import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random

# Data
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

headline_prefix = "BREAKING NEWS"
headline_list = []


# GUI App
class FakeNewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake News Generator")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.category_var = tk.StringVar()
        self.headline_var = tk.StringVar()

        title_label = tk.Label(
            root, text="Fake News Generator", font=("Helvetica", 16, "bold")
        )
        title_label.pack(pady=10)

        category_frame = tk.Frame(root)
        category_frame.pack(pady=5)
        tk.Label(category_frame, text="Select Category: ", font=("Helvetica", 12)).pack(
            side=tk.LEFT
        )
        self.category_dropdown = ttk.Combobox(
            category_frame,
            textvariable=self.category_var,
            values=list(categories.keys()),
            state="readonly",
        )
        self.category_dropdown.pack(side=tk.LEFT, padx=10)
        self.category_dropdown.set("cricket")

        generate_button = tk.Button(
            root,
            text="Generate Headline",
            command=self.generate_headline,
            bg="#4CAF50",
            fg="white",
            font=("Helvetica", 12),
        )
        generate_button.pack(pady=10)

        self.result_label = tk.Label(
            root, text="", font=("Helvetica", 12), wraplength=550, justify="center"
        )
        self.result_label.pack(pady=10)

        save_button = tk.Button(
            root,
            text="Save Headlines to File",
            command=self.save_headlines,
            bg="#2196F3",
            fg="white",
            font=("Helvetica", 12),
        )
        save_button.pack(pady=5)

        exit_button = tk.Button(
            root,
            text="Exit",
            command=root.quit,
            bg="#f44336",
            fg="white",
            font=("Helvetica", 12),
        )
        exit_button.pack(pady=5)

    def generate_headline(self):
        category = self.category_var.get()
        if category in categories:
            subject = random.choice(categories[category])
            action = random.choice(actions)
            obj = random.choice(objects)
            headline = f"{headline_prefix}: {subject} {action} {obj}"
            self.headline_var.set(headline)
            self.result_label.config(text=headline)
            headline_list.append(headline)
        else:
            messagebox.showerror("Invalid Category", "Please select a valid category.")

    def save_headlines(self):
        if not headline_list:
            messagebox.showwarning("No Headlines", "No headlines to save!")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            with open(file_path, "w") as f:
                for h in headline_list:
                    f.write(h + "\n")
            messagebox.showinfo("Success", "Headlines saved successfully!")


# Run App
if __name__ == "__main__":
    root = tk.Tk()
    app = FakeNewsApp(root)
    root.mainloop()
