import lookup

class Output:

    def __init__(self, owner_op):
        self.Owner_op = owner_op
        self.Custom_op1:lookup.CustomOp.CustomOp = owner_op.op("base_custom_op1")
        self.Custom_op2:lookup.CustomOp.CustomOp = owner_op.op("base_custom_op2")
        print('Output Init')

    def Touch_start(self):
        print('Running Touch Start | Output')
        self.Custom_op1.Touch_start()
        self.Custom_op2.Touch_start()

    def Promoted_output_method(self):
        ...
