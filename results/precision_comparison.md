# Floating-Point vs 8-bit Fixed-Point LIF

## Experiment

A floating-point LIF neuron was compared with an 8-bit fixed-point
implementation using the same input sequence and neuron parameters.

## Parameters

- Threshold: 1.0
- Decay: 0.9
- Input sequence: `[0.3, 0.4, 0.5, 0.2, 0.7, 0.4, 0.6, 0.1]`

## Results

| Metric | Floating Point | 8-bit Fixed Point |

|---|---:|---:|
| Spike count | **Floating-point spikes: [0, 0, 1, 0, 0, 1, 0, 0]
8-bit fixed-point:     [0, 0, 1, 0, 0, 1, 0, 0]** | **Floating-point spike count: 2
8-bit spike count:         2** |
| Output agreement | — | **PASTE ACTUAL 100.0%** |

## Observation

The 8-bit fixed-point implementation was compared with the
floating-point reference to determine whether reduced numerical
precision preserves the baseline spike behavior.

## Reproducibility

The experiment can be reproduced using:

`software/compare_lif_precision.py`

The experiment is automatically executed through GitHub Actions.

## Next Step

Evaluate lower precision using a 6-bit fixed-point LIF
implementation and compare its spike behavior with the baseline.
