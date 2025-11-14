import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:    
        full_path = os.path.join(working_directory, file_path)
        abs_working = os.path.abspath(working_directory)
        abs_working_with_sep = abs_working if abs_working.endswith(os.sep) else abs_working + os.sep

        abs_target = os.path.abspath(full_path)

        if not abs_target.startswith(abs_working_with_sep):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_target):
            return f'Error: File "{file_path}" not found.'
        
        if not abs_target.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        try:
            cmd = ["python", abs_target] + args
            result = subprocess.run(
                cmd,
                capture_output=True, 
                cwd=working_directory, 
                timeout=30,
                check=True,
                text=True,
            )
            if result.stdout == "" and result.stderr == "":
                return "No output produced."
            return f'STDOUT: {result.stdout}\nSTDERR: {result.stderr}'
        
        except subprocess.CalledProcessError as non_zero:
            return f'STDOUT: {non_zero.stdout}\nSTDERR: {non_zero.stderr}\nProcess exited with code {non_zero.returncode}'

    except Exception as e:
        return f"Error: executing Python file: {e}"
