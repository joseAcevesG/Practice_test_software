import subprocess


def execute_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise e
