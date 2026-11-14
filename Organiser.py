import os
import shutil

home = os.path.expanduser("~")

downloads = os.path.join(home, "Downloads")
images_dir = os.path.join(downloads, "Images")
docs_dir = os.path.join(downloads, "Documents")
V_A_dir = os.path.join(downloads, "Video and Audio")
compressed_dir = os.path.join(downloads, "Compressed Files and Software Packages")

os.makedirs(images_dir, exist_ok = True)
os.makedirs(docs_dir, exist_ok = True)
os.makedirs(V_A_dir, exist_ok = True)
os.makedirs(compressed_dir, exist_ok = True)


for filename in os.listdir(downloads):
    source = os.path.join(downloads, filename)

    if not os.path.isfile(source):
        continue

    elif filename.lower().endswith((".png", ".jpg", ".jpeg")):
        shutil.move(source, images_dir)
        print("Moved", filename, "to Images folder")

    elif filename.lower().endswith((".pdf", ".txt", ".docx", ".pptx")):
        shutil.move(source, docs_dir)
        print("Moved", filename, "to Documents folder")

    elif filename.lower().endswith((".mp4", ".mp3", ".wav", ".flac")):
        shutil.move(source, V_A_dir)
        print("Moved", filename, "to Video and Audio folder")

    elif filename.lower().endswith((".zip", ".exe", ".rar", ".7z", ".msi", ".tar", ".dmg", ".apk")):
        shutil.move(source, compressed_dir)
        print("Moved", filename, "to Compressed Files and Software Packages folder")

input("\nOrganization complete! Press Enter to exit...")