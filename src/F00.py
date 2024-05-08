# =================== DONE =======================

# nama / nim    : Alfian Hanif FY / 19623281
# judul         : Random Number Generator
# deskripsi     : memberi angka secara acak dalam range tertentu

# algoritma
import os
import time

# menggunakan lcg algorithm untuk mendapat pseudo random number
def lcg():                         
    m = 2**31                  
    a = 22695477
    c = 1
    seed = int(os.getpid() + time.time()*13)         
    return(((a*seed + c)%m)/(m))                # menghasilkan nilai (0 , 1]
    

def randInRange(start:int,end:int):
    return(int(start + lcg() * (end-start)) )

