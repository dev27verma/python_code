class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_input = input(f"Q {self.question_number} {current_question.text} (True/False)?  ")
        self.check_answer(user_input,current_question.answer)

    def check_answer(self,user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            self.score += 1
            if self.score == 12:
                print(f"Congrats you got all right. Your score is {self.score} / {len(self.question_list)}")
            else:
                print(f"You got it right, Score is {self.score}")
        else:
            print(f"You got it wrong, Correct answer is {correct_answer}, You score {self.score}/{len(self.question_list)}")
            exit()
