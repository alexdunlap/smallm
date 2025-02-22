import subprocess

import glog


def download():
    website = "https://www.gutenberg.org/cache/epub/11/pg11.txt"
    subprocess.run(["wget", website])
    glog.info("Download successful.")
