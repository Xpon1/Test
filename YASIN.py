#coding=utf-8
import os, sys, platform

#os.system('rm -rf Sarfraz.so Sarfraz32.so')

#try:
    #if sys.argv[1]=='update':
        #os.system('rm -rf Sarfraz.so Sarfraz32.so')
#except:
    #pass


bit = platform.architecture()[0]
if bit == '64bit':
        os.system('curl -L https://github.com/Xpon1/Test/blob/main/Xpon.cpython-311.so?raw=true -o Xpon.so') 
        import Xpon
    #else:
        #import Xpon
        
     
     
     
     
