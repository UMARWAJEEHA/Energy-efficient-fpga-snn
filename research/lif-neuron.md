# Leaky Integrate-and-Fire (LIF) Neuron

## 1. Research Objective

The objective of this study is to understand the computational behavior of a Leaky Integrate-and-Fire (LIF) neuron and investigate how its functionality can be mapped from a mathematical/software model to digital hardware for energy-efficient spiking neural network inference.

The LIF neuron is used as the fundamental computational element in this research project.

---

## 2. Why LIF Neurons?

A spiking neural network represents information using discrete spikes rather than conventional continuous-valued neural activations.

The LIF neuron provides a simple model for generating these spikes.

Its operation can be summarized as:

**Input → Integration → Leakage → Threshold → Spike → Reset**

The main state variable is the membrane potential.

When the membrane potential reaches the firing threshold, the neuron produces an output spike and its membrane potential is reset.

---

## 3. Mathematical Model

A simplified discrete-time LIF model can be represented as:

$$
V[t+1] =
V[t] + \frac{-(V[t]-V_{rest}) + I[t]}{\tau}
$$

where:

* \(V[t]\) = membrane potential at time \(t\)
* \(V_{rest}\) = resting membrane potential
* \(I[t]\) = input current
* \(\tau\) = membrane time constant

The neuron generates an output spike when:

$$
V[t+1] \geq V_{threshold}
$$

After firing:

$$
V[t+1] = V_{reset}
$$

Therefore:

```text
Input
  ↓
Membrane potential update
  ↓
Threshold comparison
  ↓
Threshold reached?
  ↓
YES ─────→ Output spike
              ↓
            Reset
```

---

The UT Dallas research group also investigates neuromorphic hardware using emerging technologies such as spintronics, magnetic devices, and memristive technologies.
Friedman's research focuses on neuromorphic computing and the development of efficient computing paradigms using nanoscale phenomena. His research specifically discusses artificial neurons implementing the leaking, integrating, and firing behavior associated with the LIF model.

Reference:

Joseph S. Friedman, NeuroSpinCompute Laboratory, University of Texas at Dallas.

https://personal.utdallas.edu/~joseph.friedman/



---

## 5. Research Relevance

The purpose of citing this work is not to reproduce the same research direction.

Instead, it provides a research foundation for investigating how neural computation can be represented efficiently in hardware.

My research direction focuses on:

* FPGA-based SNN implementation
* Energy-efficient neural computation
* Digital LIF neuron architectures
* Hardware–software co-design
* Resource-efficient SNN inference
* FPGA resource utilization
* Latency and throughput
* Power and energy efficiency

This creates a bridge between conventional FPGA-based intelligent systems and emerging neuromorphic computing architectures.

---

## 6. Software Experiment

The first experimental implementation will model a single LIF neuron in Python.

The experiment will investigate:

1. Input spike/current patterns
2. Membrane potential evolution
3. Threshold detection
4. Output spike generation
5. Membrane potential reset

The Python implementation will serve as the reference model for subsequent hardware implementation.

---

## 7. Hardware Mapping

The software LIF neuron will eventually be mapped to digital hardware.

A possible FPGA implementation consists of:

```text
Input Spike
     │
     ▼
Input Accumulator
     │
     ▼
Membrane Potential Register
     │
     ▼
Leak / Update Logic
     │
     ▼
Threshold Comparator
     │
     ├──── No Spike
     │
     └──── Spike
             │
             ▼
          Reset Logic
```

Potential FPGA resources include:

* Registers
* Adders/subtractors
* Comparators
* Multiplexers
* Control logic

---

## 8. Initial Research Question

The broader research question is:

> How can an FPGA-based SNN architecture be implemented and optimized to reduce hardware resource utilization and energy consumption while maintaining acceptable inference accuracy?

The LIF neuron experiment represents the first step toward answering this question.

---

## 9. Planned Evaluation Metrics

The eventual FPGA implementation will be evaluated using:

| Metric     | Purpose                         |
| ---------- | ------------------------------- |
| LUTs       | FPGA logic utilization          |
| Flip-Flops | Sequential resource utilization |
| BRAM       | Memory requirements             |
| DSP        | Arithmetic resource utilization |
| Frequency  | Maximum operating speed         |
| Latency    | Inference time                  |
| Power      | Hardware power consumption      |
| Energy     | Energy required for computation |
| Accuracy   | SNN inference performance       |

---

## 10. Next Experiment

The next experiment will investigate **spike encoding** and determine how conventional numerical input data can be converted into spike trains suitable for an SNN.

After spike encoding, the project will progress from:

**Single LIF neuron → multiple neurons → SNN → SNN inference → Verilog implementation → FPGA evaluation.**

---

## References

1. J. S. Friedman, NeuroSpinCompute Laboratory, The University of Texas at Dallas.
   https://personal.utdallas.edu/~joseph.friedman/

2. J. S. Friedman, "Neuromorphic Computing with Magnetic Domain Walls," NeuroSpinCompute Laboratory, The University of Texas at Dallas.

3. A. J. Edwards et al., "Harnessing Stochasticity for Superconductive Multi-Layer Spike-Rate-Coded Neuromorphic Networks," *Neuromorphic Computing and Engineering*, 2024.

4. P. Zhou et al., "Neuromorphic Hebbian Learning with Magnetic Tunnel Junction Synapses," *Communications Engineering*, 2025.

