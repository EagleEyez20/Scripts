# This program is creating a student "class". In the app.py file it shows the actual Object as the student.

class Student:
    # This next part is called the initialized function. It will define the attributes of a student.
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    #def __init__(self):
     #   if self.gpa >= 3.5:
     #       return True
     #   else:
     #       return False
     
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
        
        
