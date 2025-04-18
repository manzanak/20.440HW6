# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
diagnosis_data = pd.read_csv('diagnosis_data.csv')
classification = pd.read_csv('classification.csv')

def plot_fraction_of_reads(subject_ids, otus):
    """
    Plots the fraction of reads for each OTU for the specified subjects.

    Args: 
	subject_ids: A list of subject IDs to plot. 
	otus: A list of OTU names to plot.
    """

    n = len(subject_ids)
    fig, axes = plt.subplots(n, 1, figsize=(12, 6 * n), sharex=False) # Create subplots

    if n == 1:
       axes = [axes]  # Ensure axes is iterable for a single subplot
    
    # Iterate over subjects and OTUs
    for i, (ax, patient) in enumerate(zip(axes, subject_ids)):
       patient_data = diagnosis_data[(diagnosis_data['Subject_ID'] == patient)] # Filter data for current patient

       for species in otus:
            total_reads = patient_data['total_reads'].astype(float) # Get total reads
            species_read = patient_data[species].astype(float) # Get reads for current species
            fraction = species_read / total_reads # Calculate fraction of reads
            species_name = classification.loc[classification['#OTU'] == species.replace('otu', ''), 'Blast hit'].values[0] # Get species name

            x_labels = patient_data['Follow-up'].astype(str) + "/" + patient_data['BV_status'].astype(str) # Plot the data
            ax.plot(x_labels, fraction, label=species_name)
       
       # Set plot labels and title
       ax.set_title(f'Patient {patient}')
       ax.set_xlabel('Follow-up / BV Status')
       ax.set_ylabel('Mean Relative Abundance')
       ax.legend()
       ax.set_xticks(range(len(x_labels)))
       ax.set_xticklabels(x_labels, rotation=45)

    plt.tight_layout() # Adjust layout
    plt.show() # Display the plot

# Select subject IDs
subjects_ids = [20, 43, 53, 63]

# Get unique subject IDs from the selected subjects
no_initial_res_subject_IDs = diagnosis_data[diagnosis_data['Subject_ID'].isin(subjects_ids)]['Subject_ID'].unique()

# Plot the data
plot_fraction_of_reads(no_initial_res_subject_IDs, ['otu0', 'otu4', 'otu1', 'otu2'])
