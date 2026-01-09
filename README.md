# calculator

Le meilleur calculateur du monde.
Il permet de faire des calculs.

## Instalation

Cloner le dépôt sur vôtre machine et entrez dedans.
Exécuté la ligne suivante, afin d'installer les dépendances :
```bash
pip install -r requirements.txt
```

## Run calculator

### Sum

Example : 
```bash
python src/main.py -op sum -val1 1 -val2 2
```

### Tests
```bash
python -m coverage run -m unittest tests/test_calculator.py
coverage report -m
```
