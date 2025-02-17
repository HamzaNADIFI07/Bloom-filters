# -*- coding: utf-8 -*-

"""

Module that implements a Bloom filter.

Note: Author
      [Dpt Informatique - FST - Univ. Lille](http://portail.fil.univ-lille1.fr)
      2021
"""
import hash_functions

class BloomFilter:
    
    def __init__ (self, n, hashes):
        """
        Creates a new empty Bloom filter of size $2^n$
        
        Args:
          n (int): the log of the size of the filter (the filter will be of size $2^n$)
          hashes (HashFunctions): the hash functions
        """
        self.n = n # Le log de la taille du filtre
        self.hashes = hashes # La fonction de hachage
        self.size=2**n # La taille du filtre `2^n`
        self.table = [False for i in range(self.size)] # On initialise tous les cases de la table à False


    def add (self, e):
        """
        Adds `e` to the Bloom filter.

        Args:
          e (any): The element to be added
        """
        for i in range (self.hashes.nb_functions()):
            a=self.hashes.hash(i,e) % self.size
            self.table[a]=True


    def contains (self, e):
        """
        Returns True if `e` is stored in the Bloom filter

        Args:
          e (any): The element to be tested

        Returns:
          (bool): whether the element has (probably) been added to the Bloom filter
        """
        for i in range(self.hashes.nb_functions()):
          res = self.hashes.hash(i, e) % self.size
          if not self.table[res]:
            return False
        return True

    
    def __contains__(self, e):
        return self.contains(e)
