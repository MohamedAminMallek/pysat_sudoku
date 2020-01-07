![Supported Python Versions](https://img.shields.io/badge/Python->=3.6-blue.svg?logo=python&logoColor=white)

# TP Génération SUDOKU

*Mohamed Amin Mallek & EMBOUAZZA Fares*

Ce dépôt contient nos travaux concernant le TP de génération de sudoku.
Afin d'utiliser notre travail, vous devez cloner ou télécharger ce dépôt sur votre machine locale et exécuter certaines fonctions détaillées ci-après.

> Ce TP à été réalisé lors du cours de représentation des connaissances donné à L'ENSEIRB Matmeca par Laurent SIMON.

## Explication du dépôt

### Exécution du code:

- ▶️️ Téléchargement du dépôt *pysat_sudoku*: [source](https://github.com/MohamedAminMallek/pysat_sudoku)

- ▶️️ Exécution du fichier Bash *run_me.sh*: [source](https://github.com/MohamedAminMallek/pysat_sudoku/blob/master/run_me.sh)

### Détails des fonctions:

- 📚 [run_me.sh]: [source](https://github.com/MohamedAminMallek/pysat_sudoku/blob/master/run_me.sh) |
Fichier d'exécution principal. Lancer ce fichier bash afin de générer un nouveau sudoku ayant une seule et unique solution. 


- 📚 [generateEmptySudoku.py]: *python generateEmptySudoku.py > sudoku_new.cnf* [source](https://github.com/MohamedAminMallek/pysat_sudoku/blob/master/generateEmptySudoku.py) |
Fichier python permettant de générer les règles du sudoku sous la forme de clauses écritent dans le fichier [sudoku_new.cnf].


- 📚 [pysat.py]: *python pysat.py sudoku_new.cnf* [source](https://github.com/MohamedAminMallek/pysat_sudoku/blob/master/pysat.py) |
Fichier python permettant de générer un sudoku ayant une unique solution à partir d'une grille vide et des règles du sudoku sous la forme de clauses. Les clauses de cette grille sont écrites dans le fichier [solution.cnf].


- 📚 [gensudoku.py]: *python gensudoku.py solution.cnf* [source](https://github.com/MohamedAminMallek/pysat_sudoku/blob/master/gensudoku.py) |
Fichier python permettant de réduire au maximum le nombre d'élément dans la grille tout en restant sur une grille de sudoku ayant une unique solution. 



