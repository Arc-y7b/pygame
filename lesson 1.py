class Quiz:

    def __init__(self, student_name):
        self.student_name = student_name
        self.score = 0 
        self.questions = [
            {
                "question":"which language in mainly used in web page structure?",
                "options": ["Python", "HTML", "Java", "C++"],
                "answer": "HTML"
            },
            {
                "question":"which keyword is used to create a calss in python",
                "options": ["functions", "define", "class", "objects"],
                "answer": "class"
            } ,       
            {
                "question":"which data type stores true or false",
                "options": ["string", "integer", "boolean", "float"],
                "answer": "boolean"
            },
            {
                "question":"which symbol is used to start a command inj python?",
                "options": ["//", "#", "/*", "--"],
                "answer": "#"
            }
        ]
    def start_quiz(self):
        print("\nWelcome to the online Quiz!")
        print("student:" ,self.student_name)

        for question in self.questions:
            print("\n" + question["question"])

            for i in range (len(question["options"])):
                print(i + 1, ".", question["options"][i])

            try:
                choice = int(input("Enter your answer (1-4): "))

                if choice < 1 or choice > 4:
                    print("Invalid Choice! Please enter a number form 1 to 4. ")
                    continue

                selected_answer = question["options"][choice - 1]

                if selected_answer == question["answer"]:
                    print("correct!")
                    self.score += 1
                else:
                    print("Wrong!")
                    print("correct answer:", question["answer"])

            except ValueError:
                print("Please enter a valid number. ")


    def show_result(self):
        print("\n----- Quiz result -----")
        print("student:", self.student_name)
        print("Score:", 
              self.score, "/", len(self.questions))

        percentage = (self.score / len(self.questions))*100

        print("percentage:", percentage, "%")

student1 = Quiz("Alice")

student1.start_quiz()
student1.show_result()               