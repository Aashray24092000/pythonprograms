class class1:
     def test_class1(self):
            return "this is ashray"
class class2(class1):
    def test_class2(self):
        return "welcome"
class class3(class2):
    def test_class3(self):
        return "hihihi" 
class class4(class3):
    def test_class4(self):
        return "hello sir"
obj1=class4()
obj1.test_class3()
