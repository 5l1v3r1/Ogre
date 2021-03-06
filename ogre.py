#!/usr/bin/env python3
Blue, LBlue, Red, LRed, White, LWhite, Yellow, Magenta, Green, LGreen, Cyan, NC = '\033[1;94m', '\033[0;94m' ,'\033[1;91m', '\033[0;91m', '\033[1;97m', '\033[0;97m','\033[1;93m', '\033[1;95m', '\033[1;92m', '\033[0;92m', '\033[1;96m', '\033[0m'
import socket
import time
import concurrent.futures
import subprocess
import sys
import os
import os.path
from os import path
from subprocess import PIPE

usercheck = "u"
def inputHandler():
    try:
        print()
        inputHeader= (str(input(Green + "[#] Enter your Choice: " + White)))
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as e:
        print(RED + "\n" + "[!] Ogre crashed..." + "\n" + "[!] Debug info: " + "\n")
        print(traceback.format_exc())
        print("\n" + NC)
        exit()
    print()
    #print(Magenta + "-------------------------------------" + NC)
    if inputHeader == "1":
        ftp()
    elif inputHeader == "2":
        ssh()
    elif inputHeader == "3":
        telnet()
    elif inputHeader == "4":
        postgresql()
    elif inputHeader == "5":
        vnc()
    else:
        print (Red + "[!] Wrong Choice: '" + Yellow + inputHeader + Red + "'")
        inputHandler()

def ftp():
    global usercheck
    try:
        host = input(Blue + "[#] Enter Host IP: " + White)
        port = input(Blue + "[#] Enter Port(default is "+Cyan+"21"+Blue+"): ")
        usercheck = input(Blue + "[#] Would you go with a userlist(U) or a single user name(u)? ["+Cyan+"U"+Blue+"/"+Cyan+"u"+Blue+"]: "+White)
        if usercheck == "U":
            username = input(Blue + "[#] Enter path to User wordlist: "+White)
        elif usercheck == "u":
            username = input(Blue + "[#] Enter Username to use: " + White)
        wordlist = input(Blue + "[#] Enter path to Password wordlist(e.g. "+ Blue + "'" + Cyan + "wordlist/sshpass.txt" + Blue + "'): " + White)
        threads = input(Blue + "[#] Enter the no. of Threads to use(default is " + Cyan +"16" + Blue + "): "+ White)
        print("\n")
        ftpConnect(host, port, username, wordlist, threads)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as e:
        print(RED + "\n" + "[!] Ogre crashed..." + "\n" + "[!] Debug info: " + "\n")
        print(traceback.format_exc())
        print("\n" + NC)
        exit()

def ssh():
    global usercheck
    try:
        host = input(Blue + "[#] Enter Host IP: " + White)
        port = input(Blue + "[#] Enter Port(default is "+Cyan+"22"+Blue+"): ")
        usercheck = input(Blue + "[#] Would you go with a userlist(U) or a single user name(u)? ["+Cyan+"U"+Blue+"/"+Cyan+"u"+Blue+"]: "+White)
        if usercheck == "U":
            username = input(Blue + "[#] Enter path to User wordlist: "+White)
        elif usercheck == "u":
            username = input(Blue + "[#] Enter Username to use: " + White)
        wordlist = input(Blue + "[#] Enter path to Password wordlist(e.g. "+ Blue + "'" + Cyan + "wordlist/sshpass.txt" + Blue + "'): " + White)
        threads = input(Blue + "[#] Enter the no. of Threads to use(default is "+Cyan+ "16"+Blue+"): "+ White)
        #print(Magenta + "-------------------------------------" + NC)
        print("\n")
        sshConnect(host, port, username, wordlist, threads)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as e:
        print(RED + "\n" + "[!] Ogre crashed..." + "\n" + "[!] Debug info: " + "\n")
        print(traceback.format_exc())
        print("\n" + NC)
        exit()
        #with concurrent.futures.ThreadPoolExecutor() as executor:
        #    executor.submit(sshConnect, host, username, password)
