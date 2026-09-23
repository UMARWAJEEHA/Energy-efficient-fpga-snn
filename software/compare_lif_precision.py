"""
Compare floating-point, 8-bit, and 6-bit fixed-point LIF neurons.
"""

from baseline_snn import LIFNeuron
from fixed_point_lif_8bit import FixedPointLIF
from fixed_point_lif_6bit import FixedPointLIF6Bit


inputs = [0.3, 0.4, 0.5, 0.2, 0.7, 0.4, 0.6, 0.1]


def run_neuron(neuron):
    spikes = []

    for current in inputs:
        spikes.append(neuron.step(current))

    return spikes


# Floating-point baseline
float_spikes = run_neuron(
    LIFNeuron(threshold=1.0, decay=0.9)
)

# 8-bit fixed-point
eight_bit_spikes = run_neuron(
    FixedPointLIF(threshold=1.0, decay=0.9)
)

# 6-bit fixed-point
six_bit_spikes = run_neuron(
    FixedPointLIF6Bit(threshold=1.0, decay=0.9)
)


def agreement(reference, comparison):
    matches = sum(
        a == b for a, b in zip(reference, comparison)
    )

    return (matches / len(reference)) * 100


print("Floating-point spikes:", float_spikes)
print("8-bit spikes:        ", eight_bit_spikes)
print("6-bit spikes:        ", six_bit_spikes)

print()
print("Floating-point spike count:", sum(float_spikes))
print("8-bit spike count:        ", sum(eight_bit_spikes))
print("6-bit spike count:        ", sum(six_bit_spikes))

print()
print(
    "8-bit output agreement: {:.1f}%".format(
        agreement(float_spikes, eight_bit_spikes)
    )
)

print(
    "6-bit output agreement: {:.1f}%".format(
        agreement(float_spikes, six_bit_spikes)
    )
)
