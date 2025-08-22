class Pass:
    List_passanger = []
    ID = 1

    def __init__(self):
        Name = input('Enter Name: ')
        self.ID = Pass.ID
        Pass.ID+= 1
        self.Name = Name
        Pass.List_passanger.append(self)
        print('Your ID:',self.ID)

    def Details():

        for i in Pass.List_passanger:
            print('ID: ',i.ID,'Name: ',i.Name)
    
    def Get_Obj():
        ID = int(input('Enter Your ID: '))
        for obj in Pass.List_passanger:
            if obj.ID == ID:
                return obj




def Rename():
    for obj in Pass.List_passanger:
        if obj.ID == ID:
            obj.Name = input('Enter new Name: ')
i =0
while i!=3:
    obj = Pass()
    i+=1

ID = int(input('Enter ID'))

Rename()

Pass.Details()


