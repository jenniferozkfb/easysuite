import os
import shutil
import ctypes
import tempfile

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Error checking admin status: {e}")
        return False

def clear_temp_files():
    """Clear temporary files."""
    temp_dir = tempfile.gettempdir()
    try:
        shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        print("Temporary files cleared.")
    except Exception as e:
        print(f"Error clearing temporary files: {e}")

def clear_browser_data():
    """Clear browser history, cookies, and cache."""
    # Paths to clear browser data, assuming default installation paths
    paths = [
        os.path.join(os.getenv('APPDATA'), 'Mozilla', 'Firefox', 'Profiles'),
        os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data'),
        os.path.join(os.getenv('LOCALAPPDATA'), 'Microsoft', 'Edge', 'User Data')
    ]
    
    for path in paths:
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"Cleared data from: {path}")
            except Exception as e:
                print(f"Error clearing data from {path}: {e}")
        else:
            print(f"Path not found, nothing to clear: {path}")

def main():
    print("Starting EasySuite...")
    if not is_admin():
        print("This program requires administrative privileges to clear browsing data.")
        return
    
    clear_temp_files()
    clear_browser_data()
    print("Cleaning completed.")

if __name__ == "__main__":
    main()