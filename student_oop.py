class Student: 
    def __init__(self, name, age, major, gpa):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa

    def get_name(self):
        return self.title

    def get_age(self):
        return self.age

    def get_major(self):
        return self.major
    
    def get_GPA(self):
        return self.gpa
    
    def calculate_grade(self):
        """
        Calculate and return the letter grade based on GPA. Grading scale:
        - A: 4.0 or higher
        - B: 3.0 to 3.9
        - C: 2.0 to 2.9
        - D: 1.0 to 1.9
        - F: below 1.0
        """
        if self.gpa >= 4.0:
            return "A"
        elif 3.0 <= self.gpa < 4.0:
            return "B"
        elif 2.0 <= self.gpa < 3.0:
            return "c"
        elif 1.0 <= self.gpa < 2.0:
            return "D"
        else:
            return "F"