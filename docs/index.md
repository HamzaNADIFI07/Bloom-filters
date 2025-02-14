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

#### Q3:

Pour trouver une taille du filtre pour laquelle un mot tiré au hasard apparaît présent, ce qui veut dire qu'on a un faux positif, après avoir tester plusieurs valeurs de **n**, je n'ai réussi d'obtenir aucun **faux positif**, donc j'ai décider de modifier un peu le code de test du fichier `test.py` pour automatiser cette recherche de la taille du filtre avec le code suivant:

```python
if __name__ == "__main__":
    for i in range(21):
        hashes = HashFunctions(2**i)
        bf = BloomFilter(16, hashes)
        w = random_word()
        bf.add("timoleon")

        if bf.contains(w):
            print("%s est present avec i=%s" % (w , i))
            break
```
Avec ce code qui permet de tester les **21** premiers **(de 0 à 20)** taille du filtre, j'ai pu obtenir ce résultat:
```bash
src % python3 test.py
dheUCve est present avec i=20
```
Après un deuxième teste, j'ai pu obtenir ce résultat:
```bash
src % python3 test.py
DkaINUva est present avec i=20
```
Donc taille du filtre pour laquelle un mot tiré au hasard apparaît présent, ce qui veut dire qu'on a un faux positif est **`2^20`** donc **`n=20`**.

