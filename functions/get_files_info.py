import os

def get_files_info(working_directory, directory="."):
    full_path= os.path.join(working_directory, directory)
    abs_working = os.path.abspath(working_directory)
    abs_target = os.path.abspath(full_path)

    abs_working_with_sep = abs_working if abs_working.endswith(os.sep) else abs_working + os.sep
    

    if not (abs_target == abs_working or abs_target.startswith(abs_working_with_sep)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_target):
        return f'Error: "{directory}" is not a directory'
    
    try:
        entries = os.listdir(abs_target)
        lines = []
    
        for name in entries:
            p = os.path.join(abs_target, name)
            size = os.path.getsize(p)
            is_dir = os.path.isdir(p)
            lines.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}')
        return "\n".join(lines)
    except Exception as e:
        return f'Error: {e}'
    

    

        

