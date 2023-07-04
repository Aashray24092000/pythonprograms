class data_science:
    def syllabus(self):
        print("hello")
class web_dev:
    def syllabus(Self):
        print("hello sir")
class net_dev:
    def syllabus(Self):
        print("hello sir good night")
def class_parcer(class_object):
    for i in class_object:
        i.syllabus()
data_science=data_science()
web_dev=web_dev()
net_dev=net_dev()
class_object=[data_science,web_dev,net_dev]
class_parcer(class_object)
