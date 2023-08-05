class abc:
    def __init__(self,course_name,course_price):
        
        self.__course_name=course_name
        self.__course_price=course_price
    @property
    def course_price_access(self):
        return self.__course_price
    @course_price_access.setter
    def course_price_set(self,price):
        if price<=2000:
            pass
        else:
            self.__course_price=price
    @course_price_access.deleter
    def delete_course_price(self):
        del self.__course_price
a=abc("ashray",2000)
a._abc__course_price
a._abc__course_name
a.course_price_access
a.course_price_set=400
del a.delete_course_price
