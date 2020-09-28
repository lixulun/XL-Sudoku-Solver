# XL-Sudoku-Solver

## Install
```
pip install sudokuless
```

## Usage
Cmd:
```
problem1.txt:
9x37xxxx1
xxx6xx5xx
x4xxx1xxx
xxx36x2xx
8xxxxxxx4
xx6x97xxx
xxx5xxx2x
xx7xx3xxx
3xxxx28x9
```
```
$ sudokuless --time -f problem1.txt
+-----------+-----------+-----------+
| 9 ! 5 ! 3 | 7 ! 2 ! 4 | 6 ! 8 ! 1 |
| 7 ! 8 ! 1 | 6 ! 3 ! 9 | 5 ! 4 ! 2 |
| 6 ! 4 ! 2 | 8 ! 5 ! 1 | 9 ! 3 ! 7 |
+-----------+-----------+-----------+
| 1 ! 7 ! 4 | 3 ! 6 ! 8 | 2 ! 9 ! 5 |
| 8 ! 3 ! 9 | 2 ! 1 ! 5 | 7 ! 6 ! 4 |
| 5 ! 2 ! 6 | 4 ! 9 ! 7 | 3 ! 1 ! 8 |
+-----------+-----------+-----------+
| 4 ! 9 ! 8 | 5 ! 7 ! 6 | 1 ! 2 ! 3 |
| 2 ! 1 ! 7 | 9 ! 8 ! 3 | 4 ! 5 ! 6 |
| 3 ! 6 ! 5 | 1 ! 4 ! 2 | 8 ! 7 ! 9 |
+-----------+-----------+-----------+
Cost: 0.171875s
```