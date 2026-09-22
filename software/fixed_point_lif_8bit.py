"""
8-bit Fixed-Point LIF Neuron

Purpose:
Test whether a simple LIF neuron can be represented using
8-bit fixed-point arithmetic instead of floating-point arithmetic.
"""

SCALE = 128


class FixedPointLIF:
    def __init__(self, threshold=1.0, decay=0.9):
        self.threshold = int(threshold * SCALE)
        self.decay = int(decay * SCALE)
        self.membrane = 0

    def step(self, input_current):
        input_fixed = int(input_current * SCALE)

        # Apply membrane decay
        self.membrane = (self.membrane * self.decay) // SCALE

        # Integrate input
        self.membrane += input_fixed

        # Generate spike
        if self.membrane >= self.threshold:
            self.membrane = 0
            return 1

        return 0


if __name__ == "__main__":

    neuron = FixedPointLIF(
        threshold=1.0,
        decay=0.9
    )

    inputs = [0.3, 0.4, 0.5, 0.2, 0.7, 0.4, 0.6, 0.1]

    spikes = []

    for current in inputs:
        spike = neuron.step(current)
        spikes.append(spike)

    print("Input currents:", inputs)
    print("8-bit spikes:  ", spikes)
    print("Total spikes:  ", sum(spikes))
