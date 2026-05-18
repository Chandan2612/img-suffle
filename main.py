import os
import random
import shutil

# ==============================
# PATH (your images folder) 
# ==============================
root_folder = "./images"

# Output folder
output_folder = os.path.join(root_folder, "final_output")

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# ==============================
# Step 1: Collect all images
# ==============================
all_images = []

for folder in os.listdir(root_folder):
    folder_path = os.path.join(root_folder, folder)

    if os.path.isdir(folder_path) and folder != "final_output":

        for file in os.listdir(folder_path):
            if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                full_path = os.path.join(folder_path, file)
                all_images.append(full_path)

# ==============================
# Step 2: Shuffle images
# ==============================
random.shuffle(all_images)

# ==============================
# Step 3: Copy in sequence
# ==============================
mapping = []

for i, img_path in enumerate(all_images, start=1):

    ext = os.path.splitext(img_path)[1]  # keeps original extension
    new_name = f"{i}{ext}"

    dest_path = os.path.join(output_folder, new_name)

    shutil.copy2(img_path, dest_path)  # NO QUALITY LOSS

    mapping.append(f"{img_path} --> {dest_path}")

# ==============================
# Step 4: Save mapping
# ==============================
mapping_file = os.path.join(output_folder, "mapping.txt")

with open(mapping_file, "w") as f:
    for line in mapping:
        f.write(line + "\n")

print("✅ Done!")
print(f"📁 Output: {output_folder}")
