class NegativeAgeError(Exception):
    pass
class VotingRightsError(Exception):
    def voter_age(self,age):
        self.age=age
        if self.age<0:
            raise NegativeAgeError (f"Age cannot be negative you entered as {self.age}")
        elif self.age<=18 :
            raise VotingRightsError (f"Voting can only been done after 18 years of age but your age is only {self.age}")
try:
    age=float(input("enter your age: "))
    obj=VotingRightsError()
    obj.voter_age(age)
except (NegativeAgeError,VotingRightsError,ValueError) as all:
    print(all)
else:
    print("you are eligible to vote ")