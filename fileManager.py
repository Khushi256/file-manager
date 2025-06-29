#Import Statements

import os       # os provides files and directory
import shutil    # helps to move,copy and delete the files and folders 
import time      # provides Time-related functions
from datetime import datetime, timedelta     # Date/time manipulation classes


# Configuration Variables

TARGET_DIR = "C:\\Users\\khush\\OneDrive\\Desktop\\trial"   # The target directory path
DAYS_LIMIT = 30   # days limit for the file to get deleted


# function to organize the files by date

def organize_files_by_date():    

    for file in os.listdir(TARGET_DIR):     # Gets a list of all items in the target directory
        file_path = os.path.join(TARGET_DIR, file)     # combines directory path with filename

        #Check If Item is a File
        if os.path.isfile(file_path):    

            # Get File Creation Time
            created_time = datetime.fromtimestamp(os.path.getctime(file_path))     

            # Create Date-Based Folder Name 
            date_folder = created_time.strftime("%Y-%m-%d")      

            # Create Directory and Move File
            date_dir = os.path.join(TARGET_DIR, date_folder)      # Creates full path for the date folder
            os.makedirs(date_dir, exist_ok=True)                # Creates the directory if it doesn't exist
            new_path = os.path.join(date_dir, file)             #  prevents errors if directory already exists
            shutil.move(file_path, new_path)                    #  Moves the file to the new location
            print(f"Moved: {file} → {new_path}")                #  Shows what was moved


# function to delete temporary files

def delete_old_temp_files():

    now = time.time()            # Gets current time as timestamp
    for root, dirs, files in os.walk(TARGET_DIR):      # Recursively walks through all subdirectories
        for file in files:
            if "temp" in file.lower():        # Checks if "temp" appears anywhere in the filename

                # Get File Path and Timestamps
                path = os.path.join(root, file)
                print(f"Checking: {path}")
                last_access = os.path.getatime(path)     #  Gets last access time
                last_modified = os.path.getmtime(path)      # Gets last modification time

                 # Debug output
                print(f"→ Last accessed: {datetime.fromtimestamp(last_access)}")
                print(f"→ Last modified: {datetime.fromtimestamp(last_modified)}")

                # Check Age and Delete
                if (now - last_access > DAYS_LIMIT * 86400) and (now - last_modified > DAYS_LIMIT * 86400):   
                # Converts days to seconds (86400 seconds = 1 day)
                # now - last_access  -> Checks if file hasn't been accessed recently
                # now - last_modified -> Checks if file hasn't been modified recently

                    print(f"Deleting: {path}")
                    os.remove(path)     # Deletes the file if both conditions are met


# Main Execution Block

if __name__ == "__main__":      # Only runs when script is executed directly 
    organize_files_by_date()
    delete_old_temp_files()
