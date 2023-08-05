class abc:
    def student_details(self,name,mail_id):
        print(name,mail_id)
    @staticmethod
    def mentor_mail_id(mail_id_mentor):
        print(mail_id_mentor)
    @staticmethod
    def mentor_class(list_mentor):
        abc.mentor_mail_id(["ashu@","ashuu@"])
        print(list_mentor)
    @classmethod
    def class_name(cls):
        cls.mentor_class(["ashray","ashu"])
    def mentor(self,mentor_list):
        print(mentor_list)
