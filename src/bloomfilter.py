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
        pass

    def add (self, e):
        """
        Adds `e` to the Bloom filter.

        Args:
          e (any): The element to be added
        """
        pass

    def contains (self, e):
        """
        Returns True if `e` is stored in the Bloom filter

        Args:
          e (any): The element to be tested

        Returns:
          (bool): whether the element has (probably) been added to the Bloom filter
        """
        pass
    
    def __contains__(self, e):
        return self.contains(e)
