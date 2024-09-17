import subprocess

def backup_database(db_name, backup_file, db_user='root', db_password=''):
    mysqldump_path = r"C:\xampp\mysql\bin\mysqldump.exe"
    dump_command = [mysqldump_path, "-u", db_user]

    if db_password:
        dump_command.append(f"-p{db_password}")
    else:
        dump_command.append("--password=")

    dump_command.append(db_name)

    try:
        with open(backup_file, 'w') as outfile:
            result = subprocess.run(dump_command, stdout=outfile, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                print(f"Error during backup: {result.stderr}")
            else:
                print(f"Backup of {db_name} successful. Saved as {backup_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_backup():
    db_name = 'finance_db'
    backup_file = 'finance_db_backup.sql'
    db_password = ''
    backup_database(db_name, backup_file, db_user='root', db_password=db_password)


