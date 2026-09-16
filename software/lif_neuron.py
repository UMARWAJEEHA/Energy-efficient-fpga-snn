import matplotlib.pyplot as plt

# LIF neuron parameters
V_rest = 0.0
V_reset = 0.0
V_threshold = 1.0
tau = 5.0

# Input current
input_current = [
    0, 0, 1, 1, 1,
    0, 0, 1, 1, 1,
    0, 0, 1, 1, 1
]

V = V_rest

membrane_potential = []
output_spikes = []

for I in input_current:

    # Update membrane potential
    V = V + (-(V - V_rest) + I) / tau

    # Check threshold
    if V >= V_threshold:
        spike = 1
        V = V_reset
    else:
        spike = 0

    membrane_potential.append(V)
    output_spikes.append(spike)

print("Membrane potential:")
print(membrane_potential)

print("\nOutput spikes:")
print(output_spikes)

# Plot membrane potential
plt.plot(membrane_potential)
plt.axhline(V_threshold, linestyle="--")

plt.xlabel("Time Step")
plt.ylabel("Membrane Potential")
plt.title("LIF Neuron Simulation")
plt.show()
