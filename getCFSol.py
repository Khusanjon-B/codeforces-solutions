import os
import shutil
import subprocess

# --------------------------------------
# CONFIG
# --------------------------------------

# Correct practice folder for your setup
PRACTICE_DIR = os.path.join("Solutions", "codeforces", "practice")

# Ensure practice directory exists
os.makedirs(PRACTICE_DIR, exist_ok=True)

print(f"Using practice folder: {PRACTICE_DIR}\n")

# Track which problems were added
added_files = []

# --------------------------------------
# COPY SOLUTIONS
# --------------------------------------

for item in os.listdir("."):
    # Skip non-directories
    if not os.path.isdir(item):
        continue

    # Skip these folders
    if item in ["Solutions", ".vscode", "__pycache__"]:
        continue

    folder_path = os.path.join(item)
    main_cpp_path = os.path.join(folder_path, "main.cpp")

    # If folder contains a main.cpp
    if os.path.isfile(main_cpp_path):
        output_file = os.path.join(PRACTICE_DIR, f"{item}.cpp")

        # Skip duplicates
        if os.path.exists(output_file):
            print(f"⏭️  Skipping {item}: already exists")
            continue

        # Copy file
        shutil.copyfile(main_cpp_path, output_file)
        added_files.append(item)
        print(f"✔ Copied {item}/main.cpp → {output_file}")

# --------------------------------------
# GIT COMMIT + PUSH
# --------------------------------------

if not added_files:
    print("\nNo new solutions to commit. Done!")
    exit(0)

# Stage changes (git add .)
subprocess.run(["git", "add", "."], check=True)

# Create commit message
commit_message = "Add Codeforces solutions: " + ", ".join(added_files)

# Commit
subprocess.run(["git", "commit", "-m", commit_message], check=True)

print(f"\n✔ Created commit: \"{commit_message}\"")

# Push
print("Pushing to GitHub...")
subprocess.run(["git", "push"], check=True)

print("\n🎉 All done! Solutions copied, committed, and pushed successfully!")