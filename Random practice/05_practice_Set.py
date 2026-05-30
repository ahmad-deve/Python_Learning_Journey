from random import randint
class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"ticket is booked in train  no {self.trainNo}. Train going to {fro} to {to}")
    def get_status(self):
        print(f"Train no is: {self.trainNo} is runing.")
    def to_Fare(self, fro, to):
        print(f"ticket is fare {self.trainNo} is the going to {fro} to {to} and is {randint(222,4444)}")
t = train(12364)
t.book("LHR","RYK")
t.get_status()
t.to_Fare("LHR","RYK")