"""
dry run:
n = 2
f([], 2, [])
["{"]
f(["{"], 2, [])
[{, {]
f([{, {], 2, [])
[{, {, {]
"""


def recurse(arr: list, n: int, parenthesis_combos: set):
    if len(arr) == n*2:
        return parenthesis_combos.add("".join(arr[:]))
    
    
    arr.append("}")
    recurse(arr, n, parenthesis_combos)
    
    arr.pop()
    arr.append("{")
    recurse(arr, n, parenthesis_combos)
    arr.pop()
    return
    
def validate_parenthesis(parenthesis):
    stack = []
    closeToOpen = {')':'(', '}':'{', ']':'['}
    for c in parenthesis:
        if c in closeToOpen:
            if stack != [] and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    return True if stack == [] else False

def generate_n_pairs_balanced_parenthesis(n: int) -> str:
    parenthesis_combos = set()
    recurse(["{"], n, parenthesis_combos)
    res = []
    for combo in parenthesis_combos:
        if validate_parenthesis(combo):
            res.append(combo)
    return res
    
    

res = generate_n_pairs_balanced_parenthesis(4)
print(res)