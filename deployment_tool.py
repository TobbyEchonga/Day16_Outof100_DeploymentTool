import os
import shutil
from datetime import datetime

def deploy_code(source_path, destination_path):
    try:
        # Create a timestamped backup of the current deployment
        backup_folder = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        backup_path = os.path.join(destination_path, backup_folder)
        shutil.copytree(destination_path, backup_path)
        print(f"Backup created: {backup_path}")

        # Deploy the new code
        shutil.rmtree(destination_path)
        shutil.copytree(source_path, destination_path)
        print("Code deployed successfully")

    except Exception as e:
        print(f"Error during deployment: {e}")
        # Rollback in case of an error
        rollback(backup_path, destination_path)

def rollback(backup_path, destination_path):
    try:
        # Rollback to the previous deployment
        shutil.rmtree(destination_path)
        shutil.copytree(backup_path, destination_path)
        print("Rollback successful")

    except Exception as e:
        print(f"Error during rollback: {e}")
        print("Manual intervention required for rollback")

# Example Usage
if __name__ == "__main__":
    source_path = "/path/to/your/source/code"
    destination_path = "/path/to/your/deployment/folder"

    deploy_code(source_path, destination_path)
