import matplotlib.pyplot as plt 
from qiskit import QuantumCircuit, Aer, execute

# Définition de la matrice de Pauli X (porte X)
X = [[0,1],[1,0]]

# Définition du circuit quantique pour le code de Shor
q = QuantumCircuit(9, 3)
q.cx(0, 3)
q.cx(1, 3)
q.cx(2, 3)
q.cx(3, 6)
q.cx(4, 6)
q.cx(5, 6)
q.cx(6, 7)
q.cx(7, 8)
q.h(range(0,9)) 

# Application de l'erreur
q.x(0)

# Correction de l'erreur
q.cx(8, 7)
q.cx(7, 6)
q.cx(6, 3)
q.cx(5, 6)
q.cx(4, 6)
q.cx(3, 6)
q.cx(2, 3)
q.cx(1, 3)
q.cx(0, 3)

# Mesure des qubits
q.measure([3, 6, 7], [0, 1, 2])

# Dessin du circuit
q.draw(output='mpl')
plt.show()


# Exécution du circuit quantique
simulator = Aer.get_backend('qasm_simulator')
job = execute(q, simulator, shots=1000)
result = job.result()
counts = result.get_counts(q)
print(counts)

# Affichage de l'histogramme
plt.bar(counts.keys(), counts.values())
plt.xlabel('Résultats')
plt.ylabel('Fréquence')
plt.show()