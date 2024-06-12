#Web checker python 3.12 edition
#License: MIT
print("sl")
import os
import json
currentdir = os.getcwd()
lang = open(currentdir + "/en_uk.json")
la = json.load(lang)
print(la['start_imports'])
import types
import logging
logging.basicConfig(filename="logs.log", level=logging.INFO)
from datetime import datetime
timen = datetime.now()
logging.info('bootup' + str(timen))
import urllib.request
ac = 'qwertyuipopasdfghjklzxcvbnm:/#%1234567890."! @_()-QWERTYUIOPASDFGHJKLZXCVBNM'
webcheckversion = "3"
incom = ""
langname = "English(UK)"
langper = "100%(source lang)"
langcompat = "full"
confusion = 0
ccenabled = True
stenabled = True
forcedst = False
forcedstv = True
ex = False
import sys
sys.path
mf = 0
mods = [x[0] for x in os.walk(currentdir + "/mods")]
for i in mods:
    if "pyc" in i:
        mods.remove(i)
mods = mods[1:]
mf = len(mods)
modmetasopen = []
modmetas = []
for i in mods:
    try:
        modmetasopen.append(open(str(i) + "/manifest.json"))
    except:
        print("Manifest could not be found for " + str(i))
        mods.remove(i)
ml = len(mods)
for i in modmetasopen:
    modmetas.append(json.load(i))

print(la['finish_text'])
print(la['start_texto'] + webcheckversion + la["start_textt"])
print(la["policy"])
print(la["modding"])

ca = []
for i in modmetas:
    ca.append(i["name"])
print(str(mf) + la["mf"])
print(str(ml) + la["ml"] + str(ca))
modsenabled = True
cat = []
a = 0
reg = True
for i in modmetas:
    cat.append(i["id"])
    sys.path.insert(1,str(mods[a]) + "/code")
    try:
        modu = __import__(("fulloverride" + i["id"]))
        print(f"WARN: {i['name']} uses full overrides. Mods with full overrides may not be compatible with each other. Restarting...")
        reg = False
    except:
        print(str(i["name"]) + la["nofull"])
    try:
        modu.main()
    except:
        confusion +=1
    a +=1
while reg == True:
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
    if modsenabled:
        print(" ")
        cat = []
        a = 0
        for i in modmetas:
            cat.append(i["id"])
            sys.path.insert(1,str(mods[a]) + "/code")
            try:
                modu = __import__(("addons" + i["id"]))
            except:
                print(str(i) + la["nocom"])
            a +=1
            modu.extras(w)
        
    if command == True:
        print(la["cmds"])
        print(" ")
        print(" ")
        if incom == "//commands":
            print("commands, changelog, lang, dv, cc:<True/False>, st:<True/False>, resetvars, iweb, fstv<True/False>, fstve<True/False>, commandhelp, cv, echo<output>, log<output>, exper<True/False>, policy, modding, modinfo<id>")
        elif incom == "//changelog":
            print("3 - modding API, addons API, policies")
        elif incom == "//lang":
            print(la["complang"] + langname + " " + langper + " " + langcompat)
        elif incom == "//dv":
            print("DV 2.5 - Custom design possibilities with Modding API")
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
            webcheckversion = "3"
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
exper = enable experimental features(True/False)
policy = usage policy and EULA
modding = rules for modding
modinfo = supplies info for a mod(id)""")
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
        elif incom == "//policy":
            print("""Usage policy:

You may distribute on other trusted platforms not used by the creator, and modify and publish your modifications. However, you must credit the creator(LTIT), and the creator is not responsible for bugs on modified/externally distributed files, and damage, intentional or not, from these versions.


EULA:

Don'ts:
Modify to frame websites
Entirely rely on this thing, it may flag a scam site as legit
Claim that this does anything other than said in the info
Modify the log and claim that it was something outputted by the program
Generally misuse the program or do something you feel might not be right
Generally misuse modding the program

Dos:
Use to double check websites that may seem legit but you want to make sure
Use to mess around with the commands, I wonder what wc://crash does...
Use to check website statuses and wether they have ssl(https)

Info:
This isn't for telling you if a website is legit or not, only to reveal websites that look official and to check the status, and for some fun command stuff.""")
        elif incom == "//modding":
            print("""Modding rules:

Don'ts:
Modify the modding rules, usage policy or EULA, and translations and grammar fix mods to these elements MUST be fully accurate. You may not copyright your content.
Modify the systems to give false results
Add non-pg content to the mods
Make the mods malicious

Dos:
Be creative or add new features
Credit the creator
Use common sense to see if something may be right if not in the rules

Info:
If you disobey any rules, or the creator finds that the mods may not be appropriate, you must take your mod down, or make changes, if the creator requests.
I will try and notify the mod creator if I want a feature of their mod in the full program""")
        elif incom == "//mods":
            print(mods)
        elif sectorlist[1] == "//modinfo":
            for i in modmetas:
                if i["id"] == sectorlist[2]:
                    print("Name: " + i["name"])
                    print("Description: " + i["description"])
                    print("id: " + i["id"])
                else:
                    print(f"not {i['id']}")
        else:
            print(la["notfound"])
            cat = []
            a = 0
            for i in modmetas:
                cat.append(i["id"])
                sys.path.insert(1,str(mods[a]) + "/code")
                try:
                    modu = __import__(("addons" + i["id"]))
                except:
                    print(str(i) + la["nocom"])
                a +=1
                modu.commands(incom)
    print(" ")
    print(" ")
