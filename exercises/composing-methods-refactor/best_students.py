# refactor with extract method
# extract find_graduated_students
# have it return graduated students
# use query for passed_students
class Employer:
    def __init__(self, name):
        self.name = name

    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')


class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")


class School:
    def __init__(self, students) -> None:
        self.students = students

    def process_graduation(self):
        self.print_graduated_students()
        self.send_congrats_emails()
        self.send_top_students_to_employers()

    def print_graduated_students(self):
        passed_students = self.get_passed_students()
        print('*** Student who graduated *** ')
        for s in passed_students:
            print(s.name)
        print('****************************')
    
    def send_congrats_emails(self):
        passed_students = self.get_passed_students()
        for s in passed_students:
            s.send_congrats_emails()
            
    def send_top_students_to_employers(self):
        passed_students = self.get_passed_students()
        percentile = 0.9
        index = int(percentile * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)
            
    def get_passed_students(self):
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)
        return passed_students

students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school = School(students)
school.process_graduation()