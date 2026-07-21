#!/usr/bin/env python3

import subprocess
import time
from datetime import datetime

SERVICE_NAME = "docker"
LOG_FILE = "/root/service_restart.log"


def write_log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} : {message}\n")


def check_service():
    result = subprocess.run(
        ["/usr/bin/systemctl", "is-active", SERVICE_NAME],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()


def restart_service():
    subprocess.run(
        ["/usr/bin/systemctl", "restart", SERVICE_NAME]
    )


write_log("Docker Monitor Started")

while True:

    status = check_service()

    if status == "active":
        write_log("Docker Running")

    else:
        write_log("Docker Down")
        restart_service()

        if check_service() == "active":
            write_log("Docker Restarted Successfully")
        else:
            write_log("Restart Failed")

    time.sleep(15)  





    