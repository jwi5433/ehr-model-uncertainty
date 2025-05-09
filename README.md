# Reproducing Model Uncertainty Analysis for EHRs

This project aims to reproduce the core conceptual findings of the paper "Analyzing The Role Of Model Uncertainty For Electronic Health Records" by Dusenberry et al. (2020), specifically focusing on how population-level metrics can obscure significant patient-specific model uncertainty. This reproduction uses synthetically generated sequential Electronic Health Record (EHR) data and implements a Deep Ensemble of LSTM-based models.

**Original Paper:**
Dusenberry, M. W., Tran, D., Choi, E., Kemp, J., Nixon, J., Jerfel, G., ... & Dai, A. M. (2020). Analyzing the role of model uncertainty for electronic health records. *ACM Conference on Health, Inference, and Learning (CHIL)*. 
(Consider adding a direct link to the paper if available, e.g., on ACM DL or arXiv)

**Author:** John Williams (jwi5433)
**Repository URL:** https://github.com/jwi5433/ehr-model-uncertainty

## Overview

This project demonstrates that even with good overall model performance (e.g., AUC-ROC), individual predictions can have high uncertainty. This is shown using:
1.  A Deep Ensemble of LSTM models trained on synthetic EHR data.
2.  An extension using Monte Carlo (MC) Dropout for uncertainty estimation.

The data is generated by a Python script, and the modeling, evaluation, and extension are implemented in Jupyter Notebooks.

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/jwi5433/ehr-model-uncertainty.git
    cd ehr-model-uncertainty
    ```

2.  **Create and activate a Python virtual environment:**
    It is recommended to use Python 3.12 (as used in this project).

    **Create the virtual environment:**
    * **On macOS/Linux:**
        ```bash
        python3 -m venv pytorch_env
        ```
    * **On Windows:**
        ```bash
        py -m venv pytorch_env
        ```


    **Activate the virtual environment:**
    - On **Windows**:
      ```bash
      .\pytorch_env\Scripts\activate
      ```
    - On **macOS/Linux**:
      ```bash
      source pytorch_env/bin/activate
      ```
      
3.  **Install PyTorch, Torchvision, and Torchaudio:**
    Before installing other project dependencies, you need to install PyTorch tailored to your system.
    * Visit the official PyTorch website: [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)
    * On the website, select the correct options for your setup:
        * **PyTorch Build:** Stable (Recommended)
        * **Your OS:** (e.g., Linux, Mac, Windows)
        * **Package:** Pip
        * **Language:** Python
        * **Compute Platform:**
            * Choose a **CUDA version** if you have a compatible NVIDIA GPU and want GPU support (e.g., CUDA 12.1 or another version listed).
            * Choose **CPU** if you do not have an NVIDIA GPU or prefer to run on the CPU.
    * The website will generate a command. Copy this command and run it in your activated `pytorch_env` terminal.


4. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Launch Jupyter Lab:**
    The notebooks are designed to run in Jupyter Lab for better visualization.
    ```bash
    jupyter lab
    ```
    Open `notebooks/main_deep_ensemble.ipynb` to get started.

---

## Running the Code & Reproducing Results

The project consists of a data generation script and two Jupyter notebooks. Please run them in the specified order. Key outputs (metrics, plots) are displayed within the notebooks, and all generated plots are saved directly to the `plots/` directory.

**1. Data:**
   A pre-generated synthetic dataset, `synthetic_ehr_data.csv`, is included in the `data/` directory for immediate use with the notebooks.

   For completeness, the script used to generate this data, `generateData.py`, is also provided in the root of the repository. If you wish to regenerate the dataset yourself (which will overwrite the existing file in `data/`), run:
   ```bash
   python generateData.py
   ```
**2. Deep Ensemble Training and Evaluation (Main Assignment):**

   Execute the following notebook: `notebooks/main_deep_ensemble.ipynb`
   
   Running this notebook will:
   
    * Load `synthetic_ehr_data.csv` from the `data/` folder.
    * Preprocess the data.
    * Train the 20 LSTM models for the Deep Ensemble.
    * Save the trained model weights (`*.pth` files) to the `ensemble_models_pytorch/` directory.
    * Evaluate the Deep Ensemble, calculating and printing its AUC-ROC score (0.7186 reported in the paper).
    * Generate the Mean vs. Standard Deviation scatter plot for the ensemble (Figure 3 in the report) and save it to `plots/`.
    * Generate example per-patient prediction distribution histograms for the ensemble (Figure 4 in the report shows Patient Index 10; others are saved) and save them directly to the `plots/` directory.

   **Note:** This notebook trains the models from scratch. The saved models in `ensemble_models_pytorch/` are primarily for use by the MC Dropout notebook.

**3. MC Dropout Evaluation (Extension):**

   Execute the following notebook after `main_deep_ensemble.ipynb` has successfully run and saved the models: `notebooks/extension_mc_dropout.ipynb`
   
   Running this notebook will:
   
    * Load `synthetic_ehr_data.csv`.
    * Preprocess the data.
    * Load one pre-trained ensemble model (Model 0) from the `ensemble_models_pytorch/` directory.
    * Perform inference using MC Dropout (20 samples).
    * Calculate and print the AUC-ROC score for MC Dropout (0.7084 reported in the paper).
    * Generate the MC Dropout Mean vs. Standard Deviation scatter plot (Figure 6 in the report) and save it directly to the `plots/` directory.
    * Generate an example per-patient prediction distribution histogram using MC Dropout (Figure 5 in the report shows one patient; others are saved) and save it directly to the `plots/` directory.
## Key Results Summary

| Method         | AUC-ROC |
|----------------|---------|
| Deep Ensemble  | 0.7186  |
| MC Dropout     | 0.7084  |


## Hardware & Software Notes

* **Python:** 3.12
* **Key Libraries:** PyTorch (2.7.0+cu128), Pandas (2.2.3), NumPy (2.1.2), Scikit-learn (1.6.1), Matplotlib (3.10.1). See `requirements.txt` for the full list.
* **Hardware:** Training was performed on an NVIDIA GeForce RTX 4090 (CUDA enabled). Evaluation can run on CPU, but training from scratch may be slow without a GPU. Pre-trained models are provided in the `ensemble_models_pytorch/` folder.
