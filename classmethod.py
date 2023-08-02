class abc:
    
    mobile_num=455345468
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    @classmethod
    def change(cls,mobile):
        abc.mobile_num=mobile
    @classmethod
    def detail(cls,name,phone):
        return cls(name,phone)
    def student(Self):
        print(self.name,self,phone)
pw=abc.detail("ashu",58754)
pw.name
