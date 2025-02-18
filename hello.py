from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.primitives import Sampler

# Create a simple quantum circuit
qc = QuantumCircuit(3)

# Generate a 3-qubit GHZ state
qc.h(0)           # Apply Hadamard gate to the first qubit
qc.cx(0, 1)       # Apply CNOT gate from qubit 0 to qubit 1
qc.cx(1, 2)       # Apply CNOT gate from qubit 1 to qubit 2
qc.measure_all()  # Measure all qubits

# Initialize the simulator
simulator = AerSimulator()

# Create a Sampler instance
sampler = Sampler()

# Run the circuit on the simulator with the specified number of shots
job = sampler.run([qc], shots=128)

# Get the results
result = job.result()

# Access the quasi-distribution from the first result
quasi_dist = result.quasi_dists[0]  # Get QuasiDistribution from result
counts = {format(key, '03b'): int(value * 128) for key, value in quasi_dist.items()}
print('Counts:', counts)
