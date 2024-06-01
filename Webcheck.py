#Web checker python 3.12 edition
#License: MIT
print("Starting p1")
ac = 'qwertyuipopasdfghjklzxcvbnm:/#%1234567890."! @_()-'
import urllib.request
print("Finish")
print("Webcheck v1.1.0 in python")
while True:
    version = 0
    w = input("Website to check (read instructions): ")
    ic = []
    icr = "failed"
    ica = 0
    ics = "Pass"
    print(" ")
    for i in range(0, len(w)):
        if w[i] in ac:
            ica += 0
        else:
            ica += 1
            ics = "Fail"
            ic += w[i]
    icr = "succeeded"
    print("Character check " + str(icr) + " with a result of " + str(ics) + " and " + str(ica) + " bad characters")
    if ica > 0:
        print("The bad characters are: " + str(ic) + ".")
        i = input("Press i for more info, otherwise press anything else: ")
        if i == "i":
            print("Sites may use characters from other languages that look like latin characters, and this makes them look legit. However, they aren't the same as the real website.")
    print(" ")
    print(" ")
    sectorlist = w.split(":")
    if sectorlist[0] == "http":
        version = 4
    else:
        version = 5
    unsvers = "http" + w[version:len(w)]
    svers = "https" + w[version:len(w)]
    unsav = False
    sav = False
    try:
        st = urllib.request.urlopen(unsvers).status
        if st == 200:
            print(f'{w[(version + 3):len(w)]} http status: up({st})')
        else:
            print(f'{w[(version + 3):len(w)]} http status: unknown or down({st})')
        unsav = True
    except:
        print("Couldn't find website")
    print(" ")
    try:
        st = urllib.request.urlopen(svers).status
        if st == 200:
            print(f'{w[(version + 3):len(w)]} https status: up({st})')
        else:
            print(f'{w[(version + 3):len(w)]} https status: unknown or down({st})')
        sav = True
    except:
        print("https not available")
    print(" ")
    print(" ")
