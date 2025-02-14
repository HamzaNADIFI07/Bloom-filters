# -*- coding: utf-8 -*-

import random
from hash_functions import HashFunctions
from bloomfilter import BloomFilter

def random_word ():
    """
    Returns:
      (str): a word with random letters whose length is between 4 and 7.
    """
    letters = [ chr(i) for i in range(ord('a'),ord('z')+1) ] + [ chr(i) for i in range(ord('A'),ord('Z')+1) ]
    length = 4 + random.randint(0,4)
    str = ""
    for i in range(length):
        str = str + random.choice(letters)
    return str

if __name__ == "__main__":
    for i in range(10,21):
        hashes = HashFunctions(2**i)
        bf = BloomFilter(16, hashes)
        w = random_word()
        bf.add("timoleon")

        if bf.contains(w):
            print("%s est present avec i=%s" % (w , i))
            break

    
