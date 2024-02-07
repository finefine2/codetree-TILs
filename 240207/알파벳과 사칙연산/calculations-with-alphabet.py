arr = input()

Max = -1

def calculate(expression, values):
    result = values[expression[0]] 
    for i in range(1, len(expression), 2):
        op = expression[i]
        if op == '+':
            result += values[expression[i + 1]]
        elif op == '-':
            result -= values[expression[i + 1]]
        else:  # op == '*'
            result *= values[expression[i + 1]]

    return result

def cal(a, b, c, d, e, f):
    global Max
    values = {'a': a, 'b': b, 'c': c, 'd': d, 'e': e, 'f': f}  
    result = calculate(arr, values) 
    Max = max(Max, result)  

for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    for f in range(1, 5):
                        cal(a, b, c, d, e, f)

print(Max)



# # for i in range(len(a)):
# #     if a[i] == '-' or a[i] == '+' or a[i] == '*':


# from itertools import product

# def evaluate_expression(expr, values):
#     result = int(values[expr[0]])
#     for i in range(1, len(expr), 2):
#         op = expr[i]
#         if op == '+':
#             result += int(values[expr[i+1]])
#         elif op == '-':
#             result -= int(values[expr[i+1]])
#         else: # op == '*'
#             result *= int(values[expr[i+1]])
#     return result

# def maximize_expression(expr):
#     chars = {c for c in expr if c.isalpha()}
#     max_result = float('-inf')
    
#     # Generate all combinations of values for the characters
#     for combo in product(range(1, 5), repeat=len(chars)):
#         values = dict(zip(chars, combo))
#         result = evaluate_expression(expr, values)
#         max_result = max(max_result, result)
    
#     return max_result

# a = input()
# print(maximize_expression(a)) # Output: 12