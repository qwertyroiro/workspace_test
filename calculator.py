import sys

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def calculate(a, b):
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Division: {a / b}")

if len(sys.argv) != 3:
    print("Please provide exactly two arguments.")
    sys.exit(1)

arg1, arg2 = sys.argv[1], sys.argv[2]

if not is_number(arg1) or not is_number(arg2):
    print("数字ではありません")
    sys.exit(1)

num1, num2 = float(arg1), float(arg2)
calculate(num1, num2)
