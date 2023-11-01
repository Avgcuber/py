class parent:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        
class child(parent):
    def __init__(self,first_name,last_name,age,aadhar_card_no):
        parent.__init__(self,first_name,last_name)
        self.age=age
        self.aadhar_card_no=aadhar_card_no
    def display_info(self):
        parent.display_info(self)
        print(self.age)
        print(self.aadhar_card_no)
        
class grandchild(child):
    def __init__(self,first_name,last_name,age,aadhar_card_no,address,pan_card_no):
        child.__init__(self,first_name,last_name,age,aadhar_card_no)
        self.address=address
        self.pan_card_no=pan_card_no
    def display_info(self):
        child.display_info(self)
        print(self.address)
        print(self.pan_card_no)
        
gc=grandchild("John", "Doe", 25, "1234567890", "123 Main St", "ABCDE1234F")
gc.display_info()     
