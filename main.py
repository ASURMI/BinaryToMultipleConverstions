#####################################################################################################################

# Calculate the amount of letters inside the inputted binary.
def calcLenOfBin(binary):
    convertToString = str(binary)
    calcLenOfBin = len(convertToString)
    return calcLenOfBin

# Conversion from binary to decimal to octal using python function oct.
def convertOctal(binary):
    num = convertDecimal(binary)
    return oct(num)

# Conversion from binary to decimal to hexadecimal using python function hexa.
def convertHexadecimal(binary):
    num = convertDecimal(binary)
    return hex(num)

# Conversion from binary to decimal using the base 2 of the python function int.
def convertDecimal(binary):
    return int(binary, 2)

# Constructor
if __name__ == '__main__':
    initiated = True
    # While loop to ask for input and desired output.
    while initiated:
        binary = input("Enter the Binary: ")
        lenOfBin = calcLenOfBin(binary)
        if lenOfBin > 8:
            print("ERROR: Input a max of 8 digits!")
            continue
        else:
            print("Select what binary conversion you want: "
                  "\n1. Decimal"
                  "\n2. Hexadecimal"
                  "\n3. Octal"
                  "\n4. All")
            selection = input("SELECTION: ")
            if int(selection) == 1:
                print("Conversation: ", convertDecimal(binary))
            elif int(selection) == 2:
                print("Conversation: ", str(convertHexadecimal(binary)).replace("0x", "").upper())
            elif int(selection) == 3:
                print("Conversation: ", convertOctal(binary))
            elif int(selection) == 4:
                print("The binary value of ", binary, "is:"
                                                      "\nDecimal: ", convertDecimal(binary),
                      "\nHexadecimal: ", str(convertHexadecimal(binary)).replace("0x", "").upper(),
                      "\nOctal: ", convertOctal(binary).replace("0o", "").upper())

            initiated = False

#####################################################################################################################