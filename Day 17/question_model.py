class Question():
    '''
    A class to represent a question.
    Input question with dictionary 'text':'question' and 'answer':'answer'
    '''
    def __init__(self, question):
        self.text = question['text']
        self.answer = question['answer']
