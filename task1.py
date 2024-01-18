from pathlib import Path
import argparse
import shutil


def copy_files(src_dir, dest_dir):
    src_path = Path(src_dir)
    dest_path = Path(dest_dir)
    
    if not src_path.exists() or not src_path.is_dir():
        print(f"Директорія: {src_path} не існує або це щось інше.")
        return

    for element in src_path.iterdir():
        if element.is_dir():
            copy_files(element, dest_path)
        else:
            try:
                copy_file(element, dest_path)
            except Exception as e:
                print(f"Помилка копіювання файлу {src_path}: {e}")

def copy_file(src_path, dest_path):
    file_extension = src_path.suffix.lstrip(".")
    dest_subdir_path = dest_path / file_extension

    dest_subdir_path.mkdir(parents=True, exist_ok=True)   

    shutil.copy2(src_path, dest_subdir_path)
        

def parse_argv():
    parser = argparse.ArgumentParser(description="Рекурсивно копіює файли за розширенням.")
    parser.add_argument("src_dir", help="Шлях до вихідної директорії")
    parser.add_argument("dest_dir", nargs="?", default="dist", help="Шлях до директорії призначення")
    args = parser.parse_args()

    return args.src_dir, args.dest_dir


def main():
    src_dir, dest_dir = parse_argv()
    
    copy_files(src_dir, dest_dir)

if __name__ == "__main__":
    main()
