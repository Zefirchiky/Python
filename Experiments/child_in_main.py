import os

MAIN_DIR = "C:\AllArtem\games"
SAVE_IN = "C:\AllArtem\games\Screenshots"

i = 1

i = int(os.path.splitext(os.listdir(SAVE_IN)[-2])[0])

for root, dirs, files in os.walk(MAIN_DIR):
    for f in files:
        if (f.startswith(("screenshot", "ScreenShot_")) or root[-4:] == "TEMP"):
                    ext = os.path.splitext(f)[-1]
                    i += 1
                    old_path = os.path.join(root, f)
                    new_path = os.path.join(SAVE_IN, f"{i:06d}{ext}")

                    os.rename(old_path, new_path)
