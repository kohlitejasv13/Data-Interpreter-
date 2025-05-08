from parser import parser
from evaluator import evaluate

if __name__ == "__main__":
    print("Welcome to the Data Interpreter!")
    print("Enter an arithmetic expression. Type 'exit' to quit.")

    while True:
        expr = input("> ").strip()
        if expr.lower() == 'exit':
            break
        if not expr:
            print("[Input Error] Please enter a valid expression.")
            continue
        try:
            ast = parser.parse(expr)
            if ast is None:
                print("[Parse Error] Invalid or empty expression.")
                continue
            result = evaluate(ast)
            print("Result:", result)
        except ZeroDivisionError as zde:
            print(zde)
        except Exception as e:
            print(f"[Runtime Error] {e}")
