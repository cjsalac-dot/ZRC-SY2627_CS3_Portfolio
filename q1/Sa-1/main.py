class AssignmentSubmission:
    def __init__(self, student_name: str, student_id: str, assignment_title: str, due_date: str):
        self.student_name = student_name
        self.student_id = student_id
        self._student_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = False
        self.__grade = 0
        self.__submitted_files = []

    def __validate_grade(self, score: float):
        return f"Student({self.grade})"

    def __check_submission_status(self):
        if self.__is_submitted is False:
            print("Missing an assignment")
        else:
            print("No missing assignment")

    def _is_duplicate(self, filename: str):
        seen = set()
        for filename in self.__submitted_files:
            if filename in seen:
                print(f"There is a duplicated file: {filename}")
            else:
                seen.add(filename)

    def add_file(self, filename: str):
        if filename not in self.__submitted_files:
            self.__submitted_files.append(filename)
            print(f"[Success] File '{filename}' added for {self.student_name}.")
        else:
            print(f"[Success] File '{filename}' already exists for {self.student_name}.")

    def remove_file(self, filename: str):
        if self.__grade is not None:
            print(f"[Warning] Cannot remove files after grading for {self.student_name}.")
            return
        if filename in self.submitted_files:
            self.__submitted_files.remove(filename)
            print(f"[Success] File '{filename}' removed for {self.student_name}.")
        else:
            print(f"[Error] File '{filename}' not found for {self.student_name}.")
        
    def assign_grade(self, score: float):
        if not self.__submitted_files:
            print(f"[Warning] No files submitted. Cannot assign grade for {self.student_name}.")
            return
        self.__grade = score
        print(f"[Success] Grade {score} assigned to {self.student_name}.")
        

    def get_grade(self):
        return self.__grade

    def view_files(self):
        if not self.__submitted_files:
            return "No files uploaded"
        return ", ".join(self.__submitted_files)

    def get_status_report(self):
        return (
            f"ID: {self.student_id} |"
            f"ID: {self.student_name}"
            f"Status: {len(self.__submitted_files)} ({self.view_files()})"
            f"Grade: {self.get_grade()}\n"
        )




                    
print("--- INITIALIZING DROPBOX FOR STUDENTS ---")
student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-01-01" )
student2 = AssignmentSubmission(student_name="Adelle", student_id="pshs-1920-x", assignment_title="CS-103", due_date="2026-01-01")
student3 = AssignmentSubmission(student_name="Juan Dela Cruz", student_id="pshs-1033-x", assignment_title="CS-101", due_date="2026-01-01")
student4 = AssignmentSubmission(student_name="Maria Santos", student_id="pshs-1044-x", assignment_title="CS-101", due_date="2026-01-01")
student5 = AssignmentSubmission(student_name="Jose Reyes", student_id="pshs-1055-x", assignment_title="CS-101", due_date="2026-01-01")
print()

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Prevent Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")  # Should trigger private duplicate check
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")  # Blocked by grading system
print(f"Maria's Files: {student4.view_files()}\n")

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100) # Should fail because list is empty
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
                    

