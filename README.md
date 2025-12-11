# Exploration : Informatique Quantique & Oncologie

> "L'excitation autour de l'informatique quantique ne vient pas du fait qu'elle rendra nos ordinateurs un peu plus rapides. Elle vient du fait qu'elle changera la nature même du calcul."

## 1. La Révolution : Du Séquentiel au Simultané

Le calcul quantique permet de résoudre ce qui est physiquement impossible pour un ordinateur classique. La différence tient en une idée : passer du "un par un" au "tout en même temps".

### Le Principe
* **Classique (Bits) :** Traitement en série. Analogie : Un GPS qui teste chaque route une par une.
* **Quantique (Qubits) :** Parallélisme Massif. Analogie : Un GPS qui explore toutes les routes à la fois.

## 🇫🇷 Contexte : L'Excellence Scientifique Française

Ce projet s'inscrit dans une dynamique d'innovation portée par des figures majeures de la physique mondiale :

* **Alain Aspect (Nobel 2022) :** A prouvé la réalité de l'intrication quantique (violation des inégalités de Bell), confirmant que deux particules peuvent rester liées quelle que soit la distance.
* **Michel H. Devoret (Nobel 2025) :** A démontré l'existence du **tunnel quantique à l'échelle macroscopique**. Ses travaux ont prouvé qu'un circuit électrique entier (et pas juste un atome) pouvait se comporter comme un système quantique, posant les bases physiques des ordinateurs quantiques actuels (Qubits supraconducteurs).

## 2. L'Objectif : Casser le verrou du Cancer 🧬

Le problème actuel en génomique, c'est **l'explosion combinatoire**.
Pour comparer un génome tumoral complet au génome sain, il y a trop de données. L'approche quantique permet d'utiliser des algorithmes de recherche pour identifier une mutation unique parmi des milliards de possibilités en un temps record.

---

## 3. Comprendre le Code : L'Algorithme de Grover 🔎

Le fichier `quantum_search.py` est une simulation. Voici comment ça marche sans jargon compliqué.

### L'Analogie des 4 Cartes 🃏
Imaginez 4 cartes faces cachées. L'une d'elles est l'As de Cœur (la mutation).
* **Un ordinateur classique** doit retourner les cartes une par une (moyenne : 2,5 essais).
* **L'algo de Grover** trouve la carte en **une seule opération**.

### Comment ça marche ? (La notion d'Amplitude)
En quantique, on ne parle pas juste de 0 ou 1, mais "d'amplitude de probabilité". Imaginez ça comme le volume sonore d'une piste audio.
1.  **Superposition :** Au début, toutes les cartes ont le même "volume". L'ordi les considère toutes égales.
2.  **L'Oracle (Le Marquage) :** L'ordi repère l'As de Cœur mais ne nous le montre pas. À la place, il inverse sa phase (il met son volume en "négatif").
3.  **L'Amplification (Inversion autour de la moyenne) :** C'est une opération mathématique complexe. En gros, l'ordi va utiliser cette valeur "négative" pour aspirer tout le "volume" des mauvaises cartes et le donner à l'As de Cœur.
    * *Résultat :* L'As de Cœur se retrouve avec 100% de probabilité (volume max), et les autres 0%.

---

## 4. Pourquoi simuler ? (Le problème des Pétaoctets)

J'utilise **Qiskit** (IBM) avec un simulateur (`Aer`). C'est un programme classique qui imite un ordi quantique.

### Le Paradoxe
* **Le Simulateur est parfait :** Il n'y a pas d'erreur de calcul.
* **Mais il est limité :** Pour simuler un système quantique, il faut stocker des nombres complexes pour chaque état possible.
    * Simuler 2 qubits = Facile.
    * Simuler 50 qubits = Impossible sur un ordi classique. Cela demanderait des **Pétaoctets de RAM** (plus que la mémoire de tous les supercalculateurs du monde réunis).

C'est pour ça qu'on a besoin de construire de vrais ordinateurs quantiques : pour dépasser cette limite physique de la mémoire classique.
