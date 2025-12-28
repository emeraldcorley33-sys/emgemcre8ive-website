import os
from PIL import Image

# Supported image extensions
IMAGE_EXTENSIONS = ['.png', '.jpg', '.jpeg']

# Walk through all directories and files
def compress_and_convert_images(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                file_path = os.path.join(subdir, file)
                try:
                    img = Image.open(file_path)
                    # Compress and overwrite original (for PNG/JPG)
                    if ext in ['.jpg', '.jpeg']:
                        img.save(file_path, 'JPEG', quality=80, optimize=True)
                    elif ext == '.png':
                        img.save(file_path, 'PNG', optimize=True)
                    # Convert to WebP
                    webp_path = os.path.splitext(file_path)[0] + '.webp'
                    img.save(webp_path, 'WEBP', quality=80, method=6)
                    print(f"Optimized and converted: {file_path} -> {webp_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    compress_and_convert_images(os.getcwd())
    print("All images processed.")
