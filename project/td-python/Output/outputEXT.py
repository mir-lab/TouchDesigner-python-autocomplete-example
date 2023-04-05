import lookup

class Output:

    def __init__(self, owner_op):
        self.Owner_op = owner_op

        print('Output Init')

    def Touch_start(self):
        print('Running Touch Start | Output')

    def Promoted_output_method(self):
        ...
