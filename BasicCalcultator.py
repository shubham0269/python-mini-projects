

# ================================================ Basic  Calculaltor ===============================================================

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

while True:
    user_input = input("Enter an expression to calculate (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    result = evaluate_expression(user_input)
    print("Result:", result)
    
    
