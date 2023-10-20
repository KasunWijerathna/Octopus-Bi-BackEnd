# runserver.py
import subprocess

# Run the import data command
subprocess.run(["python", "manage.py", "importdata"])

# Start the development server
subprocess.run(["python", "manage.py", "runserver"])
