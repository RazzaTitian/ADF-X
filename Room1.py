import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE

def Room1(OldData_Room1, num_samples=1000, noise_level=0.01, target_column='target_column'):
    # Perform Simple Random Sampling (SRS)
    SRS_Room1 = OldData_Room1.sample(n=num_samples, replace=True, random_state=1)

    # Perform SMOTE
    smote = SMOTE(sampling_strategy='auto')
    X, y = SRS_Room1.drop(target_column, axis=1), SRS_Room1[target_column]
    X_resampled, y_resampled = smote.fit_resample(X, y)
    SMOTE_Room1 = pd.concat([X_resampled, y_resampled], axis=1)

    # Perform Data Perturbation (DP)
    def perturb_data(data, noise_lvl):
        perturbed_data = data.copy()
        for column in perturbed_data.select_dtypes(include=[np.number]).columns:
            std = perturbed_data[column].std()
            noise = np.random.normal(0, std * noise_lvl, size=perturbed_data[column].shape)
            perturbed_data[column] += noise
        return perturbed_data

    # Apply Data Perturbation to the SMOTEd data
    perturbed_df = perturb_data(SMOTE_Room1, noise_level)

    # The perturbed_df is the final output of Room1
    return perturbed_df

# Example usage:
# Assuming 'OldData_Room1' is the DataFrame containing the old data for room 1
# Room1_output = Room1(OldData_Room1)
