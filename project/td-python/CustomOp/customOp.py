import lookup

class CustomOp:

    def __init__(self, owner_op):
        self.Owner_op = owner_op

        print(f'Custom Op Init | {owner_op.name}')

    def Touch_start(self):
        print('Running Touch Start | Custom Op')

    def Promoted_custom_method(self):
        ...
