import lookup
import projectTools

class Project:

    def __init__(self, owner_op):
        self.Owner_op = owner_op
        print(f'Project Init at | {projectTools.MyTime.TD_now()}')

    def Touch_start(self):
        print('Running Touch Start | Project')
        lookup.DATA.Touch_start()
        lookup.OUTPUT.Touch_start()

    def Promoted_project_method(self):
        ...