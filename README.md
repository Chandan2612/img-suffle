# 📂 Image Shuffler Script

A simple Python script that collects images from multiple folders, shuffles them randomly, and copies them into a single folder with sequential naming — without any quality loss.

---

## 🚀 Features

- Reads images from multiple subfolders
- Randomly shuffles all images
- Renames images in sequence (`1.jpg`, `2.png`, ...)
- Generates a mapping file (`mapping.txt`)
- No quality loss (uses direct file copy)

---

## ▶️ Usage

### 1. Make sure Python is installed

```bash
python --version
```

### 2. Add your images

Place your images inside subfolders of an `images` folder.

### 3. Run the script

```bash
python script.py
```

---

## ⚙️ Configuration

Change this line in the script if you want a different folder:

```python
root_folder = "./images"
```

---

## 🧠 How It Works

- The script scans all subfolders inside the main folder
- Collects all valid image files (`.jpg`, `.jpeg`, `.png`, `.webp`)
- Shuffles them randomly using `random.shuffle()`
- Copies them into `final_output` with new sequential names
- Saves a `mapping.txt` file to track original → new file names

---

## 📁 Output

All processed images will be saved in:

```
images/final_output/
```

---
