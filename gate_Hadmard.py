'''
Experiment:: Implementation of Hadmard Gate

CNOT Gate: Takes 1 input (Qubit) || Output: Qubit(Superposition)

Author: github_id
'''

from qiskit import QuantumCircuit
from qiskit_aer import Aer
import qiskit.quantum_info as qi
# create quantum circuit
qc = QuantumCircuit(1,1)

qc.initialize(1,0)

qc.h(0)     # add a gate to the circuit

state = qi.Statevector.from_instruction(qc)
print(state.draw(output='text'))


qc.measure(0,0)                # add measurement at the end


# run
sim = Aer.get_backend('aer_simulator')
result = sim.run(qc).result()  # run circuit, get results

print(qc.draw(output="mpl", filename='hadmard_gate.png'))
print(qc.draw(output="text"))

# output statistics
counts = result.get_counts()     # extract statistics from results
print(counts)

