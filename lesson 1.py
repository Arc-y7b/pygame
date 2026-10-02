class quiz:

    def __init__(self, student_name):
        self.student_name = student_name
        self.score = 0 
        self.questions = [
            {
                "question":"which language in mainly used in web page structure?",
                "options": ["Python", "HTML", "Java", "C++"],
                "answer": "HTML"
            }
            {
                "question":,"which keyword is used to create a calss in python"
                "options": ["functions", "define", "class", "objects"],
                "answer": "class"
            }        
            {
                "question":,"which data type stores true or false"
                "options": ["string", "integer", "boolean", "float"],
                "answer": "boolean"
            }
            {
                "question":,"which symbol is used to start a command inj python?"
                "options": ["//", "#", "/*", "--"],
                "answer": "#"
            }

    def start_quiz(self):
    print("\nWelcome to the online Quiz!")
    print("student:" self.student_name)

    for question in self.questions:
    print("\n" + question["question"])

    for i in range (len(question["options"])):
        print(i + 1, ".", question["options"][i])

    choice = int(input("Enter your answer (1-4): "))

    selected_answer = question[optioms][choice - 1]

    if selective_answer == question["answer"]:
       print("correct!")
       self.score += 1
    else:
       print("Wrong!")
       print("correct answer:", question["answer"])

def show_result(self):
   print("\n----- Quiz result -----")
   print("student:", self.student_name)
   print("Score:", self.score "/", len(self.questions))

   percentage = (self.score / len(self.questions))*100

   print("percentage:", percentage, "%")

student1 = Quiz("Alice")

student1.start_quiz()
student1.show_results()               