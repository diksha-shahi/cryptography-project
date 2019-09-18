import os
import ArmstrongManager
import ColorManager

class DecryptorA:

    def __init__(self, k):
        #data members
        self.key = k
        self.XorKey = ArmstrongManager.ArmstrongManagerA.generateXORKey(self.key)
        self.cMgr = ColorManager.ColorManagerA(self.XorKey)

    def decrypt(self, encodedFile, orgiginalFile):
        status = 0
        fhSrc = None
        fhTrgt = None
        try:
            if os.path.exists(encodedFile):
                #open the encoded file for reading
                fhEncoded = open(encodedFile, "rb")

                #open the original file for writing
                fhOriginal = open(orgiginalFile, "wb")

                #decrypt
                flag = True
                i = 0
                cFlag = 1

                length = len(self.XorKey)
                decoded = bytearray()

                while flag:
                    #read a chunk of 2048 or less bytes from the source file
                    buff = fhEncoded.read(2048)

                    if buff: #if binary object is not empty

                        for abyte in buff:
                            # color decode
                            dec2 = self.cMgr.colorDecode(cFlag, abyte)
                            cFlag = cFlag % 3 + 1

                            # armstrong encrypt
                            dec1 = dec2 ^ int(self.XorKey[i])
                            i += 1
                            i %= length


                            decoded.append(dec1)


                        #writeback as encrypted
                        fhOriginal.write(decoded)
                        #prepare for next chunk
                        decoded.clear()
                    else:
                        flag = False

                status = 3 #success

            else:
                status = 0 #src file not found

        except IOError :
                status = 1 # IO Error
        except:
                status = 2 # Other Error
        finally:
            if fhEncoded is not  None:
                fhEncoded.close()
            if fhOriginal is not  None:
                fhOriginal.close()

            return  status #0,1,2,3


