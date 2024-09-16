import logging

logging.basicConfig(filename="record.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Student:
    _id_counter = 1

    def __init__(self, firstname, lastname, qualification, email, mobile_no, age):
        self.id = Student._id_counter
        Student._id_counter += 1
        self.student_firstname = firstname
        self.student_lastname = lastname
        self.qualification = qualification
        self.email = email
        self.mobile_no = mobile_no
        self.age = age
        self.enrolled_course = []
        self.institute_name = "The Kiran Academy"
        logging.info(f"Created student with ID {self.id}")

    def add_course(self, course):
        try:
            if not isinstance(course, Course):
                raise TypeError("The course must be an instance of the Course class.")
            self.enrolled_course.append(course)
            logging.info(f"Added course {course.name} to Student ID {self.id}")
        except TypeError as e:
            logging.error(e)
        except Exception as e:
            logging.error(f"An unexpected error occurred while adding course: {e}")

    def remove_course(self, course):
        try:
            if not isinstance(course, Course):
                raise TypeError("The course must be an instance of the Course class.")
            if course in self.enrolled_course:
                self.enrolled_course.remove(course)
                logging.info(f"Removed course {course.name} from Student ID {self.id}")
            else:
                logging.warning(f"Course {course.name} not found in Student ID {self.id}'s enrollments")
        except TypeError as e:
            logging.error(e)
        except Exception as e:
            logging.error(f"An unexpected error occurred while removing course: {e}")

    def student_details(self):
        try:
            logging.info("Checking the details of the student")
            course_names = ', '.join([course.name for course in self.enrolled_course])
            return f"""
                ID: {self.id}
                Student's First Name: {self.student_firstname}
                Student's Last Name: {self.student_lastname}
                Student's Qualification: {self.qualification}
                Student's Email: {self.email}
                Student's Mobile Number: {self.mobile_no}
                Student's Age: {self.age}
                Enrolled Courses: {course_names}
                Institute Name: {self.institute_name}"""
        except Exception as e:
            logging.error(f"An error occurred while retrieving student details: {e}")
            return None

class Course:
    _code_counter = 1

    def __init__(self, name, duration, fee):
        self.code = Course._code_counter
        Course._code_counter += 1
        self.name = name
        self.duration = duration
        self.fee = fee
        logging.info(f"Created course {self.name} with code {self.code}")

    def course_details(self):
        try:
            logging.info("Checking course details")
            return f"""
                Course Code: {self.code}
                Course Name: {self.name}
                Duration: {self.duration}
                Course Fees: {self.fee}"""
        except Exception as e:
            logging.error(f"An error occurred while retrieving course details: {e}")
            return None

class EnrollmentManager:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_students(self, student):
        try:
            if not isinstance(student, Student):
                raise TypeError("The student must be an instance of the Student class.")
            self.students[student.id] = student
            logging.info(f"Student with ID {student.id} added")
        except TypeError as e:
            logging.error(e)
        except Exception as e:
            logging.error(f"An unexpected error occurred while adding student: {e}")

    def add_courses(self, course):
        try:
            if not isinstance(course, Course):
                raise TypeError("The course must be an instance of the Course class.")
            self.courses[course.code] = course
            logging.info(f"Course with code {course.code} added.")
        except TypeError as e:
            logging.error(e)
        except Exception as e:
            logging.error(f"An unexpected error occurred while adding course: {e}")

    def enroll_student_in_course(self, student_id, course_code):
        try:
            student = self.students.get(student_id)
            course = self.courses.get(course_code)
            if student and course:
                student.add_course(course)
                logging.info(f"Student ID {student_id} enrolled in course {course_code}")
            else:
                raise ValueError("Student or course not found")
        except ValueError as e:
            logging.warning(e)
        except Exception as e:
            logging.error(f"An unexpected error occurred while enrolling student in course: {e}")

    def withdraw_student_from_course(self, student_id, course_code):
        try:
            student = self.students.get(student_id)
            course = self.courses.get(course_code)
            if student and course:
                student.remove_course(course)
                logging.info(f"Student ID {student_id} withdrawn from course {course_code}")
            else:
                raise ValueError("Student or course not found")
        except ValueError as e:
            logging.warning(e)
        except Exception as e:
            logging.error(f"An unexpected error occurred while withdrawing student from course: {e}")

    def get_student_details(self, student_id):
        try:
            student = self.students.get(student_id)
            if student:
                return student.student_details()
            else:
                raise ValueError(f"Student with ID {student_id} not found")
        except ValueError as e:
            logging.warning(e)
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred while retrieving student details: {e}")
            return None

    def get_course_details(self, course_code):
        try:
            course = self.courses.get(course_code)
            if course:
                return course.course_details()
            else:
                raise ValueError(f"Course with code {course_code} not found")
        except ValueError as e:
            logging.warning(e)
            return None
        except Exception as e:
            logging.error(f"An unexpected error occurred while retrieving course details: {e}")
            return None

# Create course instances
python_course = Course(name="Python Programming", duration="3 months", fee="$500")
java_course = Course(name="Java Programming", duration="4 months", fee="$600")
aws_course = Course(name="AWS Certified Solutions Architect", duration="6 months", fee="$800")

# Create student instances
student1 = Student(firstname="Saurav", lastname="Gautam", email="sauravgautam@example.com", mobile_no="1234567890", age=21, qualification="bsc")
student2 = Student(firstname="Nikita", lastname="Awalkar", email="nikita@example.com", mobile_no="0987654321", age=22, qualification="btch")

# Manage enrollments
manager = EnrollmentManager()
manager.add_students(student1)
manager.add_students(student2)
manager.add_courses(python_course)
manager.add_courses(java_course)
manager.add_courses(aws_course)

# Enroll students in courses
manager.enroll_student_in_course(student1.id, python_course.code)
manager.enroll_student_in_course(student2.id, java_course.code)

# Display student and course details
print(manager.get_student_details(student1.id))
print(manager.get_course_details(python_course.code))

# Withdraw a student from a course
manager.withdraw_student_from_course(student1.id, python_course.code)
print(manager.get_student_details(student1.id))
