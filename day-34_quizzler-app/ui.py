from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
FONT_SCORE = ("Arial", 15, "normal")


class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(height=300, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 150, width=280, text="Question", font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.click_true)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.click_false)
        self.true_button.grid(column=1, row=2)
        self.false_button.grid(column=0, row=2)

        self.score_label = Label(text=f"Score: 0")
        self.score_label.config(bg=THEME_COLOR, fg="white", font=FONT_SCORE)
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def click_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # self.get_next_question()

    def click_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        # self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=f"{self.quiz.next_question()}")
        else:
            self.canvas.itemconfig(self.question_text, text="You reached end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        self.window.after(1000, self.get_next_question)
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