def telnet():
    global usercheck
    try:
        host = input(Blue + "[#] Enter Host IP: " + White)
        port = input(Blue + "[#] Enter Port(default is "+Cyan+"23"+Blue+"): ")
        usercheck = input(Blue + "[#] Would you go with a userlist(U) or a single user name(u)? ["+Cyan+"U"+Blue+"/"+Cyan+"u"+Blue+"]: "+White)
        if usercheck == "U":
            username = input(Blue + "[#] Enter path to User wordlist: "+White)
        elif usercheck == "u":
            username = input(Blue + "[#] Enter Username to use: " + White)
        wordlist = input(Blue + "[#] Enter path to Password wordlist(e.g. "+ Blue + "'" + Cyan + "wordlist/sshpass.txt" + Blue + "'): " + White)
        threads = input(Blue + "[#] Enter the no. of Threads to use(default is "+ Cyan +"16" + Blue +"): "+ White)
        print("\n")
        telnetConnect(host, port, username, wordlist, threads)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as e:
        print(RED + "\n" + "[!] Ogre crashed..." + "\n" + "[!] Debug info: " + "\n")
        print(traceback.format_exc())
        print("\n" + NC)
        exit()

def postgresql():
    global usercheck
    try:
        host = input(Blue + "[#] Enter Host IP: " + White)
        port = input(Blue + "[#] Enter Port(default is "+Cyan+"5432"+Blue+"): ")
        usercheck = input(Blue + "[#] Would you go with a userlist(U) or a single user name(u)? ["+Cyan+"U"+Blue+"/"+Cyan+"u"+Blue+"]: "+White)
        if usercheck == "U":
            username = input(Blue + "[#] Enter path to User wordlist: "+White)
        elif usercheck == "u":
            username = input(Blue + "[#] Enter Username to use: " + White)
        wordlist = input(Blue + "[#] Enter path to Password wordlist(e.g. "+ Blue + "'" + Cyan + "wordlist/sshpass.txt" + Blue +"'): " +White)
        threads = input(Blue + "[#] Enter the no. of Threads to use(default is "+ Cyan +"16"+ Blue +"): "+ White)
        print("\n")
        postgresqlConnect(host, port, username, wordlist, threads)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as e:
        print(RED + "\n" + "[!] Ogre crashed..." + "\n" + "[!] Debug info: " + "\n")
        print(traceback.format_exc())
        print("\n" + NC)
        exit()

def vnc():
    try:
        host = input(Blue + "[#] Enter Host IP: " + White)
        port = input(Blue + "[#] Enter Port(default is "+Cyan+"5900"+Blue+"): ")
        wordlist = input(Blue + "[#] Enter path to Password wordlist(e.g. "+ Blue + "'" + Cyan + "wordlist/sshpass.txt" + Blue + "'): " + White)
        threads = input(Blue + "[#] Enter the no. of Threads to use(default is "+Cyan+"16"+Blue+"): "+ White)
        print("\n")
        vncConnect(host, port, wordlist, threads)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as e:
        print(RED + "\n" + "[!] Ogre crashed..." + "\n" + "[!] Debug info: " + "\n")
        print(traceback.format_exc())
        print("\n" + NC)
        exit()

def sshConnect(host, port, username, wordlist, threads):
    try:
        if host == "":
            print(Red + "[!] Please provide a vaild Host")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if port == "":
            port = "22"
        if not path.exists(wordlist):
            print(Red + "[!] Please provide a vaild Password Wordlist")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if usercheck == "U":
            if not path.exists(username):
                print(Red + "[!] Please provide a vaild User Wordlist")
                print(Green + "[#] Exiting...")
                raise SystemExit
            print(Red + "[!] Please provide a vaild Wordlist")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if threads == "":
            threads = "16"
        flag = 0
        print(Green + "[+] Bruteforcing ssh... " + LWhite
              )
        if usercheck == "U":
            p1 = subprocess.Popen(['hydra', '-s', port,'-L', username, '-P', wordlist,
                                   host, 'ssh', '-t', threads, '-I','-e','ns','-V'], stdout=PIPE,
                                  stderr=PIPE)
        else:
            p1 = subprocess.Popen(['hydra', '-s', port, '-l', username, '-P', wordlist, host,
                                   'ssh', '-t', threads, '-I', '-e', 'ns', '-V'], stdout=PIPE,
                                  stderr=PIPE)
        for line in iter(p1.stdout.readline, b''):
            print(line.decode('utf-8').strip('\n'))
            sys.stdout.flush()
            time.sleep(0.0001)
            if 'host' in line.decode('utf-8'):
                print("\n" + LGreen + "[+] Cracked Password:" +
                      line.decode('utf-8') + LWhite)
                flag = 1
        if flag == 0:
            print("\n" + Red + "[!] Password Not Found!" + NC)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as exc:
        print("[!] Error : %s " % exc)

def ftpConnect(host, port, username, wordlist, threads):
    try:
        if host == "":
            print(Red + "[!] Please provide a vaild Host")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if port == "":
            port = "21"
        if not path.exists(wordlist):
            print(Red + "[!] Please provide a vaild Password Wordlist")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if usercheck == "U":
            if not path.exists(username):
                print(Red + "[!] Please provide a vaild User Wordlist")
                print(Green + "[#] Exiting...")
                raise SystemExit
        if threads == "":
            threads = "16"

        flag = 0
        print(Green + "[+] Bruteforcing FTP..." + LWhite)
        if usercheck == "U":
            p1 = subprocess.Popen(['hydra', "-s", port,'-L', username, '-P', wordlist, host, 'ftp','-t', threads, '-I', '-e', 'ns', '-V'],
                                  stdout=PIPE, stderr=PIPE)
        else:
            p1 = subprocess.Popen(['hydra', "-s", port, '-l', username, '-P', wordlist, host,
                                   'ftp', '-t', threads, '-I', '-e', 'ns', '-V'], stdout=PIPE,
                                  stderr=PIPE)
        for line in iter(p1.stdout.readline, b''):
            print(line.decode('utf-8').strip('\n'))
            sys.stdout.flush()
            time.sleep(0.0001)
            if 'host' in line.decode('utf-8'):
                print("\n" + LGreen + "[+] Cracked Password:" +
                line.decode('utf-8') + LWhite)
                flag = 1
        if flag == 0:
            print("\n" + Red + "[!] Password Not Found!" + NC)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as exc:
        print("[!] Error : %s " % exc)

def telnetConnect(host, port, username, wordlist, threads):
    try:
        if host == "":
            print(Red + "[!] Please provide a vaild Host")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if port == "":
            port = "23"
        if not path.exists(wordlist):
            print(Red + "[!] Please provide a vaild Password Wordlist")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if usercheck == "U":
            if not path.exists(username):
                print(Red + "[!] Please provide a vaild User Wordlist")
                print(Green + "[#] Exiting...")
                raise SystemExit
        if threads == "":
            threads = "16"

        flag = 0
        print(Green + "[+] Bruteforcing Telnet..." + LWhite)
        if usercheck == "U":
            p1 = subprocess.Popen(['hydra', '-s', port,'-L', username, '-P', wordlist, host, 'telnet','-t', threads, '-I', '-e', 'ns', '-V'],
                                  stdout=PIPE, stderr=PIPE)
        else:
            p1 = subprocess.Popen(['hydra', '-s', port, '-l', username, '-P', wordlist, host,
                                   'telnet', '-t', threads, '-I', '-e', 'ns', '-V'], stdout=PIPE,
                                  stderr=PIPE)
        for line in iter(p1.stdout.readline, b''):
            print(line.decode('utf-8').strip('\n'))
            sys.stdout.flush()
            time.sleep(0.0001)
            if 'host' in line.decode('utf-8'):
                print("\n" + LGreen + "[+] Cracked Password:" +
                line.decode('utf-8') + LWhite)
                flag = 1
        if flag == 0:
            print("\n" + Red + "[!] Password Not Found!" + NC)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as exc:
        print("[!] Error : %s " % exc)

