#Web checker python 3.12 edition
ac = 'qwertyuipopasdfghjklzxcvbnm:/#%1234567890."!'
import urllib.request
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
        print("The bad characters are: " + str(ic) + ". Please read the instructions for more info")
    print(" ")
    print(" ")
    st = urllib.request.urlopen(w).status
    if st == 200:
        print(f'{w} status: up')
    else:
        print(f'{w} status: unknown or down')
    print(" ")
    print(" ")
