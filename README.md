# Reproducing Model Uncertainty Analysis for EHRs

This project aims to reproduce the core conceptual findings of the paper "Analyzing The Role Of Model Uncertainty For Electronic Health Records" by Dusenberry et al. (2020), specifically focusing on how population-level metrics can obscure significant patient-specific model uncertainty. This reproduction uses synthetically generated sequential Electronic Health Record (EHR) data and implements a Deep Ensemble of LSTM-based models.

**Original Paper:**
Dusenberry, M. W., Tran, D., Choi, E., Kemp, J., Nixon, J., Jerfel, G., ... & Dai, A. M. (2020). Analyzing the role of model uncertainty for electronic health records. *ACM Conference on Health, Inference, and Learning (CHIL)*. (Consider adding a direct link to the paper if available, e.g., on ACM DL or arXiv).

**Author:** John Williams/johnw13


## Overview

This project demonstrates that even with good overall model performance (e.g., AUC-ROC), individual predictions can have high uncertainty. This is shown using:
1.  A Deep Ensemble of LSTM models trained on synthetic EHR data.
2.  An extension using Monte Carlo (MC) Dropout for uncertainty estimation.

The code is organized into Jupyter Notebooks for data generation, model training, evaluation, and the extension.

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone [Link to Your GitHub Repo URL Once Created]
    cd ehr-model-uncertainty-reproduction
    ```

2.  **Create and activate a Python virtual environment:**
    It is recommended to use Python 3.12 (as used in this project).
    ```bash
    python -m venv pytorch_env 
    # On Windows
    .\pytorch_env\Scripts\activate
    # On macOS/Linux
    # source pytorch_env/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Code & Reproducing Results

The project is implemented in Jupyter Notebooks located in the `notebooks/` folder. Please run them in the specified order. Key outputs (metrics, plots) are displayed in the notebooks and plots are also saved to the `plots/` directory.

**1. Data:**
   The synthetic dataset (`synthetic_ehr_data.csv`) is pre-generated and included in the `data/` directory.
   If you wish to regenerate it, run the `notebooks/01_data_generation.ipynb` notebook. This will overwrite the existing file. This notebook also generates the `sequence_length_distribution.png` plot (Figure 1 in the report).

**2. Deep Ensemble Training & Evaluation:**

   * **Training (Optional - Pre-trained models provided):**
        To train the Deep Ensemble models from scratch, run:
        `notebooks/02_model_training_deep_ensemble.ipynb`
        This will train 20 LSTM models and save their weights to the `trained_models/` directory, overwriting any existing models.
        *Seed:* A random seed (42) is used for NumPy and PyTorch operations within the notebook to promote reproducibility of training.

   * **Evaluation (Loads Pre-trained Models by Default):**
        To evaluate the Deep Ensemble using the provided pre-trained models and generate the main results, run:
        `notebooks/03_evaluation_deep_ensemble.ipynb`
        This notebook loads the 20 pre-trained models from the `trained_models/` directory, calculates the ensemble's AUC-ROC, and generates:
        * The Mean vs. Standard Deviation scatter plot (Figure 3 in the report).
        * Example per-patient prediction distribution histograms (Figure 4 in the report shows Patient Index 10; 5 such histograms are generated and saved for different patients).

**3. MC Dropout Extension:**

   * To run the MC Dropout extension (which uses Model 0 from the pre-trained Deep Ensemble), execute:
        `notebooks/04_extension_mc_dropout.ipynb`
        This notebook calculates the AUC-ROC for MC Dropout and generates:
        * The MC Dropout Mean vs. Standard Deviation scatter plot (Figure 6 in the report, assuming Figure 5 is the MC Dropout patient histogram).
        * An example per-patient prediction distribution histogram using MC Dropout (Figure 5 in the report).

## Key Results Summary

| Method          | AUC-ROC |
|-----------------|---------|
| Deep Ensemble   | 0.7186  |
| MC Dropout      | 0.7084  |

These results are printed in the output of `notebooks/03_evaluation_deep_ensemble.ipynb` and `notebooks/04_extension_mc_dropout.ipynb` respectively.

## Hardware & Software Notes
* **Python:** 3.12
* **Key Libraries:** PyTorch (2.7.0+cu128), Pandas (2.2.3), NumPy (2.1.2), Scikit-learn (1.6.1), Matplotlib (3.10.1). See `requirements.txt` for the full list.
* **Hardware:** Training and evaluation were performed on an NVIDIA GeForce RTX 4090 (CUDA enabled). While a GPU speeds up training, the provided pre-trained models allow evaluation on CPU. Training from scratch on a CPU will be significantly slower.

---
