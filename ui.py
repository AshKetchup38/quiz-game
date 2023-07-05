from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#4E31AA"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score = Label(text="Score: 0",foreground="white",bg=THEME_COLOR)
        self.score.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, text="Text goes here", fill="black", font=("Arial",20,"italic"), width=280)
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)

        wrong = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong, highlightthickness=0, command=self.check_true)
        self.wrong_btn.grid(column=1, row=2)

        right = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=right, highlightthickness=0, command=self.check_false)
        self.right_btn.grid(column=0, row=2)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text, text=q_text)

    def check_true(self):
        answer = self.quiz.check_answer("true")
        if answer is True:
            print("Correct")
        else:
            print("False")

    def check_false(self):
        answer = self.quiz.check_answer("false")
        if answer is True:
            print("Correct")
        else:
            print("False")