"""
Baseline Spiking Neural Network

Software baseline using a Leaky Integrate-and-Fire (LIF) neuron.
"""

class LIFNeuron:
    def __init__(self, threshold=1.0, decay=0.9):
        self.threshold = threshold
        self.decay = decay
        self.membrane = 0.0

    def step(self, input_current):
        # Leak the previous membrane potential
        self.membrane *= self.decay

        # Integrate the new input
        self.membrane += input_current

        # Generate spike when threshold is reached
        if self.membrane >= self.threshold:
            self.membrane = 0.0
            return 1

        return 0


# Simple baseline experiment
if __name__ == "__main__":

    neuron = LIFNeuron(
        threshold=1.0,
        decay=0.9
    )

    inputs = [0.3, 0.4, 0.5, 0.2, 0.7, 0.4, 0.6, 0.1]

    spikes = []

    for current in inputs:
        spike = neuron.step(current)
        spikes.append(spike)

    print("Input currents:", inputs)
    print("Spike output:  ", spikes)
    print("Total spikes:  ", sum(spikes))
