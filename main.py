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
folder_counts = {}
supported_extensions = (".jpg", ".jpeg", ".png", ".webp")

for current_folder, folders, files in os.walk(root_folder):
    folders[:] = [folder for folder in folders if folder != "final_output"]

    image_count = 0

    for file in files:
        if file.lower().endswith(supported_extensions):
            full_path = os.path.join(current_folder, file)
            all_images.append(full_path)
            image_count += 1

    if image_count > 0:
        folder_counts[current_folder] = image_count

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

# ==============================
# Step 5: Save process log
# ==============================
log_file = os.path.join(output_folder, "process_log.txt")

with open(log_file, "w") as f:
    f.write("Image Shuffler Process Log\n")
    f.write("==========================\n\n")
    f.write(f"Root folder: {root_folder}\n")
    f.write(f"Output folder: {output_folder}\n")
    f.write(f"Total folders with images: {len(folder_counts)}\n")
    f.write(f"Total images found: {len(all_images)}\n")
    f.write(f"Total images copied to output: {len(mapping)}\n\n")
    f.write("Images found by folder:\n")

    for folder_path in sorted(folder_counts):
        relative_folder = os.path.relpath(folder_path, root_folder)
        display_folder = root_folder if relative_folder == "." else os.path.join(root_folder, relative_folder)
        f.write(f"{display_folder}: {folder_counts[folder_path]}\n")

print("Done!")
print(f"Output: {output_folder}")
print(f"Log: {log_file}")
