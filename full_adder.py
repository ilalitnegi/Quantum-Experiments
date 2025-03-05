'''
Experiment:: Implementation of Full Adder

Full Adder: Circuit takes 3 input two input values(A,B) and third input 
is carry_in(Cin), gives two output one is sum(S) and second is carry_out (Cout)

Author: github_id
'''

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, circuit_drawer 

print("\n Quantum Computing Experiment:: Full Adder")
q0 = input("Enter First Number:")
q1 = input("Enter Second Number:")
q2 = input("Enter Carry_in:")

print("\n******Entered Three Qubits******")
print(f"First Qubit(q0) = |{q0}>")
print(f"Second Qubit(q1) = |{q1}>")
print(f"Third Qubit(q2) = |{q2}>")

qc=QuantumCircuit(5,2)
qc.initialize(q0,0)
qc.initialize(q1,1)
qc.initialize(q2,2)


qc.cx(0,3)
qc.cx(1,3)
qc.cx(2,3)
qc.measure(3,0)


qc.ccx(0,1,4)
qc.ccx(0,2,4)
qc.ccx(1,2,4)
qc.measure(4,1)
print("\n")

print( qc.draw(output="text"))
qc.draw(output='mpl', style={'backgroundcolor': '#EEEEEE'}, filename='full_adder.png')


sim = Aer.get_backend('aer_simulator')
result = sim.run(qc, shots=2048).result()

counts = result.get_counts()

print("\n Result:: Cout Sum",counts)

