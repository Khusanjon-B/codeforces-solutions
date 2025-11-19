import os
import subprocess

print("=== UPLOADING FILES ===\n")

for folder in os.listdir("."):
    if not os.path.isdir(folder):
        continue

    if folder in [".git", ".vscode", "Solutions"]:
        continue

    folder_path = os.path.join(".", folder)
    files_to_upload = []

    # Collect only approved files
    for fname in os.listdir(folder_path):
        if fname == "main.cpp":
            files_to_upload.append(os.path.join(folder, fname))
        elif fname.startswith("data") and fname.endswith(".in"):
            files_to_upload.append(os.path.join(folder, fname))

    if not files_to_upload:
        continue

    print(f"Preparing upload for: {folder}")
    print("Files:")
    for f in files_to_upload:
        print("   -", f)

    # Add only the selected files
    subprocess.run(["git", "add"] + files_to_upload, check=True)

    # Commit
    commit_msg = f"Add solution for {folder}"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)

    # Push
    subprocess.run(["git", "push"], check=True)

print("\nDone!")