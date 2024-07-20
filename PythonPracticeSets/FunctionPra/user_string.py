input_string = "(((()()()()(())))"

def execute_code(lines):
    for line in lines:
        print(line)
        try:
            exec(line)
        except Exception as e:
            print(f"Error: {e}")

# Split the input string at every bracket to get individual lines of code
lines = input_string.split('(')
lines = [line.strip() for line in lines if line.strip()]

# Add back the brackets to each line
lines = ['(' + line + ')' for line in lines]

# Execute each line
execute_code(lines)
