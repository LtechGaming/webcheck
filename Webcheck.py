#Web checker python 3.12 edition
#License: MIT
import urllib.request
print("sl")
import json
lang = open("en_uk.json")
la = json.load(lang)
print(la['start_imports'])
ac = 'qwertyuipopasdfghjklzxcvbnm:/#%1234567890."! @_()-'
print(la['finish_text'])
print(la['start_text'])
while True:
    version = 0
    w = input(la["web_input_text"])
    ic = []
    icr = la["failed"]
    ica = 0
    ics = la["pass"]
    add = ""
    print(" ")
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
            print(unsvers + 'http '+ la["statusup"] + str(st))
        else:
            print(unsvers + 'http ' + la["statusdown"] + str(st))
        unsav = True
    except:
        print(la["noweb"])
    print(" ")
    try:
        st = urllib.request.urlopen(svers).status
        if st == 200:
            print(svers + 'https ' + la["statusup"] + str(st))
        else:
            print(svers + 'https ' + la["statusdown"] + str(st))
        sav = True
    except:
        print(la["nossl"])
    print(" ")
    print(" ")
