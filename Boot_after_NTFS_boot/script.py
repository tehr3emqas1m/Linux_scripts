import subprocess
import time

ntfs_drive = "/dev/sda3"

print("Unmounting the NTFS drive...")
try:
    subprocess.run(["sudo", "umount", ntfs_drive], check=True)
    print(f"Drive {ntfs_drive} unmounted successfully.")
except subprocess.CalledProcessError:
    print(f"Failed to unmount {ntfs_drive}. It may already be unmounted, or you may need to close any files open on it.")

time.sleep(2)

print("Running ntfsfix on the NTFS drive...")
try:
    subprocess.run(["sudo", "ntfsfix", ntfs_drive], check=True)
    print(f"ntfsfix completed on {ntfs_drive}.")
except subprocess.CalledProcessError:
    print(f"Failed to run ntfsfix on {ntfs_drive}. Please check the drive path and try again.")
