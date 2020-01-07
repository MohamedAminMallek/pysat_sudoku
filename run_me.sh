#!/bin/sh

python generateEmptySudoku.py > sudoku_new.cnf

python pysat.py sudoku_new.cnf

python gensudoku.py solution.cnf