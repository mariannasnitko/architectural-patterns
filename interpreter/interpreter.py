class Context:
    def __init__(self, input):
        self.input = input
        self.output = None


class AbstractExpression:
    def interpret(self, context):
        pass


class TerminalExpression(AbstractExpression):
    def interpret(self, context):
        # Interpret the terminal expression
        pass


class NonterminalExpression(AbstractExpression):
    def __init__(self, expression):
        self.expression = expression

    def interpret(self, context):
        # Interpret the nonterminal expression
        pass


class Parser:
    def __init__(self, expression):
        self.expression = expression

    def parse(self, context):
        # Generate the tree structure
        pass
