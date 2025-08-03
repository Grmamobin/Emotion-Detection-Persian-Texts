from tkinter import *
from respnse import response_emotion

bg_color = "#181818"
bg_gray = "#efefce"
text_color = "#EAECEE"
entry_bg_color = "#2c3e50"
placeholder_text = "Type here..."

class DetectionChatBox:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("🤠Emotion Detection🤠")
        # self.window.resizable(width=False, height=False)
        self.window.configure(width=600, height=300, bg=bg_color)
        self.text_widget = Text(
            self.window, width=20, height=2, bg=bg_color, fg=text_color ,  bd=2,                      
            relief="solid",           
            highlightthickness=2,    
            highlightbackground="#3498db", 
            highlightcolor="#3498db"        
        )
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        scrollbar = Scrollbar(self.window, command=self.text_widget.yview, width=1, bg=bg_color, troughcolor=bg_color, highlightthickness=0, bd=0)
        scrollbar.place(relheight=0.745, relx=0.999, rely=0.08)
        self.text_widget.config(yscrollcommand=scrollbar.set)

        self.bottom_canvas = Canvas(self.window, bg=bg_color, highlightthickness=0)
        self.bottom_canvas.place(relwidth=1, rely=0.83, relheight=0.07)

        entry_frame = Frame(self.window, bg=bg_color)
        entry_frame.place(relx=0.5, rely=0.835, anchor='n')

        self.msg_entry = Entry(
            entry_frame,
            bg=entry_bg_color,
            fg="gray",
            bd=0,
            font=("Helvetica", 12),
            justify="center",
            relief=FLAT
        )
        self.msg_entry.insert(0, placeholder_text)
        self.msg_entry.bind("<FocusIn>", self._clear_placeholder)
        self.msg_entry.bind("<FocusOut>", self._add_placeholder)
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        self.msg_entry.pack(ipadx=170, ipady=10, pady=5)  

    def _clear_placeholder(self, event):
        if self.msg_entry.get() == placeholder_text:
            self.msg_entry.delete(0, END)
            self.msg_entry.config(fg=text_color)

    def _add_placeholder(self, event):
        if not self.msg_entry.get():
            self.msg_entry.insert(0, placeholder_text)
            self.msg_entry.config(fg="gray")

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        if msg == placeholder_text:
            return
        self._insert_message(msg, "User")

    def _insert_message(self, msg, sender):
        if not msg.strip():
            return
        self.msg_entry.delete(0, END)
        self.text_widget.configure(state=NORMAL)

        # User message
        msg_frame = Frame(self.text_widget, bg=bg_color)
        if sender == "User":
            label = Label(
                msg_frame,
                text=f"User: {msg}",
                bg="#303F9F",
                fg="white",
                wraplength=250,
                padx=10,
                pady=5,
                bd=2,
                relief=SOLID,
                justify='right'
            )
            label.pack(anchor='e', padx=10, pady=2)
            msg_frame.pack(anchor='e', padx=10)
            self.text_widget.window_create(END, window=msg_frame)
            self.text_widget.insert(END, "\n")

        # Response
        if sender == "User":
            reply = response_emotion(msg)
            reply_frame = Frame(self.text_widget, bg=bg_color)
            reply_label = Label(
                reply_frame,
                text=f"Detector: {reply}",
                bg="#388E3C",
                fg="white",
                wraplength=250,
                padx=10,
                pady=5,
                bd=2,
                relief=SOLID,
                justify='left'
            )
            reply_label.pack(anchor='w', padx=10, pady=2)
            self.text_widget.window_create(END, window=reply_frame)
            self.text_widget.insert(END, "\n")

        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)

if __name__ == "__main__":
    app = DetectionChatBox()
    app.run()
