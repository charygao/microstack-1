#!/usr/bin/env python

import logging
import os
import subprocess
import time

# Setup Logging
log = logging.getLogger("microstack_wait")
log.setLevel(logging.INFO)
stream = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream.setFormatter(formatter)
log.addHandler(stream)


def main():
    log.info("Waiting for microstack to be initialized.")
    while True:
        status = subprocess.check_output(
            ["snapctl", "get", "initialized"],
            universal_newlines=True,
            env=os.environ
        ).strip()
        if status == "true":
            log.info("Microstack initialized. Exiting wait.")
            break
        log.debug("snap not initialized.")
        time.sleep(1)


if __name__ == '__main__':
    main()
