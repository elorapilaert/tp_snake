# TP - Le snake

## Contexte

L'objectif de ce TP est d'apprendre à concevoir et à réaliser un programme complet.

Le jeu repose sur une idée simple : le serpent est une **liste de cases**. Pour le faire avancer, on ajoute une nouvelle tête dans la direction courante et on retire la queue. Tout le reste (fruit, score, fin de partie) s'appuie sur cette représentation.

Adapté du TP « Le snake » de Thierry Parmentelat et Aurélien Noce : https://python-exos.info-mines.paris/tps/snake/readme-snake-nb/

## Installation

L'environnement de travail est créé dans la partie 0.

Documentation de Pygame : https://www.pygame.org/docs/

## Structure du projet

```text
tp_snake/ # RESPECTER les noms. J'utilise des command git pour récupérer vos tps et ça me simplifit la vie si vous avez tous le même nom de répertoire. 
└── snake.py   # tout le jeu
```

Lancement : `python snake.py`

Règles de travail :

- Tout se passe dans **un seul fichier** `snake.py`, modifié à chaque étape.
- Le code ne fonctionne **pas dans un notebook Jupyter** : travaillez dans un éditeur (VS Code) et lancez depuis un terminal.
- Faites **un commit par étape** qui fonctionne. En cas de bug, vous pouvez ainsi vous concentrer sur ce qui a changé depuis la dernière version qui marchait.

## 0. Environnement de travail

Un environnement virtuel isole les bibliothèques d'un projet : ce qu'on installe pour le snake n'affecte pas le reste de la machine.

### Aide — Commandes utiles

| Action | Commande |
|---|---|
| Lister les environnements | `conda env list` |
| Activer un environnement | `conda activate snake` |
| Désactiver l’environnement actif | `conda deactivate` |
| Afficher l’environnement actif | `echo $CONDA_DEFAULT_ENV` |
| Créer un environnement | `conda create -n test python=3.12` |
| Supprimer un environnement | `conda env remove -n test` |

**Attention :** sous Windows, dans le terminal classique `cmd`, utilisez `echo %CONDA_DEFAULT_ENV%` à la place de `echo $CONDA_DEFAULT_ENV`. Dans PowerShell, utilisez `$env:CONDA_DEFAULT_ENV`.

### 0.1. Créer l'environnement

**Consigne :** avec `conda`, créez un environnement nommé `snake` utilisant Python 3.12.

### 0.2. Activer l'environnement

**Consigne :** activez l'environnement `snake`.

**Question :** comment savoir dans quel environnement on se trouve ?

### 0.3. Installer Pygame

**Consigne :** installez `pygame` avec `pip`, vérifiez la version installée, puis lancez le programme d'exemple fourni par la bibliothèque pour tester l'installation.

<details>
<summary><b>Indice</b></summary>

Pour afficher les informations d'un paquet installé, utilisez `pip show`. Les exemples de Pygame se lancent avec `python -m pygame.examples.aliens`.

</details>


### 0.4. Créer le projet

**Consigne :** créez le dossier `mysnake`, placez-vous dedans et initialisez un dépôt Git. Dans VS Code, ouvrez ce dossier et sélectionnez l'interpréteur Python de l'environnement `snake` (clic sur la version de Python en bas de la fenêtre).

Pour la suite : `conda deactivate` permet de quitter l'environnement et `conda env remove -n snake` de le supprimer à la fin du TP.

---

## 1. Fenêtre et boucle de jeu

### 1.1. Code de démarrage

Créez `snake.py` avec le code suivant :

```python
from random import randint
import pygame as pg

pg.init()
screen = pg.display.set_mode((600, 600))
clock = pg.time.Clock()

while True:
    clock.tick(1)

    for event in pg.event.get():
        pass

    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.fill(random_color)
    pg.display.update()
```

- `clock.tick(1)` limite la boucle à 1 image par seconde.
- `pg.event.get()` doit être appelé à chaque image, sinon la fenêtre ne s'affiche pas correctement.
- `pg.display.update()` produit réellement l'affichage. Les autres calculs se font en mémoire, ce qui est très rapide ; l'affichage est beaucoup plus lent. On l'appelle donc **une seule fois par itération**.

**Consigne :** lancez le programme avec `python snake.py`.

**Question :** pourquoi ne peut-on pas fermer la fenêtre avec la croix ? Comment arrêter le programme ?

Faites un commit.

### 1.2. Quitter proprement

