from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizz")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.question = None

        self.label_score = Label(text=f"Score: {self.score}", font=13,
                                 background=THEME_COLOR, fg="white")
        self.label_score.grid(row=1, column=2, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.text_canvas = self.canvas.create_text(150, 125, text=f"{self.question}",
                                                   font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=2, column=1, columnspan=2, padx=20, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, borderwidth=0, command=self.true_answer)
        self.true_button.grid(row=3, column=1, padx=20, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, borderwidth=0, command=self.false_answer)
        self.false_button.grid(row=3, column=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.question = self.quiz.next_question()
            self.canvas.itemconfig(self.text_canvas, text=f"{self.question}")
            self.label_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text_canvas, text="You have reached the end of the quiz")
            # prevent the button from being pressed
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)