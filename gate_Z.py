'''
Experiment:: Implementation of Z Gate

CNOT Gate: Takes 1 input (Qubit) || Output: Flips input Qubit 

Author: github_id
'''

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, plot_state_qsphere
import matplotlib.pyplot as plt
# create quantum circuit
qc = QuantumCircuit(1)

qc.z(0)                          # add a gate to the circuit
qc.measure_all()                 # add measurement at the end

# run
sim = Aer.get_backend('aer_simulator')
result = sim.run(qc).result()  # run circuit, get results



print(qc.draw(output="mpl", filename='x_gate.png'))
print(qc.draw(output="text"))

# output statistics
counts = result.get_counts()     # extract statistics from results
print(counts)

hist = plot_histogram(counts)

hist.savefig('hist.png')