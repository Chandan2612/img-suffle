import os
import random
import shutil

# ==============================
# CHANGE THIS PATH
# ==============================
root_folder = "./images"
# Example:
# root_folder = r"C:\Users\chandan\Desktop\images"

# ==============================
# Step 1: Get all folders
# ==============================
folders = [
    os.path.join(root_folder, f)
    for f in os.listdir(root_folder)
    if os.path.isdir(os.path.join(root_folder, f))
]

# ==============================
# Step 2: Collect all images
# ==============================
all_images = []
folder_map = {}

for folder in folders:
    images = [
        os.path.join(folder, file)
        for file in os.listdir(folder)
        if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))
    ]

    folder_map[folder] = images
    all_images.extend(images)

# ==============================
# Step 3: Shuffle images globally
# ==============================
random.shuffle(all_images)

# ==============================
# Step 4: Redistribute
# ==============================
index = 0
new_map = {}

for folder in folder_map:
    count = len(folder_map[folder])
    new_map[folder] = all_images[index:index+count]
    index += count

# ==============================
# Step 5: Create temp folder
# ==============================
temp_root = os.path.join(root_folder, "swapped_output")

if not os.path.exists(temp_root):
    os.makedirs(temp_root)

# ==============================
# Step 6: Copy images (no quality loss)
# ==============================
mapping = []

for folder in new_map:

    folder_name = os.path.basename(folder)
    new_folder_path = os.path.join(temp_root, folder_name)

    os.makedirs(new_folder_path, exist_ok=True)

    for img_path in new_map[folder]:

        file_name = os.path.basename(img_path)
        dest_path = os.path.join(new_folder_path, file_name)

        shutil.copy2(img_path, dest_path)  # keeps quality + metadata

        mapping.append(f"{img_path}  -->  {dest_path}")

# ==============================
# Step 7: Save mapping file
# ==============================
mapping_file = os.path.join(temp_root, "mapping.txt")

with open(mapping_file, "w") as f:
    for line in mapping:
        f.write(line + "\n")

print("✅ Done!")
print(f"📁 Output folder: {temp_root}")
print(f"📄 Mapping file: {mapping_file}")
