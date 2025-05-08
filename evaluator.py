# evaluator.py

def evaluate(node):
    if node is None:
        return None

    if isinstance(node, int) or isinstance(node, float):
        return node

    if node.__class__.__name__ == 'Num':
        return node.value

    elif node.__class__.__name__ == 'BinOp':
        left_val = evaluate(node.left)
        right_val = evaluate(node.right)

        if node.op == '+':
            return left_val + right_val
        elif node.op == '-':
            return left_val - right_val
        elif node.op == '*':
            return left_val * right_val
        elif node.op == '/':
            if right_val == 0:
                raise ZeroDivisionError("[Evaluation Error] Division by zero")
        return left_val / right_val

    elif node.__class__.__name__ == 'Neg':
        return -evaluate(node.expr)

    else:
        raise Exception("Unknown AST node type")
