
## INTRODUCTION A PYTHON

![logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

### PRESENTATION

Python est un langage de programmation interprété (langage de script) multiplatforme.

Il est doté d'un typage dynamique fort, d'une gestion automatique de la mémoire par ramasse-miettes et d'un système de gestion d'exceptions.  
Ses fonctionnalités haut niveau et sa syntaxe très simple en font un langage très facile a appréhender.

Tous ces atouts font de lui un langage très populaires (3° place au moment ou nous parlons), surtout auprès des universitaires qu'ils l'on largement utilisé pour développer des outils dans le domaine de le la data science et de l'intelligence artificielle.  
C'est un langage incontournable dans ces 2 domaines aujourd'hui mais il est également largement utilisé dans les domaines du web, du jeu vidéo, de la robotique et de l'IOT.

### LES VERSIONS DE PYTHON

La dernière version au moment ou nous parlons est la 3.9 (latest) mais elle est plutôt envisagé en mode dev.

Les versions préférées pour leur stabilité (prod) sont la 3.7 ou la 3.6.

La version 2.7 qui a été préférée pendant (très) longtemps par les développeur pour sa formidable stabilité est en déprécated et doit être évitée.

Toutes ces version de python sont disponibles en téléchargement [ici](https://www.python.org/downloads/)  
Pour Linux ces versions sont également disponibles sur les dépot apt, yum ...

### ECRIRE DU CODE PYTHON

#### DANS LA CONSOLE

Après installation, la console python est disponible via la commande `python` ou `python3` dans le terminal

L'interpréteur python se lance et nous donne la possibilié d'écrire et d'éxecuter du code python dans le terminal.

```bash
(base) florent@florent-Asus-New:~$ python
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("hello world") # utilisation de la fonction de flux sortant print()
hello world
>>> exit()
```

#### DANS UN FICHIER

On peut (doit) intégrer notre code dans un fichier portant l'extension `.py` (par convention)  
On peut ensuite l'exécuter en lancant la commande `python mon_fichier.py`

* Ecrire dans hello.py

```python
print("hello world")
```

* Execution hello.py
  
```bash
(base) florent@florent-Asus-New:~$ python hello.py
hello world
```

### LES VARIABLES

Le typage dynamique fort du langage a 2 avantages importants :
* il n'est pas necessaire de definir le type de variable avant de lui attribuer une valeur, il est automatiquement definie par l'interpréteur.
* le type de la variable peut être modifié pendant le processing.

#### VARIABLES NUMERIQUES

Les variable numérique peuvent être de type ***int***, ***float*** ou **complex**.
Il peuvent prendre une valeur positive ou négative.

Les type ***int** peuvent également prendre une valeur binaire ou hexadécimale.

``` python
ma_var = 1 # variable type int positive
ma_var = -5 # variable int negative

ma_var = 2e2 # float 200.0
ma_var = .1 # variable de type float
ma_var = 2e-2 # float .02

ma_var = 0b110 # int 6
ma_var = 0xFF # int 255
```

#### CARATERES ET STRING

La valeur des chaines de caractères sont déclaré entre " ou ' (pour sigle lines).  
On peut déclarer une chaine multiline entre triple quote `"""`.

```python
ma_var='a' # variable caractere
ma_var='1' # variable caractere num
ma_var="chaine de caractere" # variable string
ma_var='chaine de caractere' # variable string 
ma_var = """chaine de caractere 
sur plusieurs lignes"""
```
Certain charactères nécessitent un séquence d'échappement pour être interprétés.

Séquences d'échappement :
|Sequence|Description|
|-|-|
|\\\\|Backslash|
|\\'|Guillemet simple (apostrophe)|
|\\"|Guillemet double|
|\\n|Saut de ligne|
|\\r|Retour chariot|
|\\t|Tabulation horizontale|

#### LES BOOLEAN

```python
# variable booleenne, attention majuscule à True et False
ma_var=True
ma_var=False
``` 

#### LA VALEUR NONE

On utilise le mot clé ***None*** pour définir une variable sans valeur.

```python
ma_var=None
```

#### LES CONTAINERS

En programmation, les containers sont des objets pouvant contenir une suite d'éléments.  
Le typage dynamique fort de python nous permet d'intégrer dans ces container tous types de variables et faire cotoyer des variables de types différents.

En python, il existe en natif 4 types de containers intégrés en natif :
* les listes : objet ***list*** 
* les tuples : objet ***tuple***
* les ranges : objet ***range***
* les set : objet ***set***
* les dictionnaires : objet ***dict***

##### LES LISTES

L'objet **list** permet de contenir une série d'éléments dans une ordre défini.

```python
ma_list = [1,2,'trois']
print(ma_list)
# [1,2,'trois']
```

Les listes sont modifiables et extensibles.  
On accède à un élément d'une liste en utilisant son index.

```python
ma_list = [1,2,'trois']
print(ma_list[2]) # affichage de l'index 2
# trois
ma_list[2]=3 # remplacement de l'index 2
print(ma_list)
# [1,2,3]
```

On peut récupérer une partie de la liste en utilisant une plage d'index.

```python
a=[1,2,3,4,5]

print(a[1:4]) #affichage de l'index 1 (inclusif) jusqu'à l'index 4 (exclusif)
# [2, 3, 4]

print(a[2:]) #affichage de l'index 2 (inclusif) jusqu'à la fin du tableau
# [3, 4, 5]

print(a[:3]) #affichage du debut du tableau  jusqu'à l'index 3 (exclusif)
# [1, 2, 3]

b = a[2:] # copie d'une partie de a dans b
print(b)
# [3, 4, 5]
```

On peut également utiliser les méthodes de **list** pour effectuer des actions sur la liste comme :
* ajouter une élément à la fin de la liste : ***append()***
* extraire un élément de la liste : ***pop()***
* trier les éléments : ***sort()***
* ... (liste des méthodes disponible [ici](https://www.w3schools.com/python/python_ref_list.asp))
 

```python
a=[1,3,'un',2]

a.append(4) # ajout de 4 à la fin de la liste
b = a.pop(2) # extrait de l'index 2
print(b)
# un

a.sort(reverse=True) # tri de la liste en mode reverse | attention fonction mutable
print(a)
# [4, 3, 2, 1]
```

##### LES TUPLES

Le ***tuple*** permet contenir un série d'éléments dans un ordre défini.  
Comme les listes, les éléments d'un tuples sont également accessible avec son index et une plage d'index permet de récupérer une partie du tuple.

Mais contrairement aux listes, les tuples ne sont pas modifiables.

```python
a=(1,2,3,4,5) # ou a=tuple([1,2,3,4,5])
print(a[1])
# 2
print(a[3:])
# (4, 5)

a[1] = 'obi' # on essai de remplacer l'élément à l'index 1
# TypeError: 'tuple' object does not support item assignment
```

##### LES RANGES

Les ranges représentent une suite de nombre ordonnée définie par 
* une valeur de début
* une valeur de fin 
* le step optional
ou
* un nombre de valeurs (commence à 0 et incrémente de 1 jusqu'à obtenir le nombre de valeur)
  
On les utilise principalement pour définir le valeurs d'itération dans une boucle ***for***.

```python
a = range(0, 10, 2) # range allant de 0 à 10 avec un step de 2.
print(list(range)) # conversion en int et affichage
# [0, 2, 4, 6, 8]

a = range(10)
print(list(range))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

##### LES SET

Les ***set*** sont conçu pour contenir une serie d'éléments uniques.  
contrairement au objets ***list*** et ***tuple***, un objet ***set*** n'est pas ***subscriptable*** (on ne peut pas accéder aux élément via un index).

```python
a = {1,2,3,4,2,1,4,5} # ou a=set([1,2,3,4,2,1,4,5])
print(a)
# {1, 2, 3, 4, 5}
```
Le ***set*** est modifiable via ses méthodes :
* ajout d'un élément (si non présent): add()
* suppression d'un élément : remove() ou discard()
* ... (liste des méthodes disponibles [ici](https://www.w3schools.com/python/python_ref_set.asp))

```python
a = {'alpha','bravo', 'charlie', 'delta'}

a.add('echo') # ajout de echo
print(a)
# {'alpha', 'charlie', 'bravo', 'delta', 'echo'}

a.remove('bravo')
print(a)
# {'alpha', 'charlie', 'delta', 'echo'}
```

##### LES DICTIONNAIRES

Les ***dict*** permettent de stocker des éléments au format ***clé : valeur***.  
Les valeurs du ***dict** sont accessibles en utilisant la clé.  
Chaque clés du dictionnaire doit être unique.  
On peut également ajouter un nouvel ensemble ***clé : valeur*** en utilisant la formulation `mon_dict[clé] = valeur`.


```python
a={
    'a':'alpha',
    'b':'bravo',
    'c':'charlie'
}

print(a['a'])
# alpha

a['d'] = 'delta'
print(a)
# {'a': 'alpha', 'b': 'bravo', 'c': 'charlie', 'd': 'delta'}
```

L'objet ***dict*** dispose d'un ensemble de méthodes permettant sa modification ou la récupération de ses élément :
* recupération liste de tuple (clé, valeur) : items()
* extraction d'une valeur : pop()
* ... (liste des méthodes disponibles [ici](https://www.w3schools.com/python/python_dictionaries_methods.asp)

```python
a={
    'a':'alpha',
    'b':'bravo',
    'c':'charlie'
}
print(a.items())
# dict_items([('a', 'alpha'), ('b', 'bravo'), ('c', 'charlie')])

b = a.pop('b')
print(b)
# bravo
```

##### LES ITERABLES

Tous les objets de container vu précédemment sont des ***iterables***.  
Les ***itérables*** sont des objets de type container dans lequels sont implémenté des fonctions spécifique qui vont permettre :
* de le parcourir via une boucle ***for***.
* d'accéder à un éléments via son index.
* d'appliquer des fonctions natives permettant sur l'objet ou son élément :
  * recuperer sa taille : len()
  * renvoyer les élément sous un format (index, valeur) : enumerate()
  * de modifier chaque element en appliquant un processing : map() ...
  
```python
a = ['a','b','c','d']
len(a)
# 4

list(enumerate(a))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

list(map(lambda x:x+":", a))
# ['a:', 'b:', 'c:', 'd:']
```

#### RECUPERER LE TYPE

On peut récupérer le type d'une variable en utilisant la méthode ***type()***.

```python
ma_var=0b110
type(ma_var)
# <class 'int'>

ma_var=None
type(ma_var)
# <class 'NoneType'>
```

### FONCTIONS DE CONVERSION : CAST 

#### FONCTION INT()

La fonction int permet de convertir une valeur de type float ou str en int.

* cast float => int
```python
a = 6.7
int(a)
# 6
```

* cast str => int

La conversion de _string_ vers _int_ peut prendre un deuxième paramêtre décrivant la base de numérique (2, 10 ou 16).  
On peut donc convertir une représentation binaire, décimale ou héxadecimale au format string en int en définissant la base.
Par défaut la base est 10.

* cast string decimal => int
```python
a = '110'
int(a) # ou int(a, 10)
# 110
```

* cast string binaire => int
```python
a = '110'
int(a, 2)
# 6
```

* cast string hexadecimale => int
```python
a = '110'
int(a, 16)
# 272
```

#### FONCTION FLOAT()

La fonction float permet de convertir une valeur de type string ou int en float

* cast int => float
```python
a = 6
float(a)
# 6.0
```

* cast str => float

```python
a='6.7'
float(a)
# 6.7
```

#### FONCTION STR()

La fonction str() permet de convertir des valeur de type int ou float en string.

* cast float/int => string 
```python
a = 6.7
int(a)
# '6.7'
```

### LES OPERATIONS

#### OPERATIONS SUR NOMBRES

Les operateurs arithmétiques suivant permettent de faire des opérations sur les nombres int et float.

|Opération|Opérateur|
|-|:-:|
|Addition|+|
|Soustraction|-|
|Multiplication|*|
|Division|\/|
|Exponentiation|**|
|Division entière|\/\/|
|Reste de la division entière (modulo)|%|

```python
a=1
b=2
c=3
(2*a+5/b)**c
# 91.125
```

Python authorise également l'utilisation de tous ces opérateurs en version condensée :

```python
a=3
a+=3 # incrémente a de 3
a/=2 # divise a par 2
print(a)
# 3
```

#### LES OPERATIONS SUR LES BITS

Les opérateurs binaire permettent de faire des opérations binaire sur les variable de type int.

|Operateurs | Opérations| Action|
|:-:|:-:|-|
| & |AND | bit resultante à 1 si toutes les bit en entree sont à 1|
\||OR|	bit resultante à 1 si au moins une des bit en entree à 1|
|^|	XOR|bit resultante à 1 si seulement une des bit en entree à 1|
|~| NOT|	Inversion de bit
|<<||décallage à gauche
|>>||décallage à droite

```python
a = 0b1010 # version binaire de 10
b = 0b1101 # version binaire de 13

bin(a & b) # binaire de a ET b
# '0b1000' = 8
bin(a | b) # binaire de a OU b
# '0b1111' = 15

bin(a >> 1) # decalage des bit vers la droite 1 fois.
# '0b101' = 5

bin(a << 1) # decalage des bits vers la gauche 1 fois
# '0b10100' = 20
```

### L'IDENTATION

L'identation est une **grosse contrainte** imposée par python.  
Le code n'utilisant pas les accolades pour encadrer les fonction, les blocs conditionnels ou les boucles, **l'executeur utilise l'identation pour identifier le debut et la fin de ces éléments**. 

```python
# bonne syntaxe
if True:
    print(...)

# mauvaise syntaxe
if True
print(...)
```

### LES CONDITIONS

#### BLOC IF

Le bloc if permet d'exécuter un ensemble d'instruction si une condition est vérifiée.  
En python, le bloc **if...else** est formulé de la façon suivante:

```python
condition=True

if condition :
    print('Condition remplie')
else :
    print("Condition non remplie")
```

Contrairement à d'autre langages de programation, la condition n'est pas définie entre parenthese. 

On peut enchainer les bloc de conditions en utilisant le mot clé `elif`

```python
condition2=True
condition1=condition3=False

if condition1 :
    print('Condition1 remplie')
elif condition2:
    print('Condition2 remplie')
elif condition3:
    print('Condition3 remplie')
else
    print('Aucune condition remplie')
```

On peut également utiliser les formulations condensées suivantes :

```python
# bloc if 
if condition : print("Condition remplie")

# bloc if .. else
print("Condition remplie") if condition else print("Condition non remplie")
```

On utilises des opérateurs de conditions, des opérateurs logiques et des opérateurs d'appartenances pour définir les conditions.

#### LES OPERATEURS DE CONDITION

Les opérateur suivant sont utilisé pour définir une condition.  
On les utilise dans un bloc if pour comparer 2 valeurs.

|opérateur|condition|utilisation|
|:-:|:-:|:-:|
|==|Egal à|x==y|	
|!=	|Différent de|x!=y|
|>|Supérieur à|x>y|	
|<|Inférieur à|x<y|
|>=|Supérieur ou égal à|x>=y|	
|<=|Inférieur ou égal à|x<=y|

```python
a = 1
b = 2

if b>a:
    print("b supérieur à a")
else :
    print("a supérieur à b")
```

#### LES OPERATEURS LOGIQUES

Le opérateurs logique permettent d'enchainer les conditions dans un bloc if.

|operateur|description|utilisation|
|:-:|-|-|
|and|True si toute les conditions sont remplies|if x < 5 and  x < 10|	
|or|True si une des conditions est remplie|if x < 5 or x < 4|	
|not|Inverse le resultat de la condition|if not x <  10 <br> if not(x < 5 and  x < 10)|

```python
condition1 = True
condition2 = False

if not condition:
    print('condition non remplie')
else:
    print('condition remplie)

if condition1 or condition2:
    print('conditions1 ou condition2 réunie')
```

#### LES OPERATEURS D'APPARTENANCE

Les opérateurs d"appartenances permettent de contrôler la présence d'un élément dans une collection (list, tuple, set et dict ...).

|operateur|description|exemple|
|:-:|-|-|
|in|True si l'element est dans la collection| x in [1,2,3]|
|not in|True si l'element n'est pas dans la collection|x not in [1,2,3]|

```python

d={'a':'alpha', 'b':'bravo', 'c':'charlie'} # dictionnaire
l = ['a','b','c'] # liste

if "a" in l: # a est present dans la liste l, la condition est remplie
    print("a est dans la liste")

if "a" in d: # a est une cle du dictionnaire, la condition est remplie 
    print("a est une cle du dictionnaire") 

if 'alpha' in d.values()):
    print("alpha est une valeur du dictionnaire")

```

### LES BOUCLES

#### BOUCLE FOR

La boucle ***for*** est utilisée pour itérer dans une collection (list, tuple, set, dict...).  
Elle permet d'exécuter un ensemble d'instrucion pour chaque élément de la collection.  

```python

t = ('alpha', 'bravo', 'charlie') # definition d'un tuple

for e in t:
    print(e)

# alpha
# bravo
# charlie
```

On peut stopper les itérations de la boucle en utilisant le mot clé `break`.

```python
d={'a':'alpha', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo'}

for (key, val) in d.items(): # methode items() renvoi un tuple (cle,valeur) pour chaque elements
    if key == "c":
        print('valeur charlie trouvée\nfin du programme.')
        break
    print(key, val)

# a alpha
# b bravo
# valeur charlie trouvée
# fin du programme.
```

Le mot clé `continue` permet de stopper l'itération en cours pour passer à la suivante.

```python
l=['alpha', 'bravo', 'charlie']

for (index, element) in enumerate(l): # enumerate renvoi un tuple (index, valeur) pour chaque elements
    if index == 1:
        continue
    print(index, element)

# 0 alpha
# 2 charlie
```

#### LA BOUCLE WHILE

La boucle ***while*** permet d'executer une série d'instruction un nombre défini tant qu'une condition est vérifiée.  
Dès que la condition n'est plus vérifiée, le programme sort de la boucle.

```python
i=0
while i< 6:
    print("boucle", i)
    i+=1

print("fin de la boucle")

# boucle 0
# boucle 1
# boucle 2
# boucle 3
# boucle 4
# boucle 5
# fin de la boucle
```

Comme la boucle ***for***, on peut utiliser le mot clé `break` pour sortir de la boucle et `continue` pour stopper une itération en cours.

On peut également intégrer un ***else*** à la suite du ***while*** pour effectuer une action en sortie de boucle.

```python
i=0
while i< 6:
    print("boucle", i)
    i+=1
else:
    print("fin de la boucle")

# boucle 0
# boucle 1
# boucle 2
# boucle 3
# boucle 4
# boucle 5
# fin de la boucle
```

### LES OPERATIONS SUR LES STRING

#### CONCATENATION

On peut concaténer plusieurs chaines de caractères en utilisant l'opérateur `+`.

```python
a='hello'
b=' '
c='world'
print(a+b+c)
```

Cet opérateur ne fonctionne uniquement pour concaténer des chaines de caractère entre elles.  
Pour concaténer une chaine avec une variable d'un autre type, on doit passer par une phase de **cast** avec la fonction **str()** ou par du tring formating.  

```python
a='hello'
b=' '
c=1 # valeur int

print(a+b+str(c)) # cast de la valeur int avant concatenation
```

##### STRING ~ LIST

En python (et comme dans la plupart des langages),les objets string sont des objets des listes (objet ***list***) de caractère. 
Comme un objet ***list*** on peut :
* recupérer un éléments de la chaine en utilisant son index
* recupérer un substring via une plage d'index
* vérifier une condition d'appartenance (mot clé in)
* ...

```python
a = "Hello World"
print(a[6])
# W
print(a[:4])
# 'Hell'

if 'Hello' in a:
    print("Hello dans ma chaine")

```

Comme ***list***, l'objet ***string*** est un ***iterable***, on peut donc également :
* le parcourir via une boucle ***for***
* afficher sa taille via la fonction ***len()***
* ...

```python
a = "Hello World"

len(a)
# 11

for c in a:
    print(c)

"""
H
e
l
l
o
 
W
o
r
l
d
"""
```

> **Attention** : les modification de la chaine en utilisant la formulation `ma_string[1]="a'` est interdite.  
> Les méthodes de ***list*** ne sont pas applicable sur un objet string, il utilise ses propres méthodes.  


##### METHODES DE STRING

L'objet string possède une serie de méthodes pour :
* les modifications : upper(), lower(), replace()...
* controler le contenu : isnumeric(), islower(), endswith() ...
* récupérer des éléments : find(), split()
* ... (liste des méthodes dispo [ici](https://www.w3schools.com/python/python_ref_string.asp))

```python
a="Hello:World"

a.lower() # renvoi string en lowercase
# 'hello:world'
a.upper() # renvoi string en uppercase
# 'HELLO:WORLD'
a.replace(":", " ") #remplace : par espace 
# 'Hello World'
a.find(":") # cherche la premier occurence de ":" et renvoi l'index
# 5
a.split(":") # sépare la chaine en utilisant le caractere : et renvoi une liste
# ['Hello', 'World']

```

#### STRING FORMATING

Le string formating permet d'intégrer des variables dans une chaine de caractère.  
En python, 2 formulations sont possibles:
    * en utilisant la méthode .format() de l'objet string. 
    * en utilisant le string formating opérator `%` : `"ma chaine et variable %d et ma variable %s"%(a, b)`

##### METHODE FORMAT

On déclare les variables entre {} dans notre chaine et on applique la méthode format sur la chaine.

```python
# utilisation avec variable non nommées
a=10
b='world'
print("ma chaine et variable {0} et ma variable {1}".format(a,b))

#utilisation avec variables nommées et operateur de format (arrondie à 2 decimal pour le float)
print("ma chaine et variable {c} et ma variable {d:.2f}".format(c="hello", d=5.445444))
# ma chaine et variable hello et ma variable 5.45

```

Il existe plusieurs opérateur de formatting, une liste est dispo [ici](https://www.w3schools.com/python/ref_string_format.asp)

##### OPERATEUR %

On déclare les variables avec le code `%<type_conversion>` dans la chaine et on applique l'opérateur % sur la chaine.
Chaque type est représenté par un code (string : %s, int; %i ...)

En complément du type, on peut intégrer des option de formatting.
Pour plus d'information sur les types disponibles et les options de formatting, une documentation est disponible [ici](https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html)

```python
a=10
b='world'

# on intègre un type int avec %i et un type string avec %s
# et on appplique l'operateur %
print("ma chaine et variable %i et ma variable %s"%(a, b))
# ma chaine et variable 10 et ma variable world

a=5.4454
b='hello'

# on intègre un type float arrondie à 2 digit avec %.2f, 
print("ma chaine et variable %.2f et ma variable %s"%(a, b))
# ma chaine et variable 5.45 et ma variable hello

```

### LES FONCTIONS

#### DEFINITION/APPEL

En python, les bloc fonction sont déclaré par le mot clé `def` suivit du nom de la fonction et des paramètre entre parenthèse (ou parenthèse vide si aucun paramètre).  
On peut ensuite l'utiliser en utilisant l'appelant par son nom dans la suite du code.  
Comme les bloc ***if*** ou ***for***, le respect de l'identation est très importante.  

```python
def ma_fonction():
    print("appel de la fonction")

# appel de la fonction
ma_function()
```

On utilise le mot clé `return` pour que la fonction renvoi un résultat.  
Pas besoin de définir le type de la valeur de retour, le typage est fait automatiquement.

```python

def ma_fonction():
    print("appel de la fonction")
    return_val = 10;
    return return_val

ma_fonction()

```

#### LES ARGUMENTS

Les arguments sont définis entre parenthèse lors de l'appel de la fonction.  
Il n'éxiste aucune restriction sur le type de l'argument en Python.  
Contrairement à javascript, par défaut, chaque argument défini doit obligatoirement avoir une valeur attribuée lors de l'appel de la fonction.  

```python

def create_session(fname, lname):
    print("creation de la session %s %s"%(fname.upper(), lname.upper()))

create_session('florent', 'dubois') # OK
# creation de la session FLORENT DUBOIS

create_session('florent') # Error
```

On peut définir une valeur par défaut pour les arguments lors de la définition de la fonction en utlisant la formulation `argument=valeur`.  
Si une valeur est définie lors de l'appel, la valeur par défaut est remplacée.

```python
def create_session(fname, lname="doe"):
    print("creation de la session %s %s"%(fname.upper(), lname.upper()))

create_session('florent', 'dubois') # OK
# creation de la session FLORENT DUBOIS

create_session('florent') # OK
# creation de la session FLORENT DOE
```

Lors de l'appel de la fonction, on peut également definir les paramêtre dans un ordre différent en utilisant leur nom.

```python
def create_session(fname, lname="doe"):
    print("creation de la session %s %s"%(fname.upper(), lname.upper()))

create_session(lname='dubois', fname='florent') # OK
# creation de la session FLORENT DUBOIS
```

#### ARBITRARY ARGUMENTS

Lors de la définition de la fonction, l'opérateur `*` nous permet de passer des arguments sans en définir le nombre.  
L'argument taggé avec `*` peut ensuite être utilisé comme un objet ***list*** dans la fonction.

```python
def print_format_name(*names):
    for n in names:
        print(n.upper())

print_format_name('obiwan','luc','han')
# OBIWAN
# LUC
# HAN
```

#### ARBITRARY KEYWORD ARGUMENTS

Un autre opérateur : `**`, nous permet de passer des arguments sans en définir le nombre.
L'argument taggé avec `**` peut ensuite être utilisé comme un objet ***dict*** dans la fonction.

```python
def print_format_user(**user):
    print("First name : {fname}, Last name : {lname}".format(fname=user['fname'], lname=user['lname']))

print_format_user(fname="florent", lname="dubois", age="34")
# First name : florent, Last name : dubois
```

### ENTREE UTILISATEURS

La fonction native ***input()*** va nous permettre d'interagir avec l'utilisateur dans le terminal.  
Elle prend en paramêtre le message à afficher et retourne la chaine de caractères entrée par l'utilisateur.

```python
print("Creation du compte")
nom = input("\tNom:")
prenom = input('\tPrenom:')
print("Bonjour %s %s.\nVotre compte est bien créé."%(prenom, nom))
```


