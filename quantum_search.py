# Exploration : Algorithme de Grover (Recherche de Mutation)
# Auteur : Sacha Miloch-Cohen
# Framework : Qiskit

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def simulation_grover():
    """
    Simulation : Trouver la combinaison '11' (la mutation) parmi 4 possibilités.
    """

    # 1. INITIALISATION (Les 4 cartes)
    # On utilise 2 Qubits. 
    # Cela nous donne 4 états possibles : 00, 01, 10, 11.
    n_qubits = 2
    qc = QuantumCircuit(n_qubits, n_qubits)

    # 2. SUPERPOSITION (Tout regarder en même temps)
    # La porte 'H' (Hadamard) met les qubits dans tous les états à la fois.
    # L'ordinateur a maintenant les 4 cartes "en main" simultanément.
    qc.h([0, 1])

    # 3. L'ORACLE (Marquer le suspect)
    # On cherche l'état '11'.
    # La porte 'CZ' agit comme un filtre. Elle reconnait '11' et inverse son signe.
    # Concrètement : Les autres états restent positifs (+), l'état '11' devient négatif (-).
    # C'est ce "tag" mathématique qui permet de le différencier.
    qc.cz(0, 1)

    # 4. AMPLIFICATION (Le rendre visible)
    # C'est l'étape mathématique (Inversion autour de la moyenne).
    # Sans rentrer dans les maths complexes : cette étape utilise l'état négatif (-) 
    # créé juste avant pour booster sa probabilité à 100%.
    # Elle transfère la probabilité des mauvaises réponses vers la bonne.
    qc.h([0, 1])
    qc.z([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])

    # 5. MESURE (Le verdict)
    # On force le système à choisir une réponse finale.
    # Grâce à l'étape 4, il est obligé de choisir '11'.
    qc.measure([0, 1], [0, 1])

    # --- LANCEMENT ---
    print(">>> Démarrage du simulateur...")
    
    # On utilise un simulateur classique parfait (Aer).
    # Comme expliqué dans le README, c'est possible car on a peu de qubits.
    # Avec 50 qubits, mon PC exploserait (manque de RAM).
    simulator = Aer.get_backend('qasm_simulator')
    
    # On lance l'expérience 1024 fois pour avoir une preuve statistique.
    job = execute(qc, simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)

    print(f">>> Résultat (Combien de fois on a trouvé '11') : {counts}")

if __name__ == "__main__":
    simulation_grover()
