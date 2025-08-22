List_passanger = []

class Pass:
    global List_passanger

    def __init__(self,ID,Name):

        self.ID = ID
        self.Name = Name

        List_passanger.append(self)

appID = 1
P = 'p'+"1"


try:
    for passanger in List_passanger:
        if passanger.ID == appID:
            P=passanger
        break
except:
    pass
print(P.Name)



