class Student():

    id_counter = 0

    def __init__(self, last, first):
        '''Create a new student object. Requires last name, first name as parameters'''
        Student.id_counter += 1

        self.first_name = first
        self.last_name = last
        self.id_num = Student.id_counter
        self.classes = []
    
    def set_classes (self, classes_list):
        '''Takes a list of classes as an argument and updates the default empty list with that list'''
        self.classes = classes_list
    
    def add_class (self, class_name):
        self.classes.append(class_name)

    def remove_class (self, class_name):
        if class_name in self.classes:
            self.classes.remove(class_name)
        else:
            print(f'{self.first_name} is not enrolled in {class_name}. ')
    
    def print_classes(self):
        print('Currently enrolled in:\n')
        for classes in self.classes:
            print(classes)
    
    def print_record(self):
        print(f'First Name: {self.first_name}\nLast Name: {self.last_name}\nID#: {self.id_num}\n')
        self.print_classes()
