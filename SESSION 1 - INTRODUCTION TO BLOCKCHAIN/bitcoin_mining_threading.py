# -*- coding: utf-8 -*-
"""
Mining Bitcoin with Multi-Threading
@author: Manoel Gadi - 23/Oct/2021
"""



import threading
from hashlib import sha256
MAX_NONCE = 100000000000
NTHREADS = 50

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros,START_NONCE=0):
    prefix_str = '0'*prefix_zeros
    END_NONCE = int(START_NONCE+MAX_NONCE/NTHREADS)
    for nonce in range(START_NONCE,END_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")

def do_mining(START_NONCE=0):
    transactions='''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    difficulty=6 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty, START_NONCE)
    total_time = str((time.time() - start))
    print(f"end mining. Mining took: {total_time} seconds")
    print(new_hash)
    
threads = []
# t = threading.Thread(target=do_mining, args=(int(0*MAX_NONCE/NTHREADS),))
# t.daemon = True
# threads.append(t)
# threads[0].start()
# threads[0].join()


for i in range(NTHREADS):
    t = threading.Thread(target=do_mining, args=(int(i*MAX_NONCE/NTHREADS),))
    t.daemon = True
    threads.append(t)
    
for i in range(NTHREADS):
    threads[i].start()

for i in range(50):
    threads[i].join()
    