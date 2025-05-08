import pandas as pd
import numpy as np

num_patients = 2000
min_len = 5
max_len = 15
feature_a_mean = 50
feature_a_std = 10
feature_b_mean = 20
feature_b_std = 5
num_categories_c = 5

np.random.seed(42)

all_patient_data = []

for patient_id in range(num_patients):
    seq_len = np.random.randint(min_len, max_len + 1)
    patient_df = pd.DataFrame({
        'patient_id': patient_id,
        'time_step': np.arange(seq_len),
        'feature_A': np.random.normal(feature_a_mean, feature_a_std, size=seq_len),
        'feature_B': np.random.normal(feature_b_mean, feature_b_std, size=seq_len),
        'feature_C': np.random.randint(1, num_categories_c + 1, size=seq_len)
    })

    final_a = patient_df['feature_A'].iloc[-1]
    final_c = patient_df['feature_C'].iloc[-1]
    prob_outcome_1 = 0.1

    if final_a > (feature_a_mean + feature_a_std * 0.5): 
         prob_outcome_1 += 0.3
    if final_c == num_categories_c: 
         prob_outcome_1 += 0.2

    prob_outcome_1 += np.random.uniform(-0.15, 0.15)
    prob_outcome_1 = np.clip(prob_outcome_1, 0.05, 0.95)

    outcome = 1 if np.random.rand() < prob_outcome_1 else 0
    patient_df['outcome'] = outcome

    all_patient_data.append(patient_df)

final_df = pd.concat(all_patient_data, ignore_index=True)

output_filename = 'synthetic_ehr_data.csv'
final_df.to_csv(output_filename, index=False)

print(f"Generated synthetic data for {num_patients} patients.")
print(f"Total records: {len(final_df)}")
print(f"Saved data to {output_filename}")
print("\nFirst few rows:")
print(final_df.head())
print("\nData description:")
print(final_df.describe())
print("\nOutcome distribution:")
print(final_df.groupby('patient_id')['outcome'].first().value_counts(normalize=True))
