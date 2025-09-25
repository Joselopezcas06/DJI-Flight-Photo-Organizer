import os 
from datetime import datetime
import shutil

# The photographies taken are named based on the following structure
# File name: DJI_20240421081310_0465_D.JPG
#       Year 2024, Month 04, Day 21, Hour 08, Minute 13, Seconds 10


# 1.  Function to relocate the images 
def relocate_images(source_directory, destination_directory):

    image_files = []

    try:
        for filename in os.listdir(source_directory):
            if filename.endswith(".JPG"):
                image_files.append(filename)
    except FileNotFoundError:
        print(f"Error: Source directory not found at {source_directory}")
        exit()
    
    image_files.sort() # The images are processed in the correct cronological order
    # === Phase 2: Process the images ===
    if not image_files:
        print("No JGP images found in the source directory")
    else:
        print("Starting flight organization process...")
        first_filename = image_files[0]
        # Extrac the full timestamp of the image
        timestamp_str = first_filename[4:18]
        print(timestamp_str)
        previous_time = datetime.strptime(timestamp_str, "%Y%m%d%H%M%S")

        # create the first flight folder
        flight_counter = 1
        current_flight_path = os.path.join(destination_directory, f"flight_{flight_counter}")
        os.makedirs(current_flight_path, exist_ok=True)

        # Copy the first image 
        source_path = os.path.join(source_directory, first_filename)
        destination_path = os.path.join(current_flight_path, first_filename)
        shutil.copy2(source_path, destination_path)
        print(f"Started flight_{flight_counter} and copied {first_filename}")

        # loop triught the rest of the files 
        for filename in image_files[1:]:
            timestamp_str = filename[4:18]
            current_time = datetime.strptime(timestamp_str, "%Y%m%d%H%M%S")


            time_difference = current_time - previous_time

            # Check the rule 
            if time_difference.total_seconds() > 60: # total_seconds is a method of datetime module
                flight_counter  +=1 
                current_flight_path = os.path.join(destination_directory, f"flight_{flight_counter}")
                os.makedirs(current_flight_path, exist_ok=True)
                print("\n-> Time diffeerence > 60s. A new directory is created")

            # Copy the file to the current flight folder

            source_path = os.path.join(source_directory,filename)
            destination_path = os.path.join(current_flight_path, filename)
            shutil.copy2(source_path, destination_path)
            print(f"   Copied {filename} to flight_{flight_counter} (Diff: {time_difference.total_seconds():.1f}s)")

            # Update the previous time
            previous_time = current_time
        
        print("\nProcess complete!")



source = r"D:\path\to\your\source_images"
destination = r"D:\path\to\your\organized_flights"

relocate_images(source, destination)

