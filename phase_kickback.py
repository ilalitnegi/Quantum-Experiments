from qiskit import QuantumCircuit
from qiskit_aer import Aer

qc= QuantumCircuit(2)


qc.initialize(1,0)
qc.initialize(1 ,1)


qc.h(0)
qc.h(1)

qc.measure_all()
qc.cx(0,1)
qc.h(0)
qc.h(1)

qc.measure_all()
print(qc.draw(output="text"))

sim = Aer.get_backend('aer_simulator')
result = sim.run(qc, shots=2048).result()

# output statistics
counts = result.get_counts()     # extract statistics from results
print(counts)