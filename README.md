# Student Record Management System

**Institution:** Limkokwing University of Creative Technology – Sierra Leone  
**Coursework:** Semester 03 Python OOP Assignment  
**Language:** Python 3 (standard library only)

## Project overview
A terminal-based educational prototype for adding, displaying, and searching basic student records. Two fictional records are loaded at startup. Data is held in memory and disappears when the program closes.

## Problem and objectives
Scattered notes can make student information difficult to find. This project demonstrates classes and objects, attributes and methods, a list and dictionary, an instance method, a `@classmethod`, and an optional tuple.

## Run the program
1. Install Python 3.10 or newer (recommended).
2. Open a terminal in this folder.
3. Run `python student_record_system.py` (or `python3 student_record_system.py`).
4. Choose an option from the menu. No third-party packages are required.

## OOP and data structures
- **Classes:** `Student` describes a student; `StudentRecordSystem` manages records.
- **Objects:** Each `Student(...)` is an instance of the `Student` class.
- **Attributes:** `student_id`, `name`, `programme`, `level`; `school_name` is a class attribute.
- **Instance method:** `display_details(self)` displays the attributes of one student object.
- **Class method:** `change_school_name(cls, new_name)` uses `@classmethod` to change the shared institution name during the current run.
- **List:** `self.students` holds all Student objects and is used to display records.
- **Dictionary:** `self.students_by_id` maps a normalized student ID to its Student object, allowing direct lookup and duplicate checking.
- **Optional tuple:** `Student.SUGGESTED_PROGRAMMES` is an immutable tuple of sample programme names, appropriate for a fixed set of suggestions.

## Example input/output
**Input** (select option 3):
```text
Choose an option: 3
Enter the student ID to search: LWK001
```
**Expected output:**
```text
Student found:
-----------------------------------
Student ID : LWK001
Name       : Student One
Programme  : Information Technology
Level      : Level 1
Institution: Limkokwing University – Sierra Leone
```
These are fictional demonstration records. Do not use sensitive or real student data in coursework screenshots.

## Digital Public Goods (DPG) alignment
This is a learning prototype and **is not certified as a Digital Public Good**. It demonstrates relevant design principles:
- **Open-source sharing:** source code can be shared publicly on GitHub; add a licence only if you have chosen one.
- **Inclusive/accessibility-minded:** simple text menu and no paid dependencies.
- **Privacy-respecting:** fictional sample data only; no sensitive information is requested.
- **Modular/reusable:** the Student class is separated from the record-management class.

## Test checklist
| Test | Action | Expected result |
|---|---|---|
| Display | Select `2` | Two sample records displayed |
| Search found | Select `3`, enter `LWK001` | Student One appears |
| Search missing | Search `LWK999` | Not-found message |
| Add unique | Add a new ID | Success message |
| Duplicate ID | Add `LWK001` again | Duplicate warning |
| Summary | Select `4` | Count and tuple values displayed |
| Class method | Select `5`, enter new institution | Institution name updates for current run |

## Execution screenshots
Capture your own screenshots of the running program on your computer, including: (1) main menu, (2) display-all output, (3) search output, and (4) summary/tuple output. On Windows, use `Win + Shift + S`. The included `sample_execution_output.png` is an illustrative image made from captured program output; your lecturer may require genuine screenshots from your own environment.

## GitHub submission and collaborator
Suggested repository name: `student-record-management-system`. Include `student_record_system.py`, `README.md`, and your screenshots. To upload after creating an empty GitHub repository:
```bash
git init
git add student_record_system.py README.md
git commit -m "Create student record management system"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
Replace the placeholder with your own repository URL. To add your lecturer: open the repository on GitHub → **Settings** → **Collaborators** (or **Collaborators and teams**) → **Add people** → enter the lecturer's GitHub username/email → send invitation. Use the details your lecturer gave you; do not guess their username.

## Limitations and conclusion
Records are not saved permanently and there is no login or access control, so this prototype must not be used for real student data. The project demonstrates two classes, objects, attributes, methods, a list, a dictionary, a class method, and the optional tuple. Future improvements could add database storage, tests, and authentication.
