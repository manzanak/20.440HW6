import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
from scipy.stats import spearmanr
import matplotlib.cm as cm
import operator

diagnosis_data = pd.read_csv('diagnosis_data.csv')
classification = pd.read_csv('classification.csv')

def plot_fraction_of_reads(subject_ids, otus):
    n = len(subject_ids)
    fig, axes = plt.subplots(n, 1, figsize=(12, 6 * n), sharex=False)

    if n == 1:
       axes = [axes]  # ensure axes is iterable for a single subplot

    for i, (ax, patient) in enumerate(zip(axes, subject_ids)):
       patient_data = diagnosis_data[(diagnosis_data['Subject_ID'] == patient)]

       for species in otus:
            total_reads = patient_data['total_reads'].astype(float)
            species_read = patient_data[species].astype(float)
            fraction = species_read / total_reads
            species_name = classification.loc[classification['#OTU'] == species.replace('otu', ''), 'Blast hit'].values[0]

            x_labels = patient_data['Follow-up'].astype(str) + "/" + patient_data['BV_status'].astype(str)
            ax.plot(x_labels, fraction, label=species_name)

       ax.set_title(f'Patient {patient}')
       ax.set_xlabel('Follow-up / BV Status')
       ax.set_ylabel('Mean Relative Abundance')
       ax.legend()
       ax.set_xticks(range(len(x_labels)))
       ax.set_xticklabels(x_labels, rotation=45)

    plt.tight_layout()
    plt.show()


subjects_ids = [20, 43, 53, 63]
no_initial_res_subject_IDs = diagnosis_data[diagnosis_data['Subject_ID'].isin(subjects_ids)]['Subject_ID'].unique()
plot_fraction_of_reads(no_initial_res_subject_IDs, ['otu0', 'otu4', 'otu1', 'otu2'])