Afin d’avoir un comportement plus “normal”, nous devons instruire Pygame en lui disant comment réagir aux clicks sur le clavier ou sur la fenêtre:

**Consigne :** modifiez le programme pour pouvoir quitter avec la croix de la fenêtre ou avec la touche `q`, puis appelez `pg.quit()` après la boucle.

<details>
<summary><b>Indice 1</b></summary>

Il vous faut une variable booléenne qui contrôle la boucle `while`.

</details>

<details>
<summary><b>Indice 2</b></summary>

Un événement de type `pg.QUIT` correspond à la croix. Un événement de type `pg.KEYDOWN` correspond à une touche enfoncée ; la touche se lit dans `event.key` (par exemple `pg.K_q`).

</details>

Faites un commit.

---

## 2. Le damier

Le plateau de jeu est découpé en 30 x 30 cases de 20 pixels de côté, soit une fenêtre de 600 x 600 pixels.

### 2.1. Dessiner un rectangle

Pygame dessine un rectangle avec `pg.draw.rect` :

```python
x, y = 100, 200            # coin supérieur gauche, en pixels
width, height = 20, 20     # largeur et hauteur, en pixels
color = (255, 0, 0)        # rouge, en (R, V, B)

rect = pg.Rect(x, y, width, height)
pg.draw.rect(screen, color, rect)
```

**Consigne :** à la place de la couleur aléatoire, remplissez l'écran en noir puis dessinez un carré rouge de 20 pixels en $(100, 200)$.

### 2.2. Le damier

**Consigne :** écrivez une fonction `draw_board()` qui dessine les cases blanches d'un damier de 30 x 30 cases (une case sur deux, en alternance d'une colonne à l'autre).

<details>
<summary><b>Indice 1</b></summary>

Dans une colonne, il y a 15 cases blanches, séparées d'une case noire : leurs ordonnées sont espacées de 40 pixels.

</details>

<details>
<summary><b>Indice 2</b></summary>

D'une colonne à la suivante, on avance de 20 pixels en abscisse, et la première case blanche passe de $y = 0$ à $y = 20$ (puis inversement).

</details>

**Question :** combien de rectangles sont dessinés à chaque image ?

Faites un commit. Le damier reste le fond d'écran pour toute la suite.

---

## 3. Un serpent qui bouge

Les positions sont exprimées **en cases**, pas en pixels : la case $(10, 15)$ occupe le carré de pixels dont le coin est en $(200, 300)$.

### 3.1. Dessiner le serpent

Le serpent est une liste de cases. Par convention ici, le premier élément est la **queue** et le dernier est la **tête** :

```python
SNAKE = [
   (10, 15),
   (11, 15),
   (12, 15),
]
```

**Consigne :** écrivez `draw_snake(snake)` qui dessine chaque segment en rouge, puis appelez-la dans la boucle après `draw_board()`.

<details>
<summary><b>Indice</b></summary>

Pour passer des cases aux pixels, multipliez les coordonnées par la taille d'une case (20).

</details>

Faites un commit.

### 3.2. Déplacer le serpent

Le serpent avance dans une **direction**, un vecteur de déplacement en cases :

```python
DIRECTION = (1, 0)   # vers la droite
```

**Consigne :** écrivez `move_snake(snake, direction)` qui ajoute une nouvelle tête (ancienne tête + direction), retire la queue et retourne le serpent.

<details>
<summary><b>Indice 1</b></summary>

La tête est le dernier élément de la liste.

</details>

<details>
<summary><b>Indice 2</b></summary>

Utilisez `append` pour la nouvelle tête et `pop(0)` pour retirer la queue.

</details>

**Tests :** ajoutez temporairement ces lignes après la définition de la fonction, puis retirez-les.

```python
assert move_snake([(10, 15), (11, 15), (12, 15)], (1, 0)) == [(11, 15), (12, 15), (13, 15)]
assert move_snake([(10, 15), (11, 15), (12, 15)], (0, -1)) == [(11, 15), (12, 15), (12, 14)]
```

### 3.3. Intégrer le déplacement

**Consigne :** définissez `DIRECTION = (1, 0)` avant la boucle, appelez `move_snake` à chaque itération, puis réglez `clock.tick(2)` pour bien voir le déplacement.

**Question :** que se passe-t-il quand le serpent atteint le bord de la fenêtre ?

Faites un commit.

---

## 4. Contrôler la direction

