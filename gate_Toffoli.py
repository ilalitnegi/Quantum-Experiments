'''
Experiment:: Implementation of CNOT Gate

CNOT Gate: Takes 3 input (2 Control Qubits Target Qubit) || Output: Target Qubit remains same if either or both Control Qubits are 0, otherwise Target Qubit flips if Both Control Qubits are 1.

Author: github_id
'''

from qiskit import QuantumCircuit
from qiskit_aer import Aer

# create quantum circuit
qc = QuantumCircuit(3,1)

qc.initialize(1,0)
qc.initialize(0,1)
qc.initialize(1,2)

qc.ccx(0,1,2)                     # add a gate to the circuit
qc.measure(2,0)                 # add measurement at the end

# run
sim = Aer.get_backend('aer_simulator')
result = sim.run(qc).result()  # run circuit, get results

print(qc.draw(output="mpl", filename='toffoli_gate.png'))
print(qc.draw(output="text"))

# output statistics
counts = result.get_counts()     # extract statistics from results
print(counts)

