from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def simulation_grover():
    """
    Simulation d'une recherche quantique.
    But : Trouver l'état '11' parmi 4 possibilités en une seule requête.
    """

    # 1. INITIALISATION
    # On prépare 2 Qubits. 
    # Avec 2 qubits, on a 4 états possibles (00, 01, 10, 11).
    n_qubits = 2
    qc = QuantumCircuit(n_qubits, n_qubits)

    # 2. SUPERPOSITION (Porte Hadamard)
    # C'est l'étape clé. On passe d'un état défini (0 ou 1) à une superposition.
    # Concrètement : l'ordinateur traite maintenant les 4 états en même temps.
    qc.h([0, 1])

    # 3. ORACLE (Le "Tag")
    # C'est la fonction qui identifie ce qu'on cherche.
    # Ici, on cherche l'état '11'. L'oracle ne nous donne pas la réponse,
    # mais il inverse le signe de la bonne réponse (inversion de phase) pour la marquer.
    qc.cz(0, 1)

    # 4. DIFFUSEUR (Amplification)
    # À ce stade, la bonne réponse est marquée mais a la même probabilité que les autres.
    # Ce bloc mathématique va "booster" la probabilité de notre cible ('11')
    # et écraser celle des mauvaises réponses.
    qc.h([0, 1])
    qc.z([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])

    # 5. MESURE
    # On force les qubits à choisir un état final (0 ou 1).
    # Grâce à l'amplification, on tombera sur '11' dans 100% des cas théoriques.
    qc.measure([0, 1], [0, 1])

    # --- EXÉCUTION ---
    print("Lancement de la simulation (Backend Aer)...")

    # Utilisation du simulateur parfait (pas de bruit quantique)
    simulator = Aer.get_backend('qasm_simulator')
    
    job = execute(qc, simulator, shots=1024)
    result = job.result()
    counts = result.get_counts(qc)

    # On vérifie qu'on a bien trouvé '11'
    print(f"Résultat de la détection : {counts}")

if __name__ == "__main__":
    simulation_grover()
