# Exploration : Informatique Quantique & Oncologie

> "L'excitation autour de l'informatique quantique ne vient pas du fait qu'elle rendra nos ordinateurs un peu plus rapides. Elle vient du fait qu'elle changera la nature même du calcul."

## 1. La Révolution : Du Séquentiel au Simultané

Le calcul quantique permet de résoudre ce qui est physiquement impossible pour un ordinateur classique. La différence tient en une idée : passer du "un par un" au "tout en même temps".

### Le Principe
| Ordinateur Classique | Ordinateur Quantique |
| :--- | :--- |
| **Bits (0 ou 1)** | **Qubits (Superposition)** |
| Traitement en série | Parallélisme Massif |

### L'Excellence Française 🇫🇷
Ce projet s'inspire des travaux de nos prix Nobel :
* **Alain Aspect (2022) :** A prouvé la réalité de l'intrication quantique.
* **Michel H. Devoret :** Pionnier des qubits supraconducteurs (technologie utilisée par IBM).

## 2. L'Objectif : Casser le verrou du Cancer 🧬

Le problème actuel en génomique, c'est **l'explosion combinatoire**.
* Pour comparer un génome tumoral complet au génome sain, il y a trop de données pour un ordinateur classique.
* **L'approche quantique :** Utiliser des algorithmes (comme Grover, simulé ici) pour identifier une mutation unique parmi des milliards de possibilités en un temps record.

## 3. Détails Techniques (Qiskit)

Le fichier `quantum_search.py` est une implémentation de l'algorithme de **Grover**.

**Note sur la simulation :**
Ce code tourne sur un simulateur (`Aer`).
* **Avantage :** C'est mathématiquement parfait (pas de bruit).
* **Limite Physique :** Simuler un système quantique sur un ordinateur classique demande une mémoire exponentielle (Pétaoctets de RAM pour 50 qubits). C'est pourquoi le passage aux vraies machines (malgré leur bruit actuel / NISQ) est l'enjeu futur.
