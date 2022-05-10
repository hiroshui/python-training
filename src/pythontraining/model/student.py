from model.person import Person


class Student(Person):
    
    def learn(self, topic = str):
        return f"{self.firstname} is learning {topic}."