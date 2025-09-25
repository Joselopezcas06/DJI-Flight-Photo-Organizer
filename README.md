# DJI Flight Photo Organizer

A Python script to automatically sort DJI drone photos into flight folders based on the time they were taken. This tool is designed to streamline the data management workflow for large photogrammetry operations.



---

## Overview

In photogrammetry surveys, a drone often performs multiple flights to cover a large area. This script solves the tedious manual task of separating photos from each flight. It works by analyzing the timestamp in each photo's filename and grouping them. If the time gap between two consecutive photos is more than 60 seconds—a common pause between landing and taking off again—it creates a new "flight" folder.

---

## Features

-   **Automatic Flight Detection**: Intelligently creates new folders for each distinct flight session.
-   **Timestamp-Based Sorting**: Uses the precise timestamp embedded in DJI filenames (`DJI_YYYYMMDDHHMMSS_...`) for accurate sorting.
-   **Simple Configuration**: Requires only the source and destination paths to be set.
-   **Zero Dependencies**: Runs using only standard Python 3 libraries.

---

## Requirements

-   Python 3.
-   Photos must be in `.JPG` format.
-   Photos must follow the standard DJI naming convention, as the script relies on it to extract the timestamp.
    -   Example: `DJI_20240421081310_0465_D.JPG`

---

## How to Use

Follow these steps to get the script running.

### 1. Save the Script

Save the code into a file named `organize_flights.py` or any other `.py` name you prefer.

### 2. Configure Your Paths

Open the script in a text editor and modify the `source` and `destination` variables at the very bottom of the file.

```python
# SET YOUR FOLDER PATHS HERE
source = r"D:\path\to\your\source_images"
destination = r"D:\path\to\your\organized_flights"

relocate_images(source, destination)
```

-   **`source`**: Set this to the absolute path of the folder containing all the unsorted `.JPG` files.
-   **`destination`**: Set this to the absolute path where you want the new `flight_...` folders to be created.

### 3. Run the Script

Open your terminal or command prompt, navigate to the directory where you saved the script, and execute it using Python.

```bash
python organize_flights.py
```

The script will print its progress in the terminal and notify you when the process is complete. Your photos will be neatly organized in the destination folder.

---

## How It Works

The script operates based on a simple but effective rule:

1.  **Scan and Sort**: It first finds all `.JPG` images in the `source` directory and sorts them chronologically based on their filenames.
2.  **Establish a Baseline**: It takes the timestamp from the very first photo and creates the initial `flight_1` folder.
3.  **Iterate and Compare**: It then loops through the rest of the images, calculating the time difference in seconds between each consecutive photo.
4.  **Apply the Rule**:
    -   If the time difference is **less than or equal to 60 seconds**, the photo belongs to the current flight and is copied into the current flight folder.
    -   If the time difference is **greater than 60 seconds**, the script assumes a new flight has begun. It increments the flight counter (e.g., `flight_2`) and creates a new folder for the subsequent photos.

This process continues until all images have been organized.
