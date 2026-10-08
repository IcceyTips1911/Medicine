import subprocess
import sys

# Launch the infinite loop script in the background
process = subprocess.Popen(
    ["bash", "/home/landon/repo/throwaway_practice/syschecker.sh"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

try:
    # Read the output line by line as the bash script generates it
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break # Script exited unexpectedly
        if output:
            print(output.strip())
            sys.stdout.flush() # Force Python to print immediately
            
except KeyboardInterrupt:
    print("\nStopping Python monitor...")
    process.terminate() # Cleanly kills the background Bash script
