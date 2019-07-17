def push(item):
    stack.append(item)

def peak():
    if len(stack) != 0:
        return stack[-1]

def pop():
    if len(stack) != 0:
        item = stack.pop(-1)

        return item

# op(연산자), op1(피연산자), op2(피연산자)
def compute(op, op1, op2):
    if op == "*":
        return op1 * op2

    elif op == "/":
        return op1 / op2

    elif op == "+":
        return op1 + op2

    elif op == "-":
        return op1 - op2

# 수식 분리
def eval(exp):
    token_list = exp.split()

    for token in token_list:
        if token in '1234567890101112131415':
            push(int(token))
            print(stack)
        else:
            operand2 = pop()
            operand1 = pop()
            print("token :", token)
            res = compute(token, operand1, operand2)
            push(res)

    return pop()


stack = []


q = input(">> (x y +) ")
print(eval(q))