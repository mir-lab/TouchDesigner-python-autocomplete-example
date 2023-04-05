import lookup

class Project:

    def __init__(self, owner_op):
        self.Owner_op = owner_op
        print('Project Init')

    def Touch_start(self):
        print('Running Touch Start | Project')
        lookup.DATA.Touch_start()
        lookup.OUTPUT.Touch_start()

    def Promoted_project_method(self):
        ...