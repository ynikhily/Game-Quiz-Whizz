# THIS IS RESPONSIBLE FOR CREATING THE UI OF OUR QUIZ APP AS A CLASS.
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUES_FONT = ("Arial", 20, 'italic')


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz-ine")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0",
                                 bg=THEME_COLOR)
        self.score_label.config(padx=10, pady=10)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Here goes the question",
                                                     font=QUES_FONT,
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        true_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.is_true)
        self.true_button.grid(row=2, column=0, padx=10, pady=10)

        false_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.is_false)
        self.false_button.grid(row=2, column=1, padx=10, pady=10)
        self.get_next_question()
        self.window.mainloop()


    def is_true(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def is_false(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of this quiz. Thanks!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
