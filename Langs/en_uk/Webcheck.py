#Web checker python 3.12 edition
#License: MIT
print("sl")
import json
lang = open("en_uk.json")
la = json.load(lang)
print(la['start_imports'])
import urllib.request
ac = 'qwertyuipopasdfghjklzxcvbnm:/#%1234567890."! @_()-QWERTYUIOPASDFGHJKLZXCVBNM'
print(la['finish_text'])
webcheckversion = "2"
print(la['start_texto'] + webcheckversion + la["start_textt"])
incom = ""
langname = "English(UK)"
langper = "100%(source lang)"
langcompat = "full"
ccenabled = True
stenabled = True
while True:
    incom = ""
    sectorlist = []
    command = False
    version = 0
    w = input(la["web_input_text"])
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
    if command == False and stenabled == True:
        system = bool(input(la["modeinput"]))
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
            except:
                print(la["noweb"])
            print(" ")
            try:
                st = urllib.request.urlopen(svers).status
                if st == 200:
                    print(svers + ' https' + la["statusup"] + str(st))
                else:
                    print(svers + ' https' + la["statusdown"] + str(st))
                sav = True
            except:
                print(la["nossl"])
        else:
            try:
                st = urllib.request.urlopen(svers).status
                if st == 200:
                    print(la["statusup"] + str(st))
                else:
                    print(la["statusdown"] + str(st))
                sav = True
            except:
                print(la["olderror"])
    elif command == True:
        print(la["cmds"])
        print(" ")
        print(" ")
        if incom == "//commands":
            print("commands, changelog, lang, dv, cc:<True/False>, st:<True/False>")
        elif incom == "//changelog":
            print("2.0 and 1.4.0 - localisation, ability to change between systems, commands")
        elif incom == "//lang":
            print(la["complang"] + langname + " " + langper + " " + langcompat)
        elif incom == "//dv":
            print("DV 2.1 - command syntax")
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
        else:
            print(la["notfound"])
    print(" ")
    print(" ")
