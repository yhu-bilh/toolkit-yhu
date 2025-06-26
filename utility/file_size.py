import os
import pathlib
from pathlib import Path

def get_file_size_methods(file_path):
    """Demonstrate different ways to get file size in Python"""

    # Method 1: Using os.path.getsize() - Most common
    try:
        size1 = os.path.getsize(file_path)
        print(f"Method 1 (os.path.getsize): {size1} bytes")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return
    except OSError as e:
        print(f"Error accessing file: {e}")
        return

    # Method 2: Using os.stat()
    try:
        stat_info = os.stat(file_path)
        size2 = stat_info.st_size
        print(f"Method 2 (os.stat): {size2} bytes")
    except OSError as e:
        print(f"Error with os.stat: {e}")

    # Method 3: Using pathlib (Python 3.4+)
    try:
        path_obj = Path(file_path)
        size3 = path_obj.stat().st_size
        print(f"Method 3 (pathlib): {size3} bytes")
    except OSError as e:
        print(f"Error with pathlib: {e}")

    # Method 4: Using file seek (for open files)
    try:
        with open(file_path, 'rb') as f:
            f.seek(0, 2)  # Seek to end of file
            size4 = f.tell()  # Get current position (file size)
            print(f"Method 4 (file seek): {size4} bytes")
    except OSError as e:
        print(f"Error opening file: {e}")

def format_file_size(size_bytes):
    """Convert bytes to human-readable format"""
    if size_bytes == 0:
        return "0 B"

    size_names = ["B", "KB", "MB", "GB", "TB"]
    import math
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_names[i]}"

def get_multiple_file_sizes(file_paths):
    """Get sizes for multiple files"""
    print("Multiple file sizes:")
    print("-" * 50)

    for file_path in file_paths:
        try:
            size = os.path.getsize(file_path)
            formatted_size = format_file_size(size)
            filename = os.path.basename(file_path)
            print(f"{filename:30} {size:>12} bytes ({formatted_size})")
        except FileNotFoundError:
            print(f"{file_path:30} File not found")
        except OSError as e:
            print(f"{file_path:30} Error: {e}")

def get_directory_size(directory_path):
    """Get total size of all files in a directory"""
    total_size = 0
    file_count = 0

    try:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(file_path)
                    total_size += size
                    file_count += 1
                except OSError:
                    # Skip files that can't be accessed
                    continue

        print(f"Directory: {directory_path}")
        print(f"Total files: {file_count}")
        print(f"Total size: {total_size} bytes ({format_file_size(total_size)})")
        return total_size

    except OSError as e:
        print(f"Error accessing directory: {e}")
        return 0

def check_file_exists_and_size(file_path):
    """Check if file exists and get its size"""
    if os.path.exists(file_path):
        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            print(f"File exists: {file_path}")
            print(f"Size: {size} bytes ({format_file_size(size)})")
            return size
        else:
            print(f"Path exists but is not a file: {file_path}")
            return None
    else:
        print(f"File does not exist: {file_path}")
        return None

def compare_file_sizes(file1, file2):
    """Compare sizes of two files"""
    try:
        size1 = os.path.getsize(file1)
        size2 = os.path.getsize(file2)

        print(f"File 1: {file1} - {size1} bytes ({format_file_size(size1)})")
        print(f"File 2: {file2} - {size2} bytes ({format_file_size(size2)})")

        if size1 > size2:
            diff = size1 - size2
            print(f"File 1 is larger by {diff} bytes ({format_file_size(diff)})")
        elif size2 > size1:
            diff = size2 - size1
            print(f"File 2 is larger by {diff} bytes ({format_file_size(diff)})")
        else:
            print("Both files are the same size")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except OSError as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Example file path - replace with your actual file
    example_file = "C:\\Users\\yhu\\OneDrive\\Pictures\\Pics\\2025-06\\2025-06-26_12-32-37.jpg"

    # Create a sample file for demonstration
    with open(example_file, "w") as f:
        f.write("This is a sample file for size testing.\n" * 100)

    print("=" * 60)
    print("FILE SIZE METHODS DEMONSTRATION")
    print("=" * 60)

    # Demonstrate different methods
    get_file_size_methods(example_file)

    print("\n" + "=" * 60)
    print("FORMATTED FILE SIZE")
    print("=" * 60)

    # Show formatted size
    size = os.path.getsize(example_file)
    print(f"Raw size: {size} bytes")
    print(f"Formatted: {format_file_size(size)}")

    print("\n" + "=" * 60)
    print("FILE EXISTENCE CHECK")
    print("=" * 60)

    # Check file existence and size
    check_file_exists_and_size(example_file)
    check_file_exists_and_size("nonexistent_file.txt")

    print("\n" + "=" * 60)
    print("DIRECTORY SIZE")
    print("=" * 60)

    # Get current directory size
    get_directory_size(".")

    # Clean up
    os.remove(example_file)