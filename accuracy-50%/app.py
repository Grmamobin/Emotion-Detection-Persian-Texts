from tkinter import *
from respnse import response_emotion
bg_color = "#181818"
bg_gray = "#efefce"
text_color = "#EAECEE"

class DetectionChatBox:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Emotion Detection")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=bg_color)

        # Head Label
        head_label = Label(self.window, bg=bg_gray, fg=text_color, text="Welcome", pady=10)
        head_label.place(relwidth=1, rely=0.01, relheight=0.05)

        # Divider
        line = Label(self.window, width=450, bg=bg_color)
        line.place(relwidth=1, relheight=0.012, rely=0.07)

        # Text widget for chat
        self.text_widget = Text(self.window, width=20, height=2, bg=bg_color, fg=text_color, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # Scrollbar
        scrollbar = Scrollbar(self.window, command=self.text_widget.yview)
        scrollbar.place(relheight=0.745, relx=0.974, rely=0.08)
        self.text_widget.config(yscrollcommand=scrollbar.set)

        # Bottom label (input box container)
        bottom_label = Label(self.window, bg=bg_gray, height=80)
        bottom_label.place(relwidth=1, rely=0.83, relheight=0.07)

        # Message entry box
        self.msg_entry = Entry(bottom_label, bg="#2c3e50", fg=text_color)
        self.msg_entry.place(relwidth=0.74, relheight=1, rely=0, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # Snd button
        send_button = Button(bottom_label, text="Send", width=20 , bg=bg_gray , command=lambda:self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0, relheight=1, relwidth=0.22)
        

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "User")

    def _insert_message(self, msg, sender):
        if not msg.strip():
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END) 
        
        msg2 = f"Detection: {response_emotion(msg)}\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)  

if __name__ == "__main__":
    app = DetectionChatBox()
    app.run()
