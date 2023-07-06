import abc
class test:
    @abc.abstractmethod
    def student(Self):
        pass
    @abc.abstractmethod
    def student1(Self):
        pass
    @abc.abstractmethod
    def student2(self):
        pass
#-----------------------------------------------
class student_detail(test):
    def student_detail(self):
        return "hi"
    def student_ass(self):
        return "hello"
    
#--------------------------------------------    
class data(test):
    def student_details(self):
        return "data science masters"
    def student_ass(self):
        return "details of assignment"
data1=data()
data1.student_ass()
