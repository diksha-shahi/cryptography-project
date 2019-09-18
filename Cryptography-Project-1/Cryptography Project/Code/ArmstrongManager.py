class ArmstrongManagerA:
    #class level data member
    armstrongNumber = [153, 370, 371, 407] #armstrong number list
    baseTable = [1234, 1243, 1324, 1342, 1423, 1432, 2134, 2143, 2314, 2341, 2413, 2431, 3124, 3142, 3214, 3241, 3412, 3421, 4123, 4132, 4213, 4231, 4312, 4321] #permutation list

    @classmethod
    def _convertKeyToNumber_(cls, key):
        total = 0
        i = 0
        keyLen = len(key)

        while i < keyLen:
            total += ord(key[i])  # ASCII = ord(char)
            i += 1

        # total has the sum of elements of key
        return total


    @classmethod
    def _generatePermuatationKey_(cls, num):

        # select a permutation based on the sum
        permutation = cls.baseTable[num % len(cls.baseTable)]
        # permuation = table[4] = 1423

        #print("num ", num)
        #print("permutation ", permutation)

        xorKey = ''
        # generate permuatation key
        while permutation > 0:
            digit = permutation % 10 -1
            xorKey = str(cls.armstrongNumber[digit]) + xorKey
            permutation = permutation// 10 #integer division

        xorKey = xorKey + str(num)

        return  xorKey

    @classmethod
    def generateXORKey(cls, key):

        #convert key to a number
        num = cls._convertKeyToNumber_(key)
        #say num is 1732
        xorKey = cls._generatePermuatationKey_(num)
        #print(xorKey)
        return  xorKey

