## INTRODUCTION A PANDAS

### INTRODUCTION

Pandas est une librairie python célèbre dans le domaine de la datascience.
Elle est spécialisé dans la gestion, l'analyse et la manipulation des données.
Il est utilisé dans (presque) tous les data-pipelines réalisé en python.

### ENVIRONNEMENT DATA-SCIENCE

Anaconda (ou Miniconda dans sa version plus légère) est une distribution libre et open source dédiée à la programmation Python et R.  
Elle est très utilisée dans la science des données, machine Learning et l’intelligence artificielle.

Cette distribution est devenue indispensable pour n’importe quel développeur dans le domaine de la data science pour sa richesse en modules et librairies de la data science mais aussi pour les outils fournie dans sa distribution (spyder, jupyter, conda ...)!

#### INSTALLATION DE MINICONDA

Miniconda est disponible au liens suivants : 
* [raspberry pi](http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh)
* [linux](https://repo.anaconda.com/miniconda/Miniconda-latest-Linux-x86_64.sh)
* [windows](https://repo.anaconda.com/miniconda/Miniconda-2.2.8-Windows-x86_64.exe)

Lancer ensuite le fichier _.exe_ pour l'installation Windows ou lancer le script d'installation pour l'installation linux.

```bash
chmod +x Miniconda-....sh
sudo ./Miniconda-....sh
```

Tester l'installation :

```
conda --version
```

Si cette commande lève une erreur, intégrez le chemin de conda dans le path.

Identifier la version de python installée 

```
python --version
```
#### JUPYTER NOTEBOOK

Jupyter Notebook est une application Web offrant une interface ergonomique pour programmer dans plus de 40 langages.
L'outil ***notebook*** de Jupyter permet de créer des documents intégrant du code directement executable, les résultats, du texte explicatif en markdown, des illustration ...  
Il permet de tester rapidement et facilement un processing et de partager le résultat. C'est donc l'outils parfait pour l'analyse de données.

Il est également fourni avec le paquet Anaconda, on peut tester sa bonne installation avec la commande `jupyter notebook --version`

On lance l'outil de jupyter notebook avec la commande suivante:
```
jupyter notebook
```

#### CONDA

Conda est un système open source de gestion d'environnement et de gestion de paquets.  

Ses fonctions principales sont :
* de créer des environnements d'exécution sur une même machine
* administer et basculer entre ces environnement
* les sauvegarder, les restaurer ou les cloner pour les partager.
* étendre leur fonctionnalités en installant de nouvelles libraries (et leur dépendances).

Il est fourni avec le paquet anaconda, on peut tester sa bonne installation avec la commande `conda --version`.

La liste des commandes est disponible dans la [documentation](https://docs.conda.io/projects/conda/en/latest/commands/list.html).

#### LES ENVIRONNEMENT CONDA

Conda permet d'installer des environnements de développement.

Chaque environnement est séparé des autres et peut contenir des paquets différents ou des version de python différentes.
Lors de l'installation de miniconda un environnement nommé ***base*** est créé, il est considéré comment la configuration global python.

Ces environnements multiples permettent de tester un code dans des configurations différentes ou de tester des librairies multiple sans toucher à la configuration python globale.

La commande `conda` permet de créér et supprimer ces environnements rapidement et facilement.

##### MANIPULER LES ENVIRONNEMENTS

###### CREATION

Creation d'un environnement nommé ***python2_env*** avec la ***version 2*** de python :

`conda create --name python2_env python=2`

Creation d'un environnement nommé ***python3_env*** avec la ***version 3*** de python.
On intégre l'installation des paquet ***ipykernel*** et ***pandas*** pendant la création. 

`conda create --name python3_env python=3 ipykernel pandas`

###### LISTER LES ENVIRONNEMENT

La commande `conda info --env` permet de lister les environnement et leur path

###### ACTIVER UN ENVIRONNEMENT 

En fonction de l'OS (et de la version de conda) une des commande suivante permet de switcher entre les environnement:
* `source activate nom_environnement`
* `activate nom_environnement`
* `conda activate nom_environnement`

###### SORTIR D'UN ENVIRONNEMENT

En fonction de l'OS (et de la version de conda) une des commande suivante permet de switcher entre les environnement:
* `source deactivate` 
* `deactivate`
* `conda deactivate`

#### LES KERNELS JUPYTER

Jupyter peut de programmer en plus de 40 langages grâce à un systeme de Kernel.
Les kernels sont des environnements d'execution, ce sont eux qui exécute le code intégré dans le notebook pour lui renvoyer le résultat.

Donc pour chacun des environnement créé, on va pouvoir créé un kernel IPython pour l'associer à jupyter notebook.
Ces kernels vont nous permettre d'executer notre code python dans chacun des environnements.

##### IPYKERNEL

Pour lié créer un kernel lié à notre environnement et l'associer à Jupyter, on utilise le module ***ipykernel***.

On l'installe via conda avec les commandes suivantes:

```bash
source activate python3_env #active le virtual env
conda install ipykernel # installation de ipykernel dans le virtual env
```

##### ASSOCIER LE KERNEL AU NOTEBOOK

On utilise le module ***ipykernel*** installé pour lié notre environnement au notebook.

```bash
source activate python3_env
python -m ipykernel install --user --name python3_env --display-name "Python 3 Env"
# installation kernel lie a python3_env nomme Python 3 Env
```

Lors de la prochaine ouverture de jupyter notebook avec la commande `jupyter notebook`, le kernel doit apparaitre dans la liste des kernels diponible

On peut également afficher la liste des kernel associé à python avec la commande :

```bash
jupyter kernelspec list
# RESULTAT
#Python 3 Env    /home/florent/.local/share/jupyter/kernels/python3_env

```

### LA BIBLIOTHEQUE PANDAS

La bibliothèque pandas est spécialisé dans l'analyse et la manipulation de large volume de données.
Elle simplifie des opérations complexes telle que :
* gestion de données manquantes
* alignement et tri de données
* redimensionnement, fusion et jointure de table
* creation de table pivot

cette bibliothèque est devenu l'outil incontournable du **Data Engineer** pour la préparation et la normalisation de données.

> Le Data Engineer est le premier maillon de la chaine de données.  
> Il concoit les algorithme pour concilier le format des data collectés avec celui des bases de données utilisées pour les analyses (par les Data Analysts) ou la création des modèles de machine learning et d'intelligence artificiellle (par les Data Scientists).

#### INSTALLATION DE PANDAS

On installe pandas (et toutes ses dépendances) avec la commande conda : `conda install pandas`.

L'installation se fait dans l'environnement préalablement activé.

Maintenant que la librairie pandas est installé, on peut l'importer dans notre code workbook avec la commande `import pandas`

![import_pandas](media/import_panda.png)

#### LES OBJETS DE PANDAS

Pour la manipulation de données Pandas se repose sur 2 composantes essentielles :
* les ***pandas.Series***
* les ***pandas.Dataframes***

Les ***pandas.Series*** sont des tableaux unidimensionnel avec un label pour chaque ligne.  
On nomme ***index** l'ensemble des labels de ligne.

Les ***pandas.Dataframes*** sont des tableau bidimensionnel avec un label pour chaque ligne et pour chaque colonnes.

![serie_dataframe](./media/serie_dataframe.webp)

La relation entre les ***Series*** et les ***Dataframes*** est étroite car un ***Dataframe*** peut être considéré comme un ensembles de ***Series***.

### LES PANDAS SERIES

#### CREER DES SERIES

Dans sa définition la plus simple on créé une Series en appelant l'objet pandas.Series() avec un objet list en paramêtre.

```python
arr = [0,1,2,3,4,5,6,7,8,9] # declaration d'un objet list
pds = pd.Series(arr) # definition de la pandas.Series()

print(pds)

"""
0    2
1    3
2    4
3    5
4    6
5    7
6    8
7    9
dtype: int64
"""
```

Pandas défini le type de la valeurs et créé un index automatiquement.  
On peut aussi définir notre propre index en passant une liste en paramêtre _index_ mais attention, chaque éléments de cette liste doit être unique.

On peut aussi donner un nom à notre Series en passant un string au paramêtre _name_.

```python
arr = [0,1,2,3,4,5,6,7,8,9] # declaration d'un objet list
arr_index = ['a','b','c','d','e','f','g','h','i','j'] #list d'index

pds = pd.Series(arr, index=arr_index, name="first_serie") # ajout index + name
print(pds)

"""
a    0
b    1
c    2
d    3
e    4
f    5
g    6
h    7
i    8
j    9
Name: first_serie, dtype: int64
"""
```

> La définission du nom et de l'index de la serie peut aussi se faire après son instantation en redéfinissant les arguments _index_ et _name_ ou les fonctions _reindex()_ et _rename()_
>
> ```python
> pds.name = "first_serie" # ou pds.rename("first_serie")
> pds.index = ['a','b','c','d','e','f','g','h','i','j'] # ou pds.reindex(...)
> ```

L'objet Series peut prendre un dictionnaire en paramêtre.  
Dans cette configuration, il utilise les clés du dictionnaire comme index.

```python
d = { # definition du dictionnaire
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9
}

pds = pd.Series(d) # déclaration de la serie
print(pds)
"""
a    1
b    2
c    3
d    4
e    5
f    6
g    7
h    8
i    9
dtype: int64
"""
```

On peut également reconvertir une serie en dictionnaire ou en list avec les méthode ***to_list()*** et ***to_dict()***.

#### PANDAS ET NUMPY

Dans son fonctionnement internet, Pandas se base en grande partie sur une autre librairie spécialisé dans la datascience : ***Numpy***.
Sa relation avec Numpy est tellement étroite qu'on peut :
* intégrer des objet propre à Numpy dans des Dataframes/Series
* utiliser des fonction numpy sur des Series pandas
* convertir des Series/Dataframes Pandas en objet Numpy.

```python
# import de numpy
import numpy as np

# definition d'un array numpy avec 
# np.nan (sans null numpy) et np.inf (valeur infinie numpy)
arr = np.array([2,4,np.nan, np.inf]) 

print(arr)
# array([ 2.,  4., nan, inf])

s = pd.Series(arr)
print(s)
"""
0    2.0
1    4.0
2    NaN
3    inf
dtype: float64
"""

print(np.min(s))
# 2.0

narr = s.to_numpy()
print(narr)
# array([ 2.,  4., nan, inf])
```

#### LES METHODES ET PROPRIETES DE SERIES

L'objet Series de pandas comporte un ensemble de méthodes et de propriétés qui vont nous permettre d'analyser les informations contenues dans la Series et de les modifiet er suivant le besoin. 

Nous allons décrire quelques méthode appliqué à la Series définies par le code suivant :

```python
import numpy as np
# definition des valeurs
arr = [2.4, 5.6, np.nan, 1.3, 0.6, 3.2, 4.3, np.nan, np.inf, 0.2, np.nan, 6.8]

# definition d'une liste d'index
index_list = [1, 11, 2, 5, 4, 9, 3, 7, 0, 10, 8, 6]

# definition de la serie

s = pd.Series(arr, index=index_list, name="score")
print(s)

"""
1     2.4
11    5.6
2     NaN
5     1.3
4     0.6
9     3.2
3     4.3
7     NaN
0     5.7
10    0.2
8     NaN
6     6.8
Name: score, dtype: float64
"""
```

##### Analyser les valeurs 

* **Nombres de valeurs :**

L'attribut ***size*** de la Series nous permet de récupérer le nombre de valeurd dans la série (on peut aussi utiliser la méthode python ***len***).
La méthode ***count()*** permet de récupérer le nombre de valeurs non nulle ( différent de np.nan)

```python
print("Nombre de valeurs {}".format(s.size))
# Nombre de valeurs dans la Series : 12

print("Nombre de valeurs non nulle dans la Series : {}".format(s.count()))
# Nombre de valeurs non nulle dans la Series : 9

print("Taux de remplissage de la Series : {}%".format((s.count()/s.size)*100))
# Taux de remplissage de la Serie : 75.0%
```

* **Valeurs uniques :**

La méthode ***drop_duplicates()*** renvoi une nouvelle serie contenant uniquement les valeurs unique.
La méthodes ***value_counts()*** renvoi une serie avec la liste de valeurs uniques en index et le comptage pour chaque élement en valeur.


```python
# recuperation des valeurs uniques
uniq_series = s.drop_duplicates()

# recuperation d'une serie avec le comptage des valeurs
count_series = s.value_counts()

print(uniq_series)
"""
1     2.4
11    5.6
2     NaN
5     1.3
4     0.6
9     3.2
3     4.3
0     inf
10    0.2
6     6.8
Name: score, dtype: float64
"""

print(count_series)
"""
5.7    1
2.4    1
0.6    1
6.8    1
1.3    1
0.2    1
3.2    1
4.3    1
5.6    1
Name: score, dtype: int64
"""
```

Une méthode ***unique()*** renvoi la liste des valeurs unique dans un format numpy array.

###### Description des données

La méthode _describe()_ permet d'afficher des infos statistique sur les données numeriques (moyenne, les quantile, la standard deviation...), le nom et le type des données
```python
s.describe()

"""
count    9.000000 # nb valeur non nulle
mean     3.344444 # moyenne
std      2.397974 # dispersion des valeur
min      0.200000 # valeur min
25%      1.300000 # quantile(0.25)
50%      3.200000 # quantile(0.50)
75%      5.600000 # quantile(0.75)
max      6.800000 # valeur max
Name: score, dtype: float64
"""
```

Toutes ces données sont accessibles individuellement en utilisant les fonctions ou les attributs correspondants :

```python
print(s.mean())
# 3.344444444444444

print(s.quantile)
# 1.3

print(s.max())
# 6.8

print(s.dtype)
# dtype('float64')
```

##### Trier les valeurs

La méthodes _sort\_values()_ renvoi une copie de la Series avec les valeurs triées
La méthode _sort\_index()_ renvoi une copie de la Series avec les index triés.

Le tri est fait dans l'ordre croissant/décroissant en fonction du boolean passé au pramètre _ascending_ (par défaut ascending=True).

```python
s_sortedValues = s.sort_values(ascending=False)

s_sortedIndexes = s.sort_index(ascending=True)

print(s_sortedValues)
"""
6     6.8
0     5.7
11    5.6
3     4.3
9     3.2
1     2.4
5     1.3
4     0.6
10    0.2
2     NaN
7     NaN
8     NaN
Name: score, dtype: float64
"""

print(s_sortedIndexes)
"""
0     5.7
1     2.4
2     NaN
3     4.3
4     0.6
5     1.3
6     6.8
7     NaN
8     NaN
9     3.2
10    0.2
11    5.6
Name: score, dtype: float64
"""
```
##### Renvoyer une valeurs ciblées

Je peux récupérer **une** valeurs de la serie en utilisant :
* le label de la ligne avec la ***propriété at[]***, la ***propriété loc[]***, la ***fonction get()***.
* le numero de l'item avec la ***propriété iat[]*** ou la ***propriété iloc[]***.

```python
print('valeur a la ligne labelisé 3 : {at}, a la ligne index 3 : {iat}'.format(at=s.at[3], iat=s.iat[3]))
# valeur a la ligne labelisé 3 : 4.3, a la ligne index 3 : 1.3

print('valeur a la ligne labelisé 6 : {loc}, a la ligne index 6 : {iloc}'.format(loc=s.loc[6], iloc=s.iloc[6]))
# valeur a la ligne labelisé 6 : 6.8, a la ligne index 6 : 4.3

print(s.get(8))
# nan
```

> ATTENTION :  La formulation simple `s[3]` existe aussi mais elle est ambigüe si le label est numérique car elle utilise le label sinon il existe sinon l'item.
> Si l'index est de type text, aucune ambigüité, on peut l'utiliser.

> POUR INFO : La fonction _get()_ ne renvoi pas d'erreur si le label de ligne n'existe pas contrairement aux propriété _at[]_ et _loc[]_, en contrepartie elle comporte le même défaut que la formulation simple ci-dessus.

##### Renvoyer plusieurs valeurs ciblées

Je peux ***renvoyer une nouvelle Series*** contenant plusieurs valeurs en utilisant:
* une liste de label avec la ***propriété loc[]***
* une liste d'item ou une plage d'item avec la ***propriété iloc[]***

```python
# je cree un Series qui contient les label pair de s
s_pairLabels = s.loc[[0,2,4,6,8,10]]

# je cree un Series qui contient les item pair de s
s_pairItems = s.iloc[[0,2,4,6,8,10]]
# formulation plage d'item => s.iloc[2:6]

print(s_paiLabels)
"""
2     NaN
4     0.6
6     6.8
8     NaN
10    0.2
Name: score, dtype: float64
"""

print(s_pairItems)
"""
1    2.4
2    NaN
4    0.6
3    4.3
0    5.7
8    NaN
Name: score, dtype: float64
"""
```

Les propriété ***loc[]*** peut aussi intégrer une plage de valeurs mais pour obtenir un résultat cohérent il faut dabord appliquer un _sort_index()_ sur la serie.

```python
# je veux obtenir la plage de label 2=>6 donc 2,3,4,5,6
# test sans sorting 

print(s.loc[2:6])
""" pandas commence au lable 2 et fini au 6
mais en intégrant tous les label intermediaires
2     NaN
5     1.3
4     0.6
9     3.2
3     4.3
7     NaN
0     5.7
10    0.2
8     NaN
6     6.8
Name: score, dtype: float64
"""

print(s.sort_index().loc[2:6])
""" j'obtient le resultat voulu
2    NaN
3    4.3
4    0.6
5    1.3
6    6.8
Name: score, dtype: float64
"""
```

> ATTENTION : La formulation simple `s[2:6]` existe aussi mais elle est ambigüe si le label est numérique car elle utilise le label si il existe sinon l'item.

##### Boucler sur une Series

Par défaut, boucle ***for*** appliqué sur une Series permet de renvoyer chaque valeur de la serie indépendement.
Pour boucler sur l'index, on utilise la propriété ***index*** de la Series.

```python
for v in s: # boucle sur valeur serie
     print(v)

for i in s.index: # boucle sur index
     print(i)
```

##### Filtrer les valeurs

La formulation `s[series_condition]` renvoie une série contenant les éléments respectant la condition définie.

La ***condition_serie*** est une ***Series*** contenant des valeurs ***True*** et ***False*** pour chaque élément de la ***Series testée*** en fonction de la condition définie.

```python
# afficache de la condition s supérieur à 5
print(s > 5)

""" renvoi d'une serie contenant
 True pour les valeurs supérieur à 5
 et False pour autres valeurs

1     False
11     True
2     False
5     False
4     False
9     False
3     False
7     False
0      True
10    False
8     False
6      True
Name: score, dtype: bool
""""
```

La Series de condition peut être obtenue en utilisant des opérateurs de condition python sur une Series ou en utilisant des méthodes de Series dédiées.

* **Opérateurs de condition sur les valeurs/index:** 

On peut utiliser les opérateurs de conditions standard python pour renvoyer une Series de condition, mais des fonction de condition correspondantes sont également disponibles (***gt()***, ***lt()***, ***eq()*** ...)

```python
s_sup5 = s[s > 5]
print(s_sup5)

""" elements de s dont les valeurs sont supérieure à 5
11    5.6
0     5.7
6     6.8
Name: score, dtype: float64
"""
```

Cette formulation fonctionne sur les valeurs de la série mais on peut l'appliquer sur l'index en utilisant la propriété ***index*** de Series.

```python
s_indexsup5 = s[s.index > 5]
print(s_indexsup5)

""" renvoi des index supérieur a 5
11    5.6
9     3.2
7     NaN
10    0.2
8     NaN
6     6.8
Name: score, dtype: float64
"""
```

On peut également utiliser les opérateur logique ***binaires*** pour chainer les conditions

```python
s_sup5inf6 = s[(s > 5) & (s < 6)] # chainage de condition
print(s_sup5inf6)
""" elements de s dont les valeurs sont supérieure à 5
et inférieure à 6

11    5.6
0     5.7
Name: score, dtype: float64
"""
```

* **Operation d'appartenance (in) sur les valeurs/index :**

La fonction isin() permet de renvoyer les éléments dont ***les valeurs*** sont contenus dans une liste.
Comme précédement, on peut l'appliquer sur l'index pour récupérer les valeurs d'index contenu dans la liste.

```python

s_valin = s[s.isin([.1,.2,.3,.4,.5,.6])] # valeur in 
s_indin = s[s.index.isin([1,3,6,9,11])] # index in

print(s_valin)
"""
4     0.6
10    0.2
Name: score, dtype: float64
"""

print(s_indin)
"""
1     2.4
11    5.6
9     3.2
3     4.3
6     6.8
Name: score, dtype: float64
"""
```

* **Identifier les valeurs nulles/non nulle :**
  
La méthodes _isna()_ et _isnull()_ permettent d'identifier les valeur np.nan de la serie.
On peut utiliser ces méthode pour renvoyer toutes les valeurs nulle de la series.

Les méthodes _notna()_ et _notnull()_ permettent d'identifier les valeur différentes de np.nan de la série. On peut utiliser ces méthode pour renvoyer toutes les valeurs non nulle de la series.

```python
s_nan = s[s.is_na()] # equivalent à isnull
print(s_nan)
"""
2   NaN
7   NaN
8   NaN
Name: score, dtype: float64
"""

s_notna = s[s.notna()] # equivalent à notnull
print(snotna)
"""
1     2.4
11    5.6
5     1.3
4     0.6
9     3.2
3     4.3
0     5.7
10    0.2
6     6.8
Name: score, dtype: float64
"""
```

* **Remplir/supprimer les valeurs nulles:**

La méthode ***fillna()*** permet de remplacer les valeurs nulles par une valeur, et dropna() de supprimer les lignes avec une valeur nulle.
Ces méthode renvoi une copie de la Series avec les modifications par défaut mais en donnant la valeur ***True*** au paramêtre inplace, on peut remplacer la Series originale.

```python
s.fillna(0)
"""
1     2.4
11    5.6
2     0.0
5     1.3
4     0.6
9     3.2
3     4.3
7     0.0
0     inf
10    0.2
8     0.0
6     6.8
Name: score, dtype: float64
"""

s.dropna()
"""
1     2.4
11    5.6
5     1.3
4     0.6
9     3.2
3     4.3
0     inf
10    0.2
6     6.8
Name: score, dtype: float64
"""
```

* **Modification des Series :**

La modification des Séries est plutot simple, elle consiste utiliser l'opérateur `=` sur les éléments ciblé ou filtré.
Les modification est mutable, elle modifie donc la/les valeurs de la série initiale, si on veut garder la Series initiale on peut en en faire une copie avec la méthode ***copy()***

```python
""" Rappel de la serie initiale
1     2.4
11    5.6
2     NaN
5     1.3
4     0.6
9     3.2
3     4.3
7     NaN
0     5.7
10    0.2
8     NaN
6     6.8
Name: score, dtype: float64
"""

s.loc[0] = 10 # valeur 10 à l'index 0 
print(s)
"""
1     2.4
11    5.6
2     NaN
5     1.3
4     0.6
9     3.2
3     4.3
7     NaN
0     10.0 # modification de la valeur a l'index 0 : inf -> 10
10    0.2
8     NaN
6     6.8
Name: score, dtype: float64
"""

s[s.isna()] = 0 # remplacement de tous les nan par 0, idem s.fillna(0)
print(s)
"""
1     2.4
11    5.6
2     0.0
5     1.3
4     0.6
9     3.2
3     4.3
7     0.0
0     0.0
10    0.2
8     0.0
6     6.8
Name: score, dtype: float64
"""
```

* **Operation sur les chaines de caractère :**

En passant par l'attribut ***str*** d'une Series, on peut effectuer des opérations ou tester des conditions sur des chaines de caractères.

Faisons quelques tests sur une Series définie par le code suivant:

```python
arr = ["Moscou,Russie","Londres,Angleterre","Paris,France","Rhin-Ruhr,Allemagne","Milan,Italie","Randstad,Allemagne","Madrid,Espagne","Saint-Pétersbourg,Russie"]
index = ["mo-ru","lo-an","pa-fr","rh-al","mi-it", "ra-al","ma-es", "sp-ru"]

s = pd.Series(arr, index=index, name="villes")

"""
mo               Moscou
lo              Londres
pa                Paris
rh            Rhin-Ruhr
mi                Milan
ra             Randstad
ma               Madrid
sp    Saint-Pétersbourg
Name: villes, dtype: object
"""
```

L'attribut ***str*** se rapproche d'un objet ***string***, certaine méthodes/fonctionnements de l'objet on été reproduit sur cet attribut pour la modification de la chaine :
* ***upper()***, ***lower()***, ***capitalize()*** : transformation majuscule/minuscule/... 
* ***split()*** : sépare la chaine suivant un caractère
* ***slice()*** : recuperation d'une partie de la chaine (formulation range index \[0:N\] aussi possible)
* ***replace()*** : remplacement d'une partie de la chaine (regex possible)
* ***extract(regex, expand=True)*** : extrait une partie de la chaine en fonction de la regex.

Ces méthodes renvoient une nouvelle Series avec les valeurs modifiées.

```python
s.str.lower()
"""
mo-ru               moscou,russie
lo-an          londres,angleterre
pa-fr                paris,france
rh-al         rhin-ruhr,allemagne
mi-it                milan,italie
ra-al          randstad,allemagne
ma-es              madrid,espagne
sp-ru    saint-pétersbourg,russie
Name: villes, dtype: object
"""

s.str.split(',')
"""
mo-ru               [Moscou, Russie]
lo-an          [Londres, Angleterre]
pa-fr                [Paris, France]
rh-al         [Rhin-Ruhr, Allemagne]
mi-it                [Milan, Italie]
ra-al          [Randstad, Allemagne]
ma-es              [Madrid, Espagne]
sp-ru    [Saint-Pétersbourg, Russie]
Name: villes, dtype: object
"""
```

Les méthodes renvoyant des conditions sont également disponibles:
* ***match(regex)*** : renvoi une serie de boolean indiquant si la valeur match la regex 
* ***contains(regex)*** : renvoi une serie de boolean indiquant si la valeur contient du texte qui match la regex 
* ***contains(text, regex=False)*** : renvoi une serie de boolean indiquant si la valeur contient le texte.

```python
s_match = s[s.str.match('(\w+)-(\w+)')] # recherche du patern word-word
print(s_match)

""" 
rh-al         Rhin-Ruhr,Allemagne
sp-ru    Saint-Pétersbourg,Russie
Name: villes, dtype: object
"""

import re # import de la lib regex
# recherche du pattern word-a... en mode ignorecase
s_contain = s[s.str.contains('\w\,a', regex=True, flags=re.IGNORECASE)]
print(s_contain)

"""
lo-an     Londres,Angleterre
rh-al    Rhin-Ruhr,Allemagne
ra-al     Randstad,Allemagne
Name: villes, dtype: object
"""
```

On peut utiliser ces fonction de conditions pour filtrer des éléments et les modifier en utilisant l'opérateur `=`, mais attention, l'opération va modifier la serie originale. 

La méthode ***extract()*** est particulière, elle permet de faire une sélection/séparation de la chaine de caractère en fonction d'une regex et renvoi un dataframe contenant une colonne pour chaque groupe de la regex

```python
s.str.extract('([a-z1-Z\-]+)(?:,)(\w+)')
print(df)
"""
                 0           1
mo-ru       Moscou      Russie
lo-an      Londres  Angleterre
pa-fr        Paris      France
rh-al         Ruhr   Allemagne
mi-it        Milan      Italie
ra-al     Randstad   Allemagne
ma-es       Madrid     Espagne
sp-ru  Pétersbourg      Russie
"""
```

La méthode ***cat()*** permet de concatener les chaines de 2 Series ensemble, pour leur index correspondants.

```python
s_concat = s.str.cat(s, sep="|")
print(s_concat)

"""
mo-ru                          Moscou,Russie|Moscou,Russie
lo-an                Londres,Angleterre|Londres,Angleterre
pa-fr                            Paris,France|Paris,France
rh-al              Rhin-Ruhr,Allemagne|Rhin-Ruhr,Allemagne
mi-it                            Milan,Italie|Milan,Italie
ra-al                Randstad,Allemagne|Randstad,Allemagne
ma-es                        Madrid,Espagne|Madrid,Espagne
sp-ru    Saint-Pétersbourg,Russie|Saint-Pétersbourg,Russie
Name: villes, dtype: object
"""
```

* **Opérations sur les Series :**

On peut utiliser des opérateurs standard pour effectuer des opérations sur les Series mais pour chaque opérateur une méthode corespondante existe (***add()***, ***sub***, ***mul()*** ...)

```python
s_add10 = s + 10 # identique a s.add(10)
print(s_add10)
"""
1     12.4
11    15.6
2     10.0
5     11.3
4     10.6
9     13.2
3     14.3
7     10.0
0     10.0
10    10.2
8     10.0
6     16.8
Name: score, dtype: float64
"""

s_op = s**2 # identique a s.pow(2)
print(s_op)
"""
1      5.76
11    31.36
2      0.00
5      1.69
4      0.36
9     10.24
3     18.49
7      0.00
0      0.00
10     0.04
8      0.00
6     46.24
Name: score, dtype: float64
"""
```

On peut également effectuer des opérations entre 2 series. 

Attention : Si l'on utilise les opérateurs standard l'opération est effectuée entre les index correspondants des 2 Series, les autres index sont instanciés à NaN.
Seul les fonction d'operation nous permettent de garder les valeurs des index qui n'ont pas de correspondance.

```python

sbis = pd.Series([10, 12, 16], index=[4, 7, 2])
print(s+sbis)

""" en utilisant l'operateur +, NAN si pas d'index correspondant
0      NaN
1      NaN
2     16.0
3      NaN
4     10.6
5      NaN
6      NaN
7     12.0
8      NaN
9      NaN
10     NaN
11     NaN
dtype: float64
"""

print(s.add(sbis, fill_value=0)) # utilisation de la fonction add

""" en utilisant la fonction je garde mes valeurs 
0      10.0
1      2.4
2     16.0
3      4.3
4     10.6
5      1.3
6      6.8
7     12.0
8      0.0
9      3.2
10     0.2
11     5.6
dtype: float64
"""
```

* **Appliquer une fonction :**
  
La méthode ***apply()*** permet d'appliquer une fonction sur chaque éléments de la Serie.
On peut utiliser soit une fonction définie préalablement soit une lambda.

```python
def addEl(x):
    return " => {}".format(x)

s_apply = s.apply(addEl) # application fonctio addEl sur chaque element de s
print(s_apply)
"""
1      => 2.4
11     => 5.6
2      => 0.0
5      => 1.3
4      => 0.6
9      => 3.2
3      => 4.3
7      => 0.0
0      => 0.0
10     => 0.2
8      => 0.0
6      => 6.8
Name: score, dtype: object
"""

s_apply_lambda = s.apply(lambda x : ' => {}'.format(x)) # idem sous format lambda
print(s_apply_lambda)
"""
1      => 2.4
11     => 5.6
2      => 0.0
5      => 1.3
4      => 0.6
9      => 3.2
3      => 4.3
7      => 0.0
0      => 0.0
10     => 0.2
8      => 0.0
6      => 6.8
Name: score, dtype: object
"""
```

### LES PANDAS DATAFRAMES

#### CREER DES DATAFRAMES

* **From scratch :**

Dans sa définition la plus simple on créé un Dataframe en appelant l'objet pandas.Dataframe() avec un objet dictionnaire en paramêtre.

```python
pays = {
'Pays': ['Russie', 'Italie', 'Maroc', 'France'],
'Densité': [8.57, 200.27, 65.46, 117.63]
}

df = pd.DataFrame(data)
print(df)

"""
     Pays  Densité
0  Russie     8.57
1  Italie   200.27
2   Maroc    65.46
3  France   117.63
"""
```

Dans cette configuration, les cles sont utilisées pour les noms de colonne et les index sont créé automatiquement, mais comme pour les Series, on peux ajouter notre propre liste d'index en paramêtre ***index***.

```python
pays = {
'pays': ['Russie', 'Italie', 'Maroc', 'France'],
'densite': [8.57, 200.27, 65.46, 117.63]
}
df = pd.DataFrame( pays , index= ['R','I','M','F'])
print(df)

"""
     pays  densité
R  Russie     8.57
I  Italie   200.27
M   Maroc    65.46
F  France   117.63
"""
```

En passant le dictionnaire dans la méthode ***from_dict()*** de ***Dataframe***, on peut utiliser les clés de dictionnaire en tant qu'index plutot que colonne en jouant sur le paramêtre ***orient***.

```python

pays_densite = {
'R': ['Russie', 8.57],
'I': ['Italie', 200.27],
'M': ['Maroc', 65.46],
'F': ['France',117.63]
}

df = pd.DataFrame.from_dict(pays_densite, orient='index', columns=['pays', 'densite'])
print(df)

"""
     pays  densite
R  Russie     8.57
I  Italie   200.27
M   Maroc    65.46
F  France   117.63
"""
```

* **Depuis plusieurs Series**

Comme dit précédemment, un Dataframe peut être considéré comme un ensembles de Series.
On peut donc concaténer 2 Series pour créer un Dataframe en utilisant la fonction de ***concat*** de Pandas.

Le Dataframe résultant contient une colonne pour chaque Serie, le nom de la Series est utilisé comme nom de colonne.
L'index de chaque Series est utilisé lors de la concaténation pour lier les données.

```python
# definition des 2 series
pays_serie = pd.Series(['Russie', 'Italie', 'Maroc', 'France'], index=['R','I','M','F'], name="pays")
densite_serie = pd.Series([200.27, 8.57,117.63,65.46], index=['I','R','F','M'], name='densite')

print(pays_serie,'\n',densite_serie)
"""
R    Russie
I    Italie
M     Maroc
F    France
Name: pays, dtype: object 
I    200.27
R      8.57
F    117.63
M     65.46
Name: densite, dtype: float64
"""

df = pd.concat([pays_serie, densite_serie], axis=1) # concat des 2 serie sur l'axe 1 (colonnes)
print(df)
"""
     pays  densite
R  Russie     8.57
I  Italie   200.27
M   Maroc    65.46
F  France   117.63
"""
```

La fonction ***concat*** fonctionne également pour des concaténation Dataframe/Serie et Dataframe/Dataframe. 

* **Depuis un fichier structuré :**

En utilisant les méthodes de pandas : ***read_csv()***, ***read_json()***, ***read_excel()***...; on peut créer un Dataframe à partir d'un fichier structuré.

```python
# creation d'un dataframe a partir de pays.csv, je defini la ligne 0 comme header et la colonne 0 comme index
df_ = pd.read_csv('pays.csv', sep=',', header=0, index_col=0)
print(df)

"""
     pays  densite
R  Russie     8.57
I  Italie   200.27
M   Maroc    65.46
F  France   117.63
"""
```

#### OPERATION SUR LES COLONNES

##### RECUPERER UNE/DES COLONNES

La formulation `df[colonne]` permet d'isoler une colonne du Dataframe, l'opération nous renvoi un objet Series

```python
print(df['pays']) # idem df.pays
"""
R    Russie
I    Italie
M     Maroc
F    France
Name: pays, dtype: object
'"""
```
On peut récupérer plusieurs colonnes en passant un tableau de colonnes : `df[[colonne1,colonne2]]`

##### AJOUTER UNE/DES COLONNES

Plusieurs solutions sont diponibles pour ajouter des colonnes à notre dataframe :
* ajout d'une serie via l'opération concat (voir plus haut)
* ajout d'une serie en utilisant la formulation `df['new_colonne']=series`
* creation d'une serie avec une valeur de remplissage en utilisant la formulation `df['new_colonne']=valeur`

```python
# creation d'une serie => colonne pays, je ne garde que les ligne index ['I','M']
splus = df['pays'].loc[['I','M']]

# ajout d'une colonne pays_plus contenant la series splus
df['pays_plus'] = splus
print(df)
"""
      pays  densite pays_plus
id                           
R   Russie     8.57       NaN # pas d'index correspondant => NaN
I   Italie   200.27    Italie
M    Maroc    65.46     Maroc
F   France   117.63       NaN # pas d'index correspondant => NaN
"""

df['pays_plus_plus'] = 10
print(df)
"""
      pays  densite pays_plus  pays_plus_plus
id                                           
R   Russie     8.57       NaN              10
I   Italie   200.27    Italie              10
M    Maroc    65.46     Maroc              10
F   France   117.63       NaN              10
"""
```

##### SUPPRIMER UNE/DES COLONNES

La méthode ***drop(colonne, axis=1)*** permet par défaut de supprimer des lignes, mais en attribuant la valeur 1 à sa propriété ***axis**, elle permet de supprimer une ou plusieurs colonne.
Par défaut, la méthode renvoi une copie du Dataframe avec la colonne supprimée, on peut modifier directement le dataframe d'origine en passant le paramêtre ***inplace*** à True.

```python
df = df.drop(['pays_plus_plus', 'pays_plus'], axis=1, inplace=True)
print(df)

"""
      pays  densite
id                 
R   Russie     8.57
I   Italie   200.27
M    Maroc    65.46
F   France   117.63
"""
```

La méthode ***pop()*** permet de renvoyer la colonne supprimée dans une variable sous la forme d'une Series.

```python
pays_pp_series = df.pop('pays_plus_plus')
```

##### MODIFIER LE NOM DES COLONNES

On peut modifier le nom des colonne via l'attribut ***columns*** du Dataframe souss le format : df.columns = [col1,col2,col3]

#### LES METHODES ET PROPRIETES DE DATAFRAME

La plupart des méthodes et les propriété de Dataframes sont similaires à celles utilisés par l'objet Series, la plupart du temps il suffit d'intégrer les information relative aux colonnes dans l'opération.

##### Trier les données

On retrouve les méthode ***sort_index()*** et ***sort_values()*** pour trier les Dataframe. 
On intègre juste les colonnes utilisé pour les tri intégré dans le paramêtre ***by*** (nom de colonne ou tableau)
Ces méthodes renvoient une copie du dataframe trié par défaut, mais comme précédement on peut utiliser le paramêtre inplace pour remplacer le Dataframe d'origine.

```python
df.sort_values(by='densite', inplace=True)
"""
      pays  densite
id                 
R   Russie     8.57
M    Maroc    65.46
F   France   117.63
I   Italie   200.27
"""
```

##### Supprimer les ligne en double

Comme sur Series, la fonction ***drop_duplicates()*** permet de supprimer les lignes en doubles.

##### Remplir/Supprimer les valeurs nulles

Comme pour les Series, la méthode ***fillna()***, permet de remplacer toutes les valeurs NaN du Dataframe par une valeur.

La méthode ***dropna()*** supprime toute les lignes contenant **au moins une valeur NaN**, en intégrant le parametre ***how=all*** on ne supprime que les lignes avec **toutes les valeurs NaN**.  
On peut appliquer la méthode sur une colonne en passant le paramêtre ***axis=1***.

```python

# je prepare un dataframe avec des valeur NaN
s = df.pays.loc[['I','M']]
df['pays_plus'] = s

print(df)
"""
      pays  densite pays_plus
id                           
R   Russie     8.57       NaN
I   Italie   200.27    Italie
M    Maroc    65.46     Maroc
F   France   117.63       NaN
"""


df.dropna()
"""
     pays  densite pays_plus
I  Italie   200.27    Italie
M   Maroc    65.46     Maroc
"""

df.dropna(axis=1)
"""
     pays  densite
R  Russie     8.57
I  Italie   200.27
M   Maroc    65.46
F  France   117.63
"""

df.fillna("NoName")
"""
     pays  densite pays_plus
R  Russie     8.57    NoName
I  Italie   200.27    Italie
M   Maroc    65.46     Maroc
F  France   117.63    NoName
"""
```

##### Renvoyer une/plusieurs valeurs ciblées

Même fonctionnement que les Series, on intègre juste les informations sur les colonnes:

```python
print(df.at['R','densite']) # recuperation d'une valeur en R, 'densite'
# 8.57

print(df.loc[['R','I'],['densite', 'pays']]) # idem R,I et densite, pays, 
"""
   densite    pays
id                 
R      8.57  Russie
I    200.27  Italie
"""

print(df.loc[['R','I']]) # index R,I toutes colonnes
"""
      pays  densite
id                 
R   Russie     8.57
I   Italie   200.27
"""

# autre formulation possible en pointant directement sur la series
print(df.pays.loc[['I','M']])
"""id
I    Italie
M     Maroc
Name: pays, dtype: object
"""
```

#### Filtrer les données

Comme pour les Series, on utilise des ***Serie de conditions*** pour filter les données de des dataframes.
Ces valeurs de condition peuvent être:
* injecté en tant qu'attribut du Dataframe : `df[condition]`
* utilisé comme utilisant l'attribut ***loc[]***, ce qui nous permet de selectionner les colonnes.

```python
# condition densite sup 100
df[df.densite > 100]
"""
      pays  densite
id                 
I   Italie   200.27
F   France   117.63
"""

# condition + selection pays
df.loc[df.densite>100, 'pays']
"""
I    Italie
F    France
Name: pays, dtype: object
"""

# similaire à la solution ci dessus
df['densite'].loc[df.densite>100]
```

Comme sur les Series, on peut chainer les conditions avec des opérateur logique binaires (&, |, ~).

#### Operation sur les Dataframes

Comme les Series, on peut effectuer des opérations sur les dataframes.
Le fonctionnement est similaire à celui des series, les opération sont effectués sur chaque valeur du dataframe.

On peut également utiliser la méthode ***apply()***.

#### Assemblage de Dataframe

La méthode de pandas ***concat()*** vu précédement permet de faire des concatenation de DataFrame.
On peut également utiliser la méthode de Dataframe **merge()** de pandas.
Il est également possible de joindre des Dataframes en utilisant les méthodes ***join()*** pour effectuer des jointures similaire à celle du sql.
























