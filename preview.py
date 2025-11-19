import os

print("=== PREVIEW OF FILES THAT WOULD BE UPLOADED ===\n")

for folder in os.listdir("."):
    # Skip non-folders
    if not os.path.isdir(folder):
        continue

    # Skip irrelevant folders
    if folder in [".git", ".vscode", "Solutions"]:
        continue

    folder_path = os.path.join(".", folder)
    files_to_upload = []

    # Look inside the folder
    for fname in os.listdir(folder_path):
        # main.cpp
        if fname == "main.cpp":
            files_to_upload.append(os.path.join(folder, fname))

        # data*.in
        if fname.startswith("data") and fname.endswith(".in"):
            files_to_upload.append(os.path.join(folder, fname))

    if files_to_upload:
        print(f"{folder}/")
        for f in files_to_upload:
            print(f"   - {f}")
        print()
