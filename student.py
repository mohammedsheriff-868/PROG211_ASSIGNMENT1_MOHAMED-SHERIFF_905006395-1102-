"""
Student Registration System"""


class Course:
    """A course a student can register for."""

    def __init__(self, code, title, credits):
        self.code = code
        self.title = title
        self.credits = credits

    def display_info(self):
        return f"{self.code} - {self.title} ({self.credits} credits)"


class Student:
    """A registered student."""

    total_students = 0  # class-level attribute

    def __init__(self, student_id, name, programme, year):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        self.year = year
        self.courses = []  # Course objects the student has registered for
        Student.total_students += 1

    # ---- Instance methods (Task 3) ----
    def update_record(self, name=None, programme=None, year=None):
        """Update any of the student's details."""
        if name:
            self.name = name
        if programme:
            self.programme = programme
        if year:
            self.year = year

    def register_course(self, course):
        """Interaction between objects: Student <-> Course."""
        if course in self.courses:
            return False
        self.courses.append(course)
        return True

    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | "
              f"Programme: {self.programme} | Year: {self.year}")
        if self.courses:
            for c in self.courses:
                print(f"    - {c.display_info()}")
        else:
            print("    (no courses registered)")

    # ---- Class method (Task 3) ----
    @classmethod
    def from_string(cls, data):
        """Create a Student from 'ID,Name,Programme,Year'."""
        student_id, name, programme, year = [p.strip() for p in data.split(",")]
        return cls(student_id, name, programme, int(year))

    @classmethod
    def get_total_students(cls):
        return cls.total_students


# ---- Task 2: ONE data structure - a dictionary keyed by student ID ----
students = {}


def add_student(student):
    """Add a student to the dictionary."""
    if student.student_id in students:
        print(f"A student with ID {student.student_id} already exists.")
        return False
    students[student.student_id] = student
    print(f"Student {student.name} registered successfully.")
    return True


def display_students():
    """Loop through the dictionary and display all records."""
    if not students:
        print("No students registered yet.")
        return
    for student in students.values():
        student.display_info()
        print()


def main():
    # Sample courses (kept simple and non-sensitive)
    courses = {
        "ICT101": Course("ICT101", "Introduction to Programming", 3),
        "ICT102": Course("ICT102", "Database Systems", 3),
        "ICT103": Course("ICT103", "Networking Fundamentals", 3),
    }

    while True:
        print("\n=== Student Registration System ===")
        print("1. Add student")
        print("2. Display all students")
        print("3. Update student record")
        print("4. Register student for a course")
        print("5. Add student from text (ID,Name,Programme,Year)")
        print("6. Show total students")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                sid = input("Student ID: ").strip()
                name = input("Name: ").strip()
                programme = input("Programme: ").strip()
                year = int(input("Year: "))
                add_student(Student(sid, name, programme, year))
            except ValueError:
                print("Year must be a number.")
        elif choice == "2":
            display_students()
        elif choice == "3":
            sid = input("Student ID to update: ").strip()
            if sid in students:
                name = input("New name (blank to keep): ").strip()
                prog = input("New programme (blank to keep): ").strip()
                year = input("New year (blank to keep): ").strip()
                students[sid].update_record(
                    name or None, prog or None, int(year) if year.isdigit() else None)
                print("Record updated.")
            else:
                print("Student not found.")
        elif choice == "4":
            sid = input("Student ID: ").strip()
            print("Available courses:")
            for c in courses.values():
                print("  ", c.display_info())
            code = input("Course code: ").strip().upper()
            if sid in students and code in courses:
                if students[sid].register_course(courses[code]):
                    print("Course registered.")
                else:
                    print("Already registered for that course.")
            else:
                print("Invalid student ID or course code.")
        elif choice == "5":
            try:
                add_student(Student.from_string(input("Enter: ")))
            except ValueError:
                print("Format must be: ID,Name,Programme,Year")
        elif choice == "6":
            print("Total students:", Student.get_total_students())
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
