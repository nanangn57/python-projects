class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input_answer = input(f"Q{self.question_number}:{current_question.text} (True/False): ")
        self.check_answer(input_answer, current_question)

    def check_answer(self, user_answer, question):
        if user_answer.lower() == question.answer.lower():
            self.score += 1
            print(f"You got it right. Your score is {self.score}/{self.question_number}")
        else:
            print(f"That's wrong. Your score is {self.score}/{self.question_number}")
        print(f"The correct answer is {question.answer}")
