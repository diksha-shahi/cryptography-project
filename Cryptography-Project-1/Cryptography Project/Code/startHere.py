import Encryptor
import Decryptor
import time

#import dbm
#import random

def main():

    e = Encryptor.EncryptorA("how old is my computer")
    d = Decryptor.DecryptorA("how old is my computer")

    print(time.time())
    flag = e.encrypt("e:\\k.jpg", "e:\\k99.jpg")#("e:\\b.mp4", "e:\\b99.mp4")
    print(time.time())

    if flag == 3:
        flag = d.decrypt("e:\\k99.jpg", "e:\\kagain.jpg")#("e:\\b99.mp4", "e:\\bAgain.mp4")
        print(time.time())
        if flag == 3:
            print("DONE")

    #dbm module provides a persistent dictionary (key - value pair)
    #create/open a dictionary
    #param1 : dictionary store
    #param2 : mode
    # r : reading
    # w : writing and reading
    # c : create, write and read (doesnt overwrite)
    # n : create as new, write and read (overwrite)
    #store = dbm.open("e:\\users", "c")

    #add key-value pairs
    #store['bijendra'] = '11112222'
    #store['dev'] = '22223333'
    #store['pankaj'] = '33334444'
    #store['dev'] = '88889999' #overwrite the pair
    #store['dummy'] = 'test'

    #delete a key-value pair
    #try:
    #    del(store['dummy'])
    #    print('Dummy entry removed')
    #except (KeyError):
    #    print('Dummy entry not found')


    #read the dictionary
    #for auser in store.keys():
        #print(auser , ' : ', store[auser])


    #x = input('enter user name ')
    #try:
        #store[x] returns the value as binary object
        #decode() on the binary objects returns the ASCII equivalent of the bytes of the binary object

        #y = store[x].decode()
        #generate a random int value in range 1000 to 9999
        #otp = random.randint(1000, 10000)

        #print(otp ,'sent to phone number : ',y )

    #except (KeyError):
        #print(x +' not found')

    #store on disk
    #store.close()


main()
