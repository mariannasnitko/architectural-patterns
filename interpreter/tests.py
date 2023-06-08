import unittest
from interpreter import Context, TerminalExpression, NonterminalExpression, Parser


# Unit Tests
class InterpreterTest(unittest.TestCase):
    def test_interpreter(self):
        context = Context("input data")
        terminal_expression = TerminalExpression()
        nonterminal_expression = NonterminalExpression(terminal_expression)
        parser = Parser(nonterminal_expression)

        # Test interpretation
        parser.parse(context)
        nonterminal_expression.interpret(context)
        terminal_expression.interpret(context)

        # Assert the results of interpretation
        # ...


if __name__ == '__main__':
    unittest.main()
