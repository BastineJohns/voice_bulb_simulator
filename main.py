import threading
import tkinter as tk
from PIL import Image, ImageTk

from voice_control import VoiceController

class BulbApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice-Controlled Bulb")

        # Load the Images
        self.img_off = ImageTk.PhotoImage(Image.open('assets/bulb_off.jpg'))
        self.img_on = ImageTk.PhotoImage(Image.open('assets/bulb_on.jpg'))

        # Label to display the bulb image
        self.bulb_label = tk.Label(root, image=self.img_off)
        self.bulb_label.pack(padx=20, pady=20)

        # Start voice controller in a separate thread
        self.voice_ctrl = VoiceController(self.command_callback)
        threading.Thread(target=self.voice_ctrl.listen_forever, daemon=True).start()

    def command_callback(self, command_text):
        """
        This function is called whenever speech is recognized.
        We check the text and update the GUI accordingly.
        """
        text = command_text.lower()
        if "turn on" in text:
            self.bulb_label.config(image=self.img_on)
        elif "turn off" in text:
            self.bulb_label.config(image=self.img_off)
        # (You can add more commands here, e.g., brightness)

if __name__ == "__main__":
    root = tk.Tk()
    app = BulbApp(root)
    root.mainloop()