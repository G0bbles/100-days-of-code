class QuizBrain():
    """
    A class to represent a quiz machine.

    Attributes:
        question_number (int): Current question index.
        question_list (list): List of question objects (see `question_model`).
        score (int): Number of correct answers.
    """

    def __init__(self, question_list):
        """
        Initialize a QuizBrain instance.

        Args:
            question_list (list): List of question objects containing `text` and `answer`.
        """
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def has_questions_left(self):
        """
        Check if there are questions left in the quiz.

        Returns:
            bool: True if there are remaining questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def ask_questions(self):
        """
        Ask the current question and prompt the user for input.

        Returns:
            bool: True if the answer is correct and False if incorrect 
            by calling check_answer()
        """
        question_object = self.question_list[self.question_number]
        question = question_object.text
        answer = question_object.answer
        user_answer = input(f"Q.{self.question_number + 1}: "
                            f"{question} (True/False)?: ").capitalize()
        return self.check_answer(answer, user_answer)

    def check_answer(self, answer, user_answer):
        """
        Compare the user's answer with the correct one.

        Args:
            answer (str): The correct answer ("True" or "False").
            user_answer (str): The user's input.

        Returns:
            bool: True if correct, False if incorrect,
            ask_questions() if the input was invalid.
        """
        if user_answer == answer:
            print("That's correct!")
            self.score += 1
            self.question_number += 1
            return True
        elif (user_answer == 'True' and answer == 'False') or\
            (user_answer == 'False' and answer == 'True'):
            print("That's incorrect")
            self.question_number += 1
            return False
        else:
            print("Please enter 'True' or 'False'")
