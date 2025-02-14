# Tp Bloom


## État du TP

Décrivez ici l'état d'avancement du TP.

## Réponses aux questions

Indiquez ici les réponses aux questions posées dans le TP. Vous
reprendrez le numéro de la section et le numéro de la question. Par
exemple pour répondre à la question 3 de la section 2.4 vous indiquerez :

### La classe BloomFilter du module bloomfilter

#### Q2:
Après avoir implémenter la méthode `hash()` de la classe `HashFunctions`, ainsi que le constructeur et les deux méthodes `add()`et `contains()` de la class `BloomFilter`.

On a testé nos fonctions en utilisant le programme de test déjà écrit qui insère le mot **"timoleon"** puis teste sa présence dans le filtre et la présence d'un mot aléatoire avec la commande suivante:

```bash
src % python3 test.py
```
Et on a eu le résultat suivant:
```bash
timoleon est present
```
Après avoir ajouter cette ligne aussi au programme de test du fichier `test.py`, et qui permet de rajouter le mot aléatoire génerer par la fonction `random_word()`, pour pouvoir tester sa présence dans le filtre :
```python
if __name__ == "__main__":
    hashes = HashFunctions(8)
    bf = BloomFilter(16, hashes)
    w = random_word()
    bf.add("timoleon")
    bf.add(w) # LIGNE RAJOUTÉE
    if bf.contains("timoleon"):
        print("%s est present" % ("timoleon"))
    if bf.contains(w):
        print("%s est present" % (w))
```
On a eu le résultat suivant :
```bash
timoleon est present
IQufLUs est present
```
Et qui permet de conclure que: 

- La fonction `random_word()` permet bien génerer un mot compris entre 4 et 7 lettres. 

- La fonction `add()` permet bien de rajouter un élement au filtre.

- La fonction `contains()` permet bien de vérifier la présence d'un élement dans le filtre.


