from tkinter import *

from quiz import Train

class interface:

    def __init__(self, quiz:Train):
        self.quiz1=quiz
        self.window = Tk()
        self.window.title("Ticket")
        self.window.config(padx=20, pady=20,bg='#25395C')

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)
        self.question_text = self.canvas.create_text(150,125,
        width=280,
        text="Some Question text", fill= "#25395C", font=("Arial",15,"italic"))
        
        self.seat1 = Label(text="(Black diamond) seat: 300",fg="white",bg="#25395C")
        self.seat1.grid(row=0, column=0)

        self.seat2 = Label(text="(Poorva Express) seat: 250",fg="white",bg="#25395C")
        self.seat2.grid(row=0, column=1)


        black_image = PhotoImage(file = "E:/python/train/image/black.png")
        self.black_button = Button(image=black_image,highlightthickness=0, command=self.black_pressed)
        self.black_button.grid(row=2, column=0)

        poorva_image = PhotoImage(file = "E:/python/train/image/poorva.png")
        self.poorva_button = Button(image=poorva_image,highlightthickness=0, command=self.poorva_pressed)
        self.poorva_button.grid(row=2, column=1)


        self.get_ticketbook()

        self.window.mainloop()
    
    def get_ticketbook(self):
        self.canvas.config(bg="white")
        if self.quiz1.booking_continue():
            self.seat1.config(text=f"(Black diamond) seat: {self.quiz1.seat1}")
            self.seat2.config(text=f"(Poorva Express) seat: {self.quiz1.seat2}")
            tick_book = self.quiz1.bookTicket()
            self.canvas.itemconfig(self.question_text,text=tick_book)

    def black_pressed(self):
        is_right = self.quiz1.train_name("black diamond")
        self.give_feedback(is_right)
        
    
    def poorva_pressed(self):
        is_right1 = self.quiz1.train_name("poorva express")
        self.give_feedback1(is_right1)
    

    def give_feedback(self, is_right):
        if is_right:
            
            # self.canvas.itemconfig(self.question_text, text = is_right)
            
            self.canvas.itemconfig(self.question_text, text = "Booked")

            self.canvas.config(bg="green")
            
        self.window.after(1000, self.get_ticketbook)


    def give_feedback1(self, is_right1):
        if is_right1:

            # self.canvas.itemconfig(self.question_text, text = is_right1)
            
            self.canvas.itemconfig(self.question_text, text = "Booked")

            self.canvas.config(bg="yellow")

        self.window.after(1000, self.get_ticketbook)
                   