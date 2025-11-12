import os
import config 

def get_file_content(working_directory, file_path):
    
    try:
        full_path = os.path.join(working_directory, file_path)
        abs_working = os.path.abspath(working_directory)
        abs_working_with_sep = abs_working if abs_working.endswith(os.sep) else abs_working + os.sep

        abs_target = os.path.abspath(full_path)
        
        if not (abs_target == abs_working or abs_target.startswith(abs_working_with_sep)):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(abs_target):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        with open(abs_target, "r") as f:
            if os.path.getsize(abs_target) > config.MAX_CHARS:
                file_contents = f.read(config.MAX_CHARS)
                too_long = f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
                return file_contents + too_long
            return f.read()

    except Exception as e:
        return f'Error: {e}'