import sympy as sp

def complexity_estimator(func):
    if func == sp.Symbol('n'):
        return "O(n)"
    elif func == sp.log(sp.Symbol('n')):
        return "O(log n)"
    elif func == sp.Symbol('n')**2:
        return "O(n^2)"
    # Add more rules or heuristics for common cases
    else:
        return "Complexity not easily identifiable"
