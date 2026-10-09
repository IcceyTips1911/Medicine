def syschecker():
	return

import os
import shutil
import signal
import subprocess
import sys

# 1. Search for the script dynamically using the system PATH
script_name = "syschecker.sh"
script_path = shutil.which(script_name)

if not script_path:
    print(f"Error: '{script_name}' could not be found anywhere in your system PATH.")
    print("Please make sure the script is executable (chmod +x) and moved to a PATH directory.")
    sys.exit(1)

print(f"Located script at: {script_path}")
print("Launching background monitor...")

# 2. Launch the script using the dynamically discovered path
process = subprocess.Popen(
    ["bash", script_path],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    preexec_fn=os.setpgrp  # Groups bash and all its child tasks together
)

try:
    # Read the output line by line as the bash script generates it
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break  # Script exited unexpectedly
        if output:
            print(output.strip())
            sys.stdout.flush()  # Force Python to print immediately
            
except KeyboardInterrupt:
    print("\nStopping Python monitor and cleaning up background processes...")
    try:
        # Send SIGTERM to the entire process group
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
    except ProcessLookupError:
        pass  # Process already exited on its own
