import random

class PracticeTestMaker:

    def parse_input(self, input_file):
        filepath = input_file
        questions = []
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                question = line.strip()
                questions.append(question)
                line = fp.readline()

        return questions


    def chooseQuestions(self, questions, amt_of_qs):
        exam_questions = []

        while amt_of_qs > 0:
            element = random.randint(0, len(questions)) 
            exam_questions.append(questions.pop(element))
            amt_of_qs -= 1

        return exam_questions


    def writeOutExam(self, questions):
        with open("practice_exam.txt","w+") as sf:
            for question in questions:
                sf.write(question)
                sf.write('\n')
                sf.write('\n')
                sf.write('\n')
            

    def createTest(self, question_file, amt_of_qs):
        question_bank = self.parse_input(question_file)
        exam_questions = self.chooseQuestions(question_bank, amt_of_qs)
        self.writeOutExam(exam_questions)


if __name__ == '__main__':
    p = PracticeTestMaker()
    p.createTest('cv_questions.txt',5)
