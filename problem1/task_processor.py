def change_case(text):
    return text.swapcase()

def evaluate_expression(expr):
    try:
        return str(eval(expr))
    except:
        return "Invalid expression"

def reverse_string(text):
    return text[::-1]

def process_task(data):
    try:
        task_type, content = data.split(':', 1)
        
        if task_type == '1':
            return change_case(content)
        elif task_type == '2':
            return evaluate_expression(content)
        elif task_type == '3':
            return reverse_string(content)
        else:
            return "Invalid task type"
    except:
        return "Error processing task"
