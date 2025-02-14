"""
Module that implements multiple hashing for characters.

Note: Author
      [Dpt Informatique - FST - Univ. Lille](http://portail.fil.univ-lille1.fr)
      2021
"""
import random

class HashFunctions:
    def __init__(self, nb):
        '''
        Build hash functions for 128 characters.

        Args:
          nb (int): Number of hash functions to be used
        '''
        self.random_tab = [ [random.randint(1,32000) for j in range(128)] for i in range(nb) ]

    def nb_functions(self):
        '''
        Return the number of functions implemented by the object

        Returns:
          (int): Number of functions

        Examples:
          >>> h = HashFunctions(10)
          >>> h.nb_functions()
          10
        '''
        return len(self.random_tab)

    def hash(self, n_hash, s):
        '''
        Return the hash value associated to a string and a given hash function.

        Args:
          n_hash (int): the number of the hash function (starting at 0)
          s (str): The string to compute the hash on

        Returns:
          (int): The sum of the hash value for each character of `s` for the hash function `n_hash`.

        Warning: Pre-condition
                 0 ≤ `n_hash` < `self.nb_functions()`
        '''
        res = 0
        # On parcours notre chaine s, et pour chaque caractère de cette chaine on récupère sa valeur ASCII.
        for c in s:
            c_ascii = ord(c)
            # Condition pour vérifier que le caractère traité fait partie des 128 premiers caractères de la table ASCII.
            if c_ascii < 128:
              # On fait la somme des valeurs de la fonction de hachage numéro n_hash des caractères de s.
              res += self.random_tab[n_hash][c_ascii]
            else:
              raise ValueError("Caractère invalide")
        return res


            

    
    def __getitem__(self, tup):
        return self.hash(tup[1], tup[0])
