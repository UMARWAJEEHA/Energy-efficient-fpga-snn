# Baseline LIF Neuron Results

## Experiment

A simple Leaky Integrate-and-Fire (LIF) neuron was evaluated using
a sequence of input currents.

### Parameters

- Threshold: 1.0
- Membrane decay: 0.9
- Arithmetic: Floating point
- Input: Synthetic current sequence

### Input

[0.3, 0.4, 0.5, 0.2, 0.7, 0.4, 0.6, 0.1]

### Metrics

The baseline records:

- Spike output
- Total spike count
- Membrane potential behavior

## Purpose

This experiment establishes a software reference model that can
later be compared with fixed-point and FPGA implementations.

## Planned Comparison

| Implementation | Precision | Spike Count | Accuracy | FPGA Resources | Energy |
|---|---|---:|---:|---:|---:|
| Floating-point baseline | FP | TBD | TBD | TBD | TBD |
| Fixed-point | 8-bit | TBD | TBD | TBD | TBD |
| Fixed-point | 6-bit | TBD | TBD | TBD | TBD |
| Fixed-point | 4-bit | TBD | TBD | TBD | TBD |

## Next Step

Implement a fixed-point LIF neuron and compare its behavior with
the floating-point baseline.
