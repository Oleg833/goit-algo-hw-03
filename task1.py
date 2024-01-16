import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        print(f"Помилка: Вихідна директорія {src_dir} не існує.")
        return
    
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)


    for root, dirs, files in os.walk(src_dir):
        for subdir in dirs:
            src_subdir = os.path.join(root, subdir)
            dest_subdir = os.path.join(dest_dir, os.path.relpath(src_subdir, src_dir))

            copy_files(src_subdir, dest_subdir)

        for file in files:
            src_path = os.path.join(root, file)

            try:
                copy_file(src_path, dest_dir)
            except Exception as e:
                print(f"Помилка копіювання файлу {src_path}: {e}")

def copy_file(src_path, dest_dir):
    _, file_extension = os.path.splitext(src_path)

    subdir = os.path.join(dest_dir, file_extension[1:])
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    shutil.copy2(src_path, os.path.join(subdir, os.path.basename(src_path)))

def main():
    parser = argparse.ArgumentParser(description="Рекурсивно копіює файли та сортує їх за розширенням.")
    parser.add_argument("src_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Шлях до директорії призначення")
    args = parser.parse_args()

    copy_files(args.src_dir, args.dest_dir)

if __name__ == "__main__":
    main()
