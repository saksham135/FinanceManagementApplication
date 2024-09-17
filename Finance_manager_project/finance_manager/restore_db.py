import subprocess


def restore_database(db_name, backup_file, db_user='root', db_password=''):
    mysql_path = r"C:\xampp\mysql\bin\mysql.exe"

    # Construct the mysql command
    restore_command = [
        mysql_path, "-u", db_user
    ]

    if db_password:
        restore_command.append(f"-p{db_password}")
    else:
        restore_command.append("--password=")  # Handle empty password

    restore_command.append(db_name)

    # Print the command for debugging purposes
    print(f"Running command: {' '.join(restore_command)}")

    try:
        # Open the backup file and feed it to the mysql command
        with open(backup_file, 'r') as infile:
            result = subprocess.run(
                restore_command,
                stdin=infile,
                stdout=subprocess.PIPE,  # Capture stdout
                stderr=subprocess.PIPE,  # Capture stderr
                text=True  # Ensure output is in text format
            )

            # Check if there was any output or error
            if result.returncode != 0:
                print(f"Error during restoration: {result.stderr}")
            else:
                print(f"Restoration of {db_name} from {backup_file} successful.")
                print(f"Output: {result.stdout}")  # Print stdout for visibility
    except FileNotFoundError as fnf_error:
        print(f"File not found: {backup_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


def restore_backup():
    db_name = 'finance_db'
    backup_file = 'finance_db_backup.sql'
    db_password = ''  # Add the password if necessary
    restore_database(db_name, backup_file, db_user='root', db_password=db_password)



