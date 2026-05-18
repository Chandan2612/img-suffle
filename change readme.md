# Changes Made

Updated `main.py` so it now reads images from nested folders inside the `images` folder.

Before this change, the script only checked one folder level:

```text
images/
  folder/
    image.jpg
```

Now it works with deeper folder structures too:

```text
images/
  folder/
    subfolder/
      image.jpg
```

The script still skips `images/final_output` so already processed output files are not collected again.

Main code change:

- Replaced `os.listdir()` folder scanning with `os.walk()`.
- Kept the same supported image types: `.jpg`, `.jpeg`, `.png`, `.webp`.
- Kept the same output behavior: shuffled images are copied into `images/final_output` with sequential names.

## Logging Added

Updated `main.py` to create a new log file:

```text
images/final_output/process_log.txt
```

This log shows:

- How many folders contained images.
- How many total images were found.
- How many total images were copied into `final_output`.
- How many images were found inside each source folder.

The script also prints the output folder path and log file path after it finishes.
