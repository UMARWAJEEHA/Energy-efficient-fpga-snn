"""
Compare floating-point and 8-bit fixed-point LIF neurons.
"""

from baseline_snn import LIFNeuron
from fixed_point_lif_8bit import FixedPointLIF


inputs = [0.3, 0.4, 0.5, 0.2, 0.7, 0.4, 0.6, 0.1]


# Floating-point baseline
float_neuron = LIFNeuron(threshold=1.0, decay=0.9)
float_spikes = []

for current in inputs:
    float_spikes.append(float_neuron.step(current))


# 8-bit fixed-point
fixed_neuron = FixedPointLIF(threshold=1.0, decay=0.9)
fixed_spikes = []

for current in inputs:
    fixed_spikes.append(fixed_neuron.step(current))


# Compare results
matching_outputs = sum(
    a == b for a, b in zip(float_spikes, fixed_spikes)
)

match_percentage = (
    matching_outputs / len(inputs)
) * 100


print("Floating-point spikes:", float_spikes)
print("8-bit fixed-point:    ", fixed_spikes)

print("Floating-point spike count:", sum(float_spikes))
print("8-bit spike count:        ", sum(fixed_spikes))

print("Output agreement: {:.1f}%".format(match_percentage))
