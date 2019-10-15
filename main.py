class PracticeTestMaker:

    def parse_input(self, input_file):
        filepath = input_file
        questions = []
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                line = fp.readline()

        return questions


    def createTest(self, question_file, amt_of_qs):
        question_bank = self.parse_input(question_file)


if __name__ == '__main__':
    p = PracticeTestMaker()
    p.createTest('cv_questions.txt',5)
