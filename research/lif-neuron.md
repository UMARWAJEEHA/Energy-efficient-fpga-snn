# Leaky Integrate-and-Fire (LIF) Neuron

## Objective

The objective of this experiment is to understand and implement a simplified Leaky Integrate-and-Fire (LIF) neuron as the basic computational element of a spiking neural network.

## Basic Operation

The LIF neuron follows four main steps:

1. Receive input spikes or current.
2. Integrate the input into the membrane potential.
3. Compare the membrane potential with a firing threshold.
4. Generate an output spike and reset the membrane potential when the threshold is reached.

## Computational Model

The membrane potential is updated at each discrete time step:

V[t+1] = V[t] + (-(V[t] - V_rest) + I[t]) / tau

If:

V[t+1] >= V_threshold

the neuron generates an output spike.

After generating a spike, the membrane potential is reset to V_reset.

## Hardware Perspective

The LIF neuron can be implemented digitally using:

* Registers for membrane potential
* Arithmetic logic for membrane-potential updates
* A comparator for threshold detection
* Control logic for resetting the neuron
* Input logic for receiving spikes

## Research Relevance

This experiment establishes the software-level behavior that will later be mapped to FPGA hardware.

The eventual hardware implementation will be evaluated using metrics such as:

* LUT utilization
* Flip-flop utilization
* BRAM utilization
* Maximum operating frequency
* Latency
* Power consumption
* Energy per inference
* Classification accuracy

## Next Step

The next step is to implement the LIF neuron in Python and verify its behavior using a simple spike-input sequence.
