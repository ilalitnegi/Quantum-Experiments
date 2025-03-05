'''
Experiment:: Implementation of Full Adder

Full Adder: Circuit takes 3 input two input values(A,B) and third input 
is carry_in(Cin), gives two output one is sum(S) and second is carry_out (Cout)

Author: github_id
'''

from qiskit import QuantumCircuit
from qiskit_aer import Aer

    

sim = Aer.get_backend('aer_simulator')

results = {}
for i in range(8):
    qc = QuantumCircuit(5, 2)
    
    if i & 1:
        qc.x(0)  # Set qubit 0 to |1⟩
    if i & 2:
        qc.x(1)  # Set qubit 1 to |1⟩
    if i & 4:
        qc.x(2)  # Set qubit 2 to |1⟩

    # Apply the full adder logic
    qc.cx(0,3)
    qc.cx(1,3)
    qc.cx(2,3)


    qc.ccx(0,1,4)
    qc.ccx(0,2,4)
    qc.ccx(1,2,4)    
    # Measure the qubits
    qc.measure(3,0)
    qc.measure(4,1)
    print(f"\n********************Case {i+1}********************")
    print( qc.draw(output="text"))

    result = sim.run(qc, shots=2048).result()

    counts = result.get_counts()
    
    results[i] = counts
    print(f"Input {i} (binary: {i:03b}): {results[i]}")
    print("\n")


