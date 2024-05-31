#Web checker python 3.12 edition
print("Starting p1")
ac = 'qwertyuipopasdfghjklzxcvbnm:/#%1234567890."! @_()-'
import urllib.request
print("Finish")
print("Webcheck v1.1.0 in python")
while True:
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
    try:
        st = urllib.request.urlopen(w).status
        if st == 200:
            print(f'{w} status: up({st})')
        else:
            print(f'{w} status: unknown or down({st})')
    except:
        print("Couldn't find the website, or the certificate is incorrect. If you have definitely spelt it correctly, this could be a red flag.")
        print("One fix is to use http instead of https, if they haven't got an ssl certificate.")
    print(" ")
    print(" ")
