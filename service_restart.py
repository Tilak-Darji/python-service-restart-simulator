import subprocess

service = input("Enter Service Name: ")
status = input("Enter Service Status (running/stopped): ").lower()

if status == "stopped":
    print(f"{service} is stopped.")
    print("Restarting service...")

    subprocess.run(["sudo", "systemctl", "restart", service])

    print(f"{service} restarted successfully.")
else:
    print(f"{service} is running fine.")