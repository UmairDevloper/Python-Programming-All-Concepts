from random import randint

class Train:

# If we change "harry" to "sef" or "self" to "sef" there will be no change  bcz self is just a way to call the object 

    def __init__(sef, trainNo):
        sef.trainNo = trainNo

    def booking(harry, fro, to):
        print("Train no", harry.trainNo, "from", fro, "to", to, "is booked")

    def status(harry):
        print("Train no", harry.trainNo, "is running")

    def getFare(harry, fro, to):
        print("Fare from", fro, "to", to, "is", randint(500, 1000))

t = Train(236)
t.booking("Pune", "Mumbai")
t.status()
t.getFare("Pune", "Mumbai")



    