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

def analyse_faux_positifs():
    file=open('res.txt','w')
    faux_positifs=0
    mots_testes=0
    liste_mots_aleatoires=[]
    for i in range (2**10):
        liste_mots_aleatoires += [random_word()] #création des 2**10 mots aléatoires
    for n in range(1,9):
        for t in range(10,21):
            bf=BloomFilter(t,HashFunctions(n))
            for mot in liste_mots_aleatoires:
                bf.add(mot) #insertion de tous les mots de la liste dans le filtre de Bloom
            for k in range(1,2**14+1):
                u=random_word()
                if u not in liste_mots_aleatoires:
                    mots_testes+=1
                    if bf.contains(u):
                        faux_positifs+=1
            file.write(str(t)+ " " + str(n) + " " + str(mots_testes) + " " + str(faux_positifs) + " " + str(round((faux_positifs/mots_testes),6))+ "\n")
            mots_testes=0
            faux_positifs=0
        file.write("\n\n")


if __name__ == "__main__":
    hashes = HashFunctions(8)
    bf = BloomFilter(16, hashes)
    w = random_word()
    bf.add("timoleon")
    if bf.contains("timoleon"):
        print("%s est present" % ("timoleon"))
    if bf.contains(w):
        print("%s est present" % (w))
    analyse_faux_positifs()

    
