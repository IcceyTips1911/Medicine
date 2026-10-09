def syschecker():
	return

import subprocess
import sys
from pathlib import Path


def find_bash_script():
    current_dir = Path(__file__).resolve().parent

    # Search this directory and all parent directories.
    for directory in (current_dir, *current_dir.parents):
        candidate = directory / "syschecker.sh"

        if candidate.is_file():
            return candidate

    return None


def syschecker():
    bash_script = find_bash_script()

    if bash_script is None:
        print("Error: Could not find syschecker.sh.", file=sys.stderr)
        return 1

    print(f"\nStarting system checker: {bash_script}\n")

    try:
        # Run in the foreground so output appears in the dashboard terminal.
        result = subprocess.run(
            ["bash", str(bash_script)],
            check=False,
        )

        return result.returncode

    except KeyboardInterrupt:
        print("\nSystem checker interrupted.")
        return 130

    except OSError as error:
        print(f"Error running system checker: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(syschecker())
