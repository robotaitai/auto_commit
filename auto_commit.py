import subprocess
import time
import datetime
import os

def generate_code():
    """
    Generates (or updates) a Python file with a timestamp.
    """
    current_time = datetime.datetime.now().isoformat()
    code = f"""# Auto-generated code file
# Timestamp: {current_time}

def greet():
    print("Hello! The current time is: {current_time}")

if __name__ == "__main__":
    greet()
"""
    with open("auto_generated.py", "w") as f:
        f.write(code)
    print(f"[{datetime.datetime.now()}] Code generated in auto_generated.py")

def git_push(commit_message):
    """
    Stages changes, commits, and pushes to the remote repository.
    """
    try:
        # Stage all changes
        subprocess.run(["git", "add", "."], check=True)
        # Commit with the provided commit message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        # Push changes to the default remote branch (adjust 'main' if needed)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print(f"[{datetime.datetime.now()}] Changes pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        # Handle errors (e.g., if there's nothing to commit)
        print(f"[{datetime.datetime.now()}] Git command failed: {e}")

def main():
    # Interval in seconds (2 hours = 7200 seconds)
    interval = 7200

    while True:
        # Generate or update the code file
        generate_code()

        # Create a commit message with the current timestamp
        commit_message = f"Automated commit: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        git_push(commit_message)

        # Wait for the specified interval before running again
        print(f"Sleeping for {interval/3600} hours...\n")
        time.sleep(interval)

if __name__ == "__main__":
    # Optional: Change directory to your repository if needed
    # os.chdir("/path/to/your/repository")
    main()
