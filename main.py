import customtkinter as ctk
import time
import random
from tkinter import messagebox


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")
        ctk.set_appearance_mode("dark")  # Set dark mode
        ctk.set_default_color_theme("blue")  # Set color theme

        self.sample_texts = [
            "The sun set behind the mountains, casting a warm golden glow over the valley, while the birds chirped happily, signaling the end of another beautiful day in paradise.",
            "As the rain poured down, the children splashed in the puddles, laughing and playing, completely unaware of the storm brewing in the distance, which would soon change everything.",
            "In the quiet library, a young girl discovered a dusty old book filled with magical tales, transporting her to distant lands where dragons roamed and heroes fought for justice.",
            "The aroma of freshly baked bread wafted through the air, drawing neighbors to the small bakery, where they gathered to share stories and enjoy the simple pleasures of life.",
            "Under the starry night sky, the campers gathered around the fire, sharing ghost stories and roasting marshmallows, creating memories that would last a lifetime in the heart of nature.",
            "With each stroke of the brush, the artist brought the canvas to life, capturing the vibrant colors of the sunset and the serene beauty of the landscape before her.",
            "As the clock struck midnight, the city came alive with lights and sounds, as people celebrated the New Year, filled with hope and dreams for the future ahead.",
            "The old man sat on the park bench, feeding the pigeons while reminiscing about his youth, reflecting on the choices he made and the adventures that shaped his life.",
            "In a small village, the annual festival brought everyone together, with laughter, music, and delicious food, celebrating the rich culture and traditions that had been passed down through generations.",
            "The scientist worked tirelessly in her lab, conducting experiments and analyzing data, driven by her passion for discovery and the desire to make a difference in the world."
        ]
        self.start_time = None
        self.end_time = None
        self.current_sample_text = ""

        self.create_widgets()

    def create_widgets(self):
        # Sample text label
        self.text_label = ctk.CTkLabel(self.root, text="Type the following text:", font=("Arial", 14))
        # self.text_label.pack(pady=10)

        # Display sample text
        self.sample_text_label = ctk.CTkLabel(self.root, text="", font=("Arial", 12), wraplength=500)
        # self.sample_text_label.pack(pady=10)

        # Text entry for user input
        self.user_input = ctk.CTkTextbox(self.root, height=55, font=("Arial", 12))
        # self.user_input.pack(pady=10)

        # Start button
        self.start_button = ctk.CTkButton(self.root, text="Start", command=self.start_typing_test, font=("Arial", 12))
        self.start_button.pack(pady=10)

        # Result label
        self.result_label = ctk.CTkLabel(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.done_button = ctk.CTkButton(self.root, text="Done", command=self.failed, font=("Arial", 12))
        # self.done_button.pack(pady=10)

    def start_typing_test(self):
        self.user_input.delete(1.0, ctk.END)  # Clear previous input
        self.result_label.configure(text="")  # Clear previous results
        self.current_sample_text = random.choice(self.sample_texts)  # Select a random sample text
        self.sample_text_label.configure(text=self.current_sample_text)  # Update the sample text label
        self.start_button.configure(text="Start Again")
        self.text_label.pack(pady=10)
        self.sample_text_label.pack(pady=10)
        self.user_input.pack(pady=10)
        self.done_button.pack(pady=10)
        self.start_time = time.time()  # Record start time
        self.user_input.bind("<KeyRelease>", self.check_input)  # Bind key release event

    def check_input(self, event):
        typed_text = self.user_input.get(1.0, ctk.END).strip()
        if typed_text == self.current_sample_text:
            self.end_time = time.time()  # Record end time
            self.calculate_wpm()
        elif len(typed_text) > len(self.current_sample_text):
            messagebox.showinfo("Typing Test Failed", "You typed too many characters.")

    def calculate_wpm(self):
        time_taken = self.end_time - self.start_time  # Calculate time taken in seconds
        words_typed = len(self.current_sample_text.split())  # Count words in the sample text
        wpm = (words_typed / time_taken) * 60  # Calculate words per minute
        self.result_label.configure(text=f"Your typing speed: {wpm:.2f} WPM")
        self.user_input.unbind("<KeyRelease>")  # Unbind the event after test completion
        messagebox.showinfo("Typing Test Complete", f"Your typing speed: {wpm:.2f} WPM")

    def failed(self):
        messagebox.showinfo("Typing Test Failed", "You didn't type enough characters")


if __name__ == "__main__":
    root = ctk.CTk()  # Create a CustomTkinter window
    app = TypingSpeedApp(root)
    root.mainloop()