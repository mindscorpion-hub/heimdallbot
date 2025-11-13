import os

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_working = os.path.abspath(working_directory)
        abs_working_with_sep = abs_working if abs_working.endswith(os.sep) else abs_working + os.sep

        abs_target = os.path.abspath(full_path)

        if not os.path.exists(abs_target):
            os.makedirs(os.path.dirname(abs_target), exist_ok=True)
            

        if not (abs_target == abs_working or abs_target.startswith(abs_working_with_sep)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        with open(abs_target, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path} ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {e}'

