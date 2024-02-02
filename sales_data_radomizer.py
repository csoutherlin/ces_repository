# Import the required libraries
import csv
import random
import time
import shutil
import logging

# Set up the logging configuration
logging.basicConfig(filename='shuffle_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the source and backup directories
source_dir = 'sales_data/'
backup_dir = 'sales_data_backup/'

# Define the list of CSV files to shuffle
csv_files = ['sales_jan.csv', 'sales_feb.csv', 'sales_mar.csv']

# Define the backup interval in seconds
backup_interval = 10

# Define a variable to store the last backup date
last_backup_date = None

# Define a function to shuffle and backup a CSV file
def shuffle_and_backup(csv_file):
    # Read the sales data from the CSV file
    with open(source_dir + csv_file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader) # Skip the header row
        data = list(reader) # Store the rest of the data in a list
    
    # Check if the current date is different from the last backup date
    global last_backup_date
    current_date = time.strftime('%Y-%m-%d')
    if current_date != last_backup_date:
        # Copy the original file to the backup directory
        shutil.copy(source_dir + csv_file, backup_dir + csv_file)
        # Update the last backup date
        last_backup_date = current_date
        # Log the backup operation
        logging.info(f'Backed up {csv_file} to {backup_dir}')
    
    # Shuffle the rows of the sales data
    random.shuffle(data)

    # Write the shuffled data back to the original CSV file
    with open(source_dir + csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header) # Write the header row
        writer.writerows(data) # Write the shuffled data
    # Log the shuffle operation
    logging.info(f'Shuffled {csv_file} in {source_dir}')

# Define a loop to run the shuffle and backup operation every backup interval
while True:
    # Loop through the CSV files
    for csv_file in csv_files:
        try:
            # Call the shuffle and backup function
            shuffle_and_backup(csv_file)
        except Exception as e:
            # Log any errors that might occur
            logging.error(f'Error while processing {csv_file}: {e}')
    # Wait for the backup interval
    time.sleep(backup_interval)
