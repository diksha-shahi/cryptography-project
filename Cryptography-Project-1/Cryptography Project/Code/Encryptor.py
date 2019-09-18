import os
import ArmstrongManager
import ColorManager

class EncryptorA:

    def __init__(self, k):
        #data members
        self.key = k
        self.XorKey = ArmstrongManager.ArmstrongManagerA.generateXORKey(self.key)
        self.cMgr = ColorManager.ColorManagerA(self.XorKey)

    def encrypt(self, srcFile, trgtFile):
        status = 0
        fhSrc = None
        fhTrgt = None
        try:
            if os.path.exists(srcFile):
                #open the source file for reading
                fhSrc = open(srcFile, "rb")

                #open the target file for writing
                fhTrgt = open(trgtFile, "wb")

                #encrypt
                flag = True
                i = 0
                cFlag = 1

                length = len(self.XorKey)
                encoded = bytearray()

                while flag:
                    #read a chunk of 2048 or less bytes from the source file
                    buff = fhSrc.read(2048)

                    if buff: #if binary object is not empty

                        for abyte in buff:
                            # armstrong encrypt
                            enc1 = abyte ^ int(self.XorKey[i])
                            i += 1
                            i %= length

                            #color encode
                            enc2 = self.cMgr.colorEncode(cFlag, enc1)
                            cFlag = cFlag % 3 +1

                            encoded.append(enc2)


                        #writeback as encrypted
                        fhTrgt.write(encoded)
                        #prepare for next chunk
                        encoded.clear()
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
            if fhSrc is not  None:
                fhSrc.close()
            if fhTrgt is not  None:
                fhTrgt.close()

            return  status #0,1,2,3


