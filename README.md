# Microbial Abundance Visualization for BV Recurrence Types
This project visualizes the relative abundance of specific OTUs (Operational Taxonomic Units) over various follow-ups for HIV positive women with Bacterial Vaginosis (BV), based on sequencing data. The code plots the relative abundance of patients labeled with a recurrence type of **No Initial Response**, **Immediate Recurrence**, and **Delayed Recurrence** and a patient who had successful response to antibiotic treatments.

## Dataset
Here we use an edited dataset composed of subject diagnostic information and vaginal microbiota of 132 HIV positive Tanzanian women (including 39 who received metronidazole treatment for BV) with added columns for BV status and Recurrence Type. A BV status of 1 indicates positive and 0 indicated negative for BV based on a nugent score of 7 or greater. The recurrence types are defined as 
- **No Initial Response**: BV positive for all follow-ups,
- **Immediate Recurrence**: BV positive after one negative follow-up,
- **Delayed Recurrence**: BV positive after two or more negative follow-ups,

No recurrence is labeled as
- **Successful Response**: BV negative for all follow-ups after first visit.

## Project Files
diagnosis_data.csv -- Edited dataset from Hummelen et al. (2010) containing initial and follow-up tests (Amsel score, Nugent score, pH, OTUs, etc.) with added features BV status and Recurrence Type as desribed above. 

classification.csv -- Original taxonomical classification for identified OTUs from Hummelen et al. (2010). 

expected_result.png -- Expected graphs created from running re_fig.py. 

## Packages 
pandas version: 2.2.2
matplotlib version: 3.10.0

## Installation 
You can run the script from the terminal by following the steps below. 
1. Create and name folder in a directory of your choice (ie. Downloads > tutorial)
2. Download diagnosis_data.csv, classification.csv, and re_fig.py and store in the folder created in step 1.
3. Open terminal and navigate into the folder created in step 1, which should have the files from step 2. (ie. cd Downloads/tutorial)
4. Enter in the command line: python3 re_fig.py
5. Compare to expected output file.
   


##Dataset Source
Hummelen, R., Fernandes, A. D., Macklaim, J. M., Dickson, R. J., Changalucha, J., Gloor, G. B., & Reid, G. (2010). Deep Sequencing of the Vaginal Microbiota of Women with HIV. PLOS ONE, 5(8), e12078. https://doi.org/10.1371/journal.pone.0012078 



