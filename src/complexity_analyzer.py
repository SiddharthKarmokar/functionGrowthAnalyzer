import ast

class TimeComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 0
        self.logarithmic_count = 0

    def visit_FunctionDef(self, node):
        self.generic_visit(node)

    def visit_For(self, node):
        # Each 'for' loop contributes O(n) to the complexity
        self.complexity += 1
        self.generic_visit(node)

    def visit_While(self, node):
        # Each 'while' loop contributes O(n)
        self.complexity += 1
        self.generic_visit(node)

    def visit_If(self, node):
        self.generic_visit(node)

    def visit_Call(self, node):
        # Check for specific function calls that are known to have logarithmic complexity
        if isinstance(node.func, ast.Name) and node.func.id in {"sort", "sorted"}:
            self.logarithmic_count += 1
        self.generic_visit(node)

    def visit_BinOp(self, node):
        # Binary operations (e.g., +, -, *, /) are O(1)
        self.generic_visit(node)

    def visit_ListComp(self, node):
        # List comprehensions can be considered as O(n) in complexity
        self.complexity += 1
        self.generic_visit(node)

    def visit_Expr(self, node):
        self.generic_visit(node)

    def visit_Return(self, node):
        self.generic_visit(node)

    def visit_Call(self, node):
        # Recognize recursive calls to the same function
        if isinstance(node.func, ast.Name):
            self.generic_visit(node)

    def visit(self, node):
        super().visit(node)
        return self.complexity, self.logarithmic_count

def estimate_time_complexity(code):
    try:
        # Parse the code into an AST
        tree = ast.parse(code)
        analyzer = TimeComplexityAnalyzer()
        complexity, log_count = analyzer.visit(tree)

        # Determine the final complexity notation
        if log_count > 0:
            if complexity > 0:
                return f"O(n log n)"  # Adjusting for logarithmic contribution
            else:
                return "O(log n)"  # Just logarithmic complexity
        else:
            if complexity > 0:
                return f"O(n^{complexity})"
            else:
                return "O(1)"  # No complexity detected
    except Exception as e:
        return f"Error analyzing code: {e}"

if __name__ == "__main__":
    file_path = 'function_code.txt'  # Path to the input file

    try:
        with open(file_path, 'r') as file:
            function_code = file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit()

    result = estimate_time_complexity(function_code)
    print("Estimated Time Complexity:", result)
