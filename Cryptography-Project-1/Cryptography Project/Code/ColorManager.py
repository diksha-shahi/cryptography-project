class ColorManagerA:
    def __init__(self, Xorkey):
        self.Xorkey = Xorkey

        portionB =  self.Xorkey[12:]
        self.r = int(portionB) + int(self.Xorkey[0:4])
        self.r = self.r % 256

        self.g = int(portionB) + int(self.Xorkey[4:8])
        self.g = self.g % 256

        self.b = int(portionB) + int(self.Xorkey[8:12])
        self.b = self.b % 256

    def colorEncode(self, colorFlag, data):

        #break the byte into nibble
        row = data & 240 # 11110000
        row = row >> 4
        col = data & 15 #00001111



        baseNumber = 0
        if colorFlag == 1:
            baseNumber = self.r
        elif colorFlag == 2:
            baseNumber == self.g
        else:
            baseNumber = self.b


        number = baseNumber + row * 16 + col
        number = number % 256
        return number

    def colorDecode(self, colorFlag, number):

        baseNumber = 0
        if colorFlag == 1:
            baseNumber = self.r
        elif colorFlag == 2:
            baseNumber == self.g
        else:
            baseNumber = self.b


        temp = number - baseNumber + 256
        temp = temp % 256

        row = temp // 16
        col = temp % 16

        #merge the row and col to get the data
        #cleanup
        row = row & 15 #00001111
        col = col & 15 #00001111

        data = row << 4 | col

        return data

