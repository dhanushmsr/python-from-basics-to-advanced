from abstract_class import password_check
class pass_operations(password_check):
    def pass_accept(self,password):
        if len(password)>8:
            print("the pass is valid and it is accepted")
        else:
            print("password is not valid re-enter the password")
        return super().pass_accept()
    def pass_match(self,password):
        if password=="dhanush@123":
            print("you are login successfully")
        else:
            print("Entered password is wrong")
        return super().pass_match()