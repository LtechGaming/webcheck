#Web checker python 3.12 edition
#License: MIT
print("sl")
import os
import json
currentdir = os.getcwd()
lang = open(currentdir + "/en_uk.json")
la = json.load(lang)
print(la['start_imports'])
print("1")
import logging
print("2")
logging.basicConfig(filename="logs.log", level=logging.INFO)
print("3")
from datetime import datetime
print("4")
timen = datetime.now()
print("5")
logging.info('bootup' + str(timen))
print("6")
import urllib.request
print("7")
ac = 'qwertyuipopasdfghjklzxcvbnm:/#%1234567890."! @_()-QWERTYUIOPASDFGHJKLZXCVBNM'
print("8")
webcheckversion = "2.1"
print("9")
incom = ""
print("10")
langname = "English(UK)"
print("11")
langper = "100%(source lang)"
print("12")
langcompat = "full"
print("13")
ccenabled = True
print("14")
stenabled = True
print("15")
forcedst = False
print("16")
forcedstv = True
print("17")
ex = False
print(la['finish_text'])
print(la['start_texto'] + webcheckversion + la["start_textt"])
while True:
    proc = ""
    incom = ""
    sectorlist = []
    command = False
    version = 0
    w = input(la["web_input_text"])
    logging.info("Input: " + w)
    ic = []
    icr = la["failed"]
    ica = 0
    ics = la["pass"]
    add = ""
    print(" ")
    if ccenabled == True:
        for i in range(0, len(w)):
            if w[i] in ac:
                ica += 0
            else:
                ica += 1
                ics = la["fail"]
                ic += w[i]
        icr = la["success"]
        print(la["cc"] + str(icr) + la["result"] + str(ics) + la["and"] + str(ica) + la["bc"])
        if ica > 0:
            print(la["bci"] + str(ic) + ".")
            i = input(la["inforequest"])
            if i == "i":
                print(la["infofull"])
        print(" ")
        print(" ")
        logging.info("Character check restult for: " + w + " resulted in " + la["cc"] + str(icr) + la["result"] + str(ics) + la["and"] + str(ica) + la["bc"])
    sectorlist = w.split(":")
    try:
        if sectorlist[0] == "wc":
            command = True
            version = 3
            incom = w[version:len(w)]
        else:
            command = False
    except:
        command = False
        logging.warn("Exception occured with detecting commands")
    if command == False and stenabled == True:
        if forcedst == False:
            system = bool(input(la["modeinput"]))
        else:
            system = forcedstv
        print(" ")
        if system == True:
            sectorlist = w.split(":")
            if sectorlist[0] == "https":
                version = 5
            elif sectorlist[0] == "http":
                version = 4
            else:
                version = 0
                add = "://"
            unsvers = "http" + add + w[version:len(w)]
            svers = "https" + add + w[version:len(w)]
            unsav = False
            sav = False
            try:
                st = urllib.request.urlopen(unsvers).status
                if st == 200:
                    print(unsvers + ' http'+ la["statusup"] + str(st))
                else:
                    print(unsvers + ' http' + la["statusdown"] + str(st))
                unsav = True
                logging.info("Http check success for " + w)
            except:
                print(la["noweb"])
                logging.warning("Http check fail for " + w)
            print(" ")
            try:
                st = urllib.request.urlopen(svers).status
                if st == 200:
                    print(svers + ' https' + la["statusup"] + str(st))
                else:
                    print(svers + ' https' + la["statusdown"] + str(st))
                sav = True
                logging.info("Https check success for " + w)
            except:
                print(la["nossl"])
                logging.warning("Https check fail for " + w)
        else:
            try:
                st = urllib.request.urlopen(svers).status
                if st == 200:
                    print(la["statusup"] + str(st))
                else:
                    print(la["statusdown"] + str(st))
                sav = True
                logging.info("Check success for " + w)
            except:
                logging.warning("Check fail for " + w)
                print(la["olderror"])
    elif command == True:
        print(la["cmds"])
        print(" ")
        print(" ")
        if incom == "//commands":
            print("commands, changelog, lang, dv, cc:<True/False>, st:<True/False>, resetvars, iweb, fstv<True/False>, fstve<True/False>, commandhelp, cv, echo<output>, log<output>, exper<True/False>")
        elif incom == "//changelog":
            print("2.1 - separate command changelog, logs")
        elif incom == "//lang":
            print(la["complang"] + langname + " " + langper + " " + langcompat)
        elif incom == "//dv":
            print("DV 2.3 - logs, cc separate")
        elif incom == "//cc:True" or incom == "//cc:False":
            if sectorlist[2] == True:
                print(la["enabled"])
                ccenabled = True
            else:
                print(la["disabled"])
                ccenabled = False
        elif incom == "//st:True" or incom == "//st:False":
            if sectorlist[2] == True:
                print(la["enabled"])
                stenabled = True
            else:
                print(la["disabled"])
                stenabled = False
        elif incom == "//resetvars":
            print(la["resetv"])
            incom = ""
            sectorlist = []
            command = False
            version = 0
            w = ""
            ic = []
            icr = la["failed"]
            ica = 0
            ics = la["pass"]
            add = ""
            langname = "English(UK)"
            langper = "100%(source lang)"
            langcompat = "full"
            ccenabled = True
            stenabled = True
            currentdir = os.getcwd()
            lang = open(currentdir + "/en_uk.json")
            la = json.load(lang)
            webcheckversion = "2.1"
            proc = ""
            forcedst = False
            forcedstv = True
        elif incom == "//iweb":
            proc = input(la["iwebwarn"])
            if proc == "y":
                w = input(la["iweb"])
                print(urllib.request.urlopen(w).status)
        elif incom == "//fstv:True" or incom == "//fstv:False":
            forcedst = True
            if sectorlist[2] == True:
                print(la["full"])
                forcedstv = True
            else:
                print(la["basic"])
                forcedstv = False
        elif incom == "//fstve:True" or incom == "//fstve:False":
            if sectorlist[2] == True:
                print(la["enabled"])
                forcedst = True
            else:
                print(la["disabled"])
                forcedst = False
        elif incom == "//commandhelp":
            print(la["chinfo"])
            print("""
commands = full list of commands
changelog = changelog of the latest python version
lang = language info
dv = design version + changelog
cc = enable/disable character check(True/False)
st = enable/disable status check(True/False)
resetvars = debug command for resetting variables
iweb = individual web check using raw urllib.request, may crash the program
fstv = force status version(to new or old using True/False)
fstve = force status version anable(True/False)
commandhelp = detailed list of what commands do
cv = command version + changelog
echo = echo command
log = log to logs file
crash = well, we know what this does...
exper = enable experimental features(True/False)""")
        elif incom == "//cv":
            print("CV 4 - command version, command help, forced status, echo, log")
        elif sectorlist[1] == "//echo":
            print(sectorlist[2])
        elif sectorlist[1] == "//log":
            logging.info("Logged by user: " + sectorlist[2])
        elif incom == "//crash":
            timen = datetime.now()
            logging.error("You crashed this. This is your fault. at" + str(timen))
            forcedst = True + 0 + "hi"
        elif incom == "//exper:True" or incom == "//exper:False":
            print("EX: None")
            if sectorlist[2] == True:
                print(la["enabled"])
                ex = True
            else:
                print(la["disabled"])
                ex = False
        else:
            print(la["notfound"])
    print(" ")
    print(" ")
