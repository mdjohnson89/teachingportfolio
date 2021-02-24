student_1 = {
    'name': 'Joel Embiid', 
    'id_num': '01234', 
    'grad_year': 2021 , 
    'courses': ['English', 'Math', 'Science']}

student_2 = {
    'name': 'Ben Simmons', 
    'id_num': '01235', 
    'grad_year': 2021, 
    'courses': ['Spanish', 'Math', 'Art']}


students = {'student_a' : {
    'name': 'Joel Embiid', 
    'id_num': '01234', 
    'grad_year': 2021 , 
    'courses': ['English', 'Math', 'Science']},
    
    'student_b' : {
    'name': 'Ben Simmons', 
    'id_num': '01235', 
    'grad_year': 2021, 
    'courses': ['Spanish', 'Math', 'Art']}
    }

print(students['student_a']['courses'][0])