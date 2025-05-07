# Reproducing Model Uncertainty Analysis for EHRs

This project aims to reproduce the core conceptual findings of the paper "Analyzing The Role Of Model Uncertainty For Electronic Health Records" by Dusenberry et al. (2020), specifically focusing on how population-level metrics can obscure significant patient-specific model uncertainty. This reproduction uses synthetically generated sequential Electronic Health Record (EHR) data and implements a Deep Ensemble of LSTM-based models.

**Original Paper:**
Dusenberry, M. W., Tran, D., Choi, E., Kemp, J., Nixon, J., Jerfel, G., ... & Dai, A. M. (2020). Analyzing the role of model uncertainty for electronic health records. *ACM Conference on Health, Inference, and Learning (CHIL)*. (Consider adding a direct link to the paper if available, e.g., on ACM DL or arXiv).

**Author:** [Your Name/GitHub Username]
**Repository URL:** [Link to Your GitHub Repo URL Once Created]

## Overview

This project demonstrates that even with good overall model performance (e.g., AUC-ROC), individual predictions can have high uncertainty. This is shown using:
1.  A Deep Ensemble of LSTM models trained on synthetic EHR data.
2.  An extension using Monte Carlo (MC) Dropout for uncertainty estimation.

The code is organized into Jupyter Notebooks for data generation, model training, evaluation, and the extension.

## Repository Structure
