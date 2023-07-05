from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#4E31AA"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}",foreground="white",bg=THEME_COLOR)
        self.score.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, text="START", fill="black", font=("Arial",20,"italic"), width=280)
        self.canvas.grid(column=0,row=1,columnspan=2, pady=50)

        wrong = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong, highlightthickness=0, command=self.check_false)
        self.wrong_btn.grid(column=1, row=2)

        right = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=right, highlightthickness=0, command=self.check_true)
        self.right_btn.grid(column=0, row=2)

        self.next_question = self.window.after(1000, func=self.get_question)

        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg="white")
        self.wrong_btn.config(state="active")
        self.right_btn.config(state="active")
        if self.quiz.still_has_questions():                 
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text=f"You've completed the quiz!\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.wrong_btn.config(state="disabled")
            self.right_btn.config(state="disabled")

    def check_true(self):
        self.feedback(self.quiz.check_answer("true"))

    def check_false(self):
        self.feedback(self.quiz.check_answer("false"))

    def feedback(self, answer):
        self.right_btn.config(state="disabled")
        self.wrong_btn.config(state="disabled")
        self.window.after_cancel(self.next_question)
        if answer is True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.next_question = self.window.after(1000, func=self.get_question)