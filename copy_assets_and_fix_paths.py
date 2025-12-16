<<<<<<< HEAD
import shutil
import os
import glob
import sys

# Source and destination directories
src_base = r"c:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website"
dest_base = r"c:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website\emgemcre8ive-website"

# Open log file
log_file = open(os.path.join(dest_base, "copy_log.txt"), "w", encoding="utf-8")

def log(msg):
    print(msg)
    log_file.write(msg + "\n")
    log_file.flush()
    sys.stdout.flush()

# Folders to copy
folders = [
    "website-mockups",
    "website-design-mockups",
    "barbie-birthday-package-website",
    "two-fast-birthday-package-website",
    "in-full-bloom-birthday-package",
    "emgemcre8ive-logos-svg",
    "emgemcre8ive-logos-png",
    "emgemcre8ive-website-icons",
    "printables"
]

log("Copying asset folders...")
for folder in folders:
    src = os.path.join(src_base, folder)
    dest = os.path.join(dest_base, folder)
    if os.path.exists(src):
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
        log(f"  ✓ Copied: {folder}")
    else:
        log(f"  ✗ Not found: {folder}")

# Copy loose image files
log("\nCopying loose image files...")
for ext in ['*.jpg', '*.png']:
    for file in glob.glob(os.path.join(src_base, ext)):
        filename = os.path.basename(file)
        dest_file = os.path.join(dest_base, filename)
        shutil.copy2(file, dest_file)
        log(f"  ✓ Copied: {filename}")

# Fix HTML file paths
log("\nFixing HTML file paths...")
os.chdir(dest_base)
for htmlfile in glob.glob("*.html"):
    with open(htmlfile, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    content = content.replace('src="../', 'src="')
    content = content.replace('srcset="../', 'srcset="')
    
    if content != original:
        with open(htmlfile, "w", encoding="utf-8") as f:
            f.write(content)
        log(f"  ✓ Fixed: {htmlfile}")
    else:
        log(f"  - No changes: {htmlfile}")

log("\n✅ All done!")
log_file.close()
=======
import shutil
import os
import glob
import sys

# Source and destination directories
src_base = r"c:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website"
dest_base = r"c:\Users\Teaga\OneDrive\Documents\emgemcre8ive-website\emgemcre8ive-website"

# Open log file
log_file = open(os.path.join(dest_base, "copy_log.txt"), "w", encoding="utf-8")

def log(msg):
    print(msg)
    log_file.write(msg + "\n")
    log_file.flush()
    sys.stdout.flush()

# Folders to copy
folders = [
    "website-mockups",
    "website-design-mockups",
    "barbie-birthday-package-website",
    "two-fast-birthday-package-website",
    "in-full-bloom-birthday-package",
    "emgemcre8ive-logos-svg",
    "emgemcre8ive-logos-png",
    "emgemcre8ive-website-icons",
    "printables"
]

log("Copying asset folders...")
for folder in folders:
    src = os.path.join(src_base, folder)
    dest = os.path.join(dest_base, folder)
    if os.path.exists(src):
        if os.path.exists(dest):
            shutil.rmtree(dest)
        shutil.copytree(src, dest)
        log(f"  ✓ Copied: {folder}")
    else:
        log(f"  ✗ Not found: {folder}")

# Copy loose image files
log("\nCopying loose image files...")
for ext in ['*.jpg', '*.png']:
    for file in glob.glob(os.path.join(src_base, ext)):
        filename = os.path.basename(file)
        dest_file = os.path.join(dest_base, filename)
        shutil.copy2(file, dest_file)
        log(f"  ✓ Copied: {filename}")

# Fix HTML file paths
log("\nFixing HTML file paths...")
os.chdir(dest_base)
for htmlfile in glob.glob("*.html"):
    with open(htmlfile, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    content = content.replace('src="../', 'src="')
    content = content.replace('srcset="../', 'srcset="')
    
    if content != original:
        with open(htmlfile, "w", encoding="utf-8") as f:
            f.write(content)
        log(f"  ✓ Fixed: {htmlfile}")
    else:
        log(f"  - No changes: {htmlfile}")

log("\n✅ All done!")
log_file.close()
>>>>>>> 24bc712b3951ad0deb946694a2b72a4c7a69f20d
