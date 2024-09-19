import socket
import os

asnii_a=ord('a')# <- it's an asnii character variable
asnii_z=ord('z')

detal=ord('a')-ord('A')# the difference

asnii_A=asnii_a-detal
asnii_Z=asnii_z
asnii_Z-=detal# asnii_Z=asnii_Z-detal


if(__name__=="__main__"):#<- starting point
    hostname=socket.gethostname()

    #output formal: PY{password}

    print("password: PY{",end='')#output: PY{ 

    #password
    #Caesar cipher: A->J
    for asnii in hostname:

        #Caesar cipher(A->J)=> "hxd wnnm jmm cqnbn lxmn:"

        # asnii=ord(asnii)
        # IF ( asnii>=asnii_a and asnii<=asnii_z ):#if the asnii character is between 'a' and 'z'
        #     asnii=chr(( asnii-asnii_a +9)%26+asnii_a)
        #     pass
        # elif ( asnii>=asnii_A and asnii<=asnii_A ):#or between 'A' and 'Z'
        #     asnii=chr(( asnii-asnii_A +9)%26+asnii_A)
        #     pass

        print(asnii,end='')
        pass

    print("}")#output:  }
    os.system("pause")
    pass