**Consigne :** faites changer `DIRECTION` avec les quatre flèches du clavier (`pg.K_UP`, `pg.K_DOWN`, `pg.K_LEFT`, `pg.K_RIGHT`).

<details>
<summary><b>Indice</b></summary>

Les touches sont traitées dans la boucle d'événements, dans la branche `KEYDOWN`. Pour chaque flèche, affectez le bon vecteur à `DIRECTION`.

</details>

**Question :** pourquoi la direction vers le haut est-elle $(0, -1)$ ?

**Bonus :** empêchez le serpent de faire demi-tour (par exemple aller à gauche alors qu'il va vers la droite). Cette protection n'est pas incluse dans `snake.py`.

Faites un commit.

---

## 5. Le fruit et le score 

### 5.1. Dessiner le fruit

Le fruit est une case, placée au hasard sur le plateau :

```python
FRUIT = (randint(0, 29), randint(0, 29))
```

**Consigne :** écrivez `draw_fruit(fruit)` qui dessine le fruit en vert.

### 5.2. Manger le fruit

**Consigne :** écrivez `eat_fruit(score, snake, fruit)` qui retourne le triplet `(score, snake, fruit)`. Si la tête du serpent est sur le fruit : le score augmente de 1, un nouveau fruit est placé au hasard et le serpent s'allonge d'une case.

<details>
<summary><b>Indice 1</b></summary>

La tête est `snake[-1]`. Comparez-la directement au fruit.

</details>

<details>
<summary><b>Indice 2</b></summary>

Pour allonger le serpent, ajoutez un segment au début de la liste avec `insert(0, ...)`.

</details>

**Tests :**

```python
score, snake, fruit = eat_fruit(0, [(10, 15), (11, 15), (12, 15)], (12, 15))
assert score == 1 and len(snake) == 4

score, snake, fruit = eat_fruit(0, [(10, 15), (11, 15), (12, 15)], (0, 0))
assert score == 0 and len(snake) == 3 and fruit == (0, 0)
```

**Question :** pourquoi insère-t-on une copie de `snake[0]` plutôt qu'un segment à une autre position ?

### 5.3. Intégrer

**Consigne :** définissez `FRUIT` et `SCORE` avant la boucle, puis appelez `eat_fruit` après le déplacement et `draw_fruit` après `draw_snake`.

Faites un commit.

---

## 6. Fin de partie 

### 6.1. Détecter et annoncer la défaite

Le serpent perd s'il se mord : sa tête arrive sur une case déjà occupée par son corps.

**Consigne :** écrivez `game_over(snake)` qui retourne `True` si le serpent se mord. Dans ce cas, elle affiche aussi "Game Over" pendant 2 secondes. Dans la boucle, arrêtez le jeu quand elle retourne `True`.

<details>
<summary><b>Indice 1</b></summary>

La tête est `snake[-1]` et le corps est `snake[:-1]`. L'opérateur `in` teste l'appartenance.

</details>

<details>
<summary><b>Indice 2</b></summary>

Pour écrire un texte : créez une police avec `pg.font.Font(None, 74)`, produisez une image avec `font.render(...)`, collez-la avec `screen.blit(...)`, puis affichez avec `pg.display.flip()` et attendez avec `pg.time.wait(2000)`.

</details>

**Tester puis commit !**
### 6.2. Afficher le score

**Consigne :** affichez le score dans le titre de la fenêtre, à chaque itération.

<details>
<summary><b>Indice</b></summary>

Utilisez `pg.display.set_caption(...)` avec une f-string.

</details>

Le code complet de la solution est dans `snake.py`. Faites un dernier commit.


## Pour aller plus loin

1. **Variables globales :** les fonctions de dessin utilisent la variable globale `screen`. Modifiez le code pour passer `screen` en paramètre et réduire le nombre de variables globales.
2. **Ligne de commande :** avec le module `argparse`, permettez de choisir le nombre de cases, la taille d'une case en pixels et la vitesse du jeu.
3. **Vitesse de réaction :** avec `clock.tick(1)`, la touche `q` répond-elle immédiatement ? Le serpent tourne-t-il parfois trop tard ? Modifiez le code pour améliorer la réactivité.
4. **Deux fréquences :** séparez la fréquence d'affichage (images par seconde) de la fréquence de déplacement du serpent (cases par seconde).
5. **Cas non traités :** que se passe-t-il quand le serpent sort du plateau ? Que se passe-t-il quand un nouveau fruit apparaît sur le serpent ? Corrigez ces deux cas.