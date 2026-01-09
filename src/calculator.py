class Calculator :
    # return the sum between 2 operands
    def mysum(self, first_operand, second_operand):
        return first_operand + second_operand

    def mymean(self, *argv) :
        n = len(argv)
        if n == 0 :
            return 0
        return sum(argv) / n
