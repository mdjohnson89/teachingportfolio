from Student import Student
import student_mod

student_1 = Student('Johnson', 'Matt')
student_2 = Student('Flay', 'Bobby')

student_1.set_classes(['English', 'Math', 'Astronomy'])
student_1.print_record()

print(student_2.id_num)

student_1.remove_class('Math')
student_1.print_classes()