def postgresqlConnect(host, port, username, wordlist, threads):
    try:
        if host == "":
            print(Red + "[!] Please provide a vaild Host")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if port == "":
            port = "5432"
        if not path.exists(wordlist):
            print(Red + "[!] Please provide a vaild Password Wordlist")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if usercheck == "U":
            if not path.exists(username):
                print(Red + "[!] Please provide a vaild User Wordlist")
                print(Green + "[#] Exiting...")
                raise SystemExit
        if threads == "":
            threads = "16"

        flag = 0
        print(Green + "[+] Bruteforcing PostgreSQL..." + LWhite)
        if usercheck == "U":
            p1 = subprocess.Popen(['hydra', '-s', port, '-L', username, '-P', wordlist, host, 'postgres','-t', threads, '-I', '-e', 'ns', '-V'],
                                  stdout=PIPE, stderr=PIPE)
        else:
            p1 = subprocess.Popen(['hydra', '-s', port,'-l', username, '-P', wordlist, host,
                                   'postgres', '-t', threads, '-I', '-e', 'ns', '-V'], stdout=PIPE,
                                  stderr=PIPE)
        for line in iter(p1.stdout.readline, b''):
            print(line.decode('utf-8').strip('\n'))
            sys.stdout.flush()
            time.sleep(0.0001)
            if 'host' in line.decode('utf-8'):
                print("\n" + LGreen + "[+] Cracked Password:" +
                line.decode('utf-8') + LWhite)
                flag = 1
        if flag == 0:
            print("\n" + Red + "[!] Password Not Found!" + NC)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as exc:
        print("[!] Error : %s " % exc)

def vncConnect(host, port, wordlist, threads):
    try:
        if host == "":
            print(Red + "[!] Please provide a vaild Host")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if port == "":
            port = "5900"
        if not path.exists(wordlist):
            print(Red + "[!] Please provide a vaild Wordlist")
            print(Green + "[#] Exiting...")
            raise SystemExit
        if threads == "":
            threads = "16"

        flag = 0
        print(Green + "[+] BruteForcing VNC..." + LWhite)
        p1 = subprocess.Popen(['hydra', '-s' , port, '-P', wordlist, host,
                                     'vnc', '-t', threads, '-V'], stdout=PIPE,
                                    stderr=PIPE)
        for line in iter(p1.stdout.readline, b''):
            print(line.decode('utf-8').strip('\n'))
            sys.stdout.flush()
            time.sleep(0.0001)
            if 'host' in line.decode('utf-8'):
                print("\n" + LGreen + "[+] Cracked Password:" +
                line.decode('utf-8') + LWhite)
                flag = 1
        if flag == 0:
            print("\n" + Red + "[!] Password Not Found!" + NC)
    except KeyboardInterrupt:
        print(Green + "\n" + "[~] Shutting down..." + NC)
        raise SystemExit
    except Exception as exc:
        print("[!] Error : %s " % exc)


os.system('clear||cls')
header = """

        ░█████╗░░██████╗░██████╗░███████╗
        ██╔══██╗██╔════╝░██╔══██╗██╔════╝
        ██║░░██║██║░░██╗░██████╔╝█████╗░░
        ██║░░██║██║░░╚██╗██╔══██╗██╔══╝░░ """+White+"""v0.1 by Yashvendra Kashyap a.k.a y_k_007"""+Green+"""
        ╚█████╔╝╚██████╔╝██║░░██║███████╗
        ░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝
  """
print(Green + "\t" + header + "\n\t" +Red+ "    The Ultimate Bruteforcer" +
     NC)
print()
print(Green + "[~] Available Services to Brute: ")
print()
print(Yellow + "[1] " + "FTP" + NC)
print(Yellow + "[2] " + "SSH" + NC)
print(Yellow + "[3] " + "Telnet" + NC)
print(Yellow + "[4] " + "Postgresql" + NC)
print(Yellow + "[5] " + "VNC" + NC)
inputHandler()

