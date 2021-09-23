# İkiklik Sayı Sistemi Çevirici

def ReverseText(text):
    reservedText = ""

    i = len(text) - 1
    while i >= 0:
        reservedText += text[i]
        i -= 1

    return reservedText


def ConvertBinaryDigit(number):
    binary = ""
    byteSize = 8

    while True:
        if number == 1 or number == 0:
            binary += str(number)
            break
        bit = number % 2
        binary += str(bit)
        number //= 2

    binary = ReverseText(binary)
    
    zeroLength = byteSize - len(binary)
    zeros = ""
    for i in range(zeroLength):
        zeros += "0"

    binary = zeros + binary
    return binary

data = int(input("Enter Data: "))
bayt = ConvertBinaryDigit(data);
print(f"{data}'s equivalent in the binary number system:\n{bayt}")