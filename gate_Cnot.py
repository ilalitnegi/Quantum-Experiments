'''
Experiment:: Implementation of CNOT Gate

CNOT Gate: Takes 2 input (Control Qubit, Target Qubit) || Output: Target Qubit remains same if Control Qubit is 0, otherwise Target Qubit flips if Control Qubit is 1.

Author: github_id
'''

from qiskit import QuantumCircuit
from qiskit_aer import Aer
# create quantum circuit
qc = QuantumCircuit(2,1)

qc.initialize(1,0)
qc.initialize(1,1)

qc.cx(0,1)                      # add a gate to the circuit
qc.measure(1,0)                 # add measurement at the end

# run
sim = Aer.get_backend('aer_simulator')
result = sim.run(qc).result()  # run circuit, get results

print(qc.draw(output="mpl", filename='cnot_gate.png'))
print(qc.draw(output="text"))

# output statistics
counts = result.get_counts()     # extract statistics from results
print(counts)

