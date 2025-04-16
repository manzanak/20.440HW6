# Microbial Abundance Visualization for BV Recurrence Types
This project visualizes the relative abundance of specific OTUs (Operational Taxonomic Units) over time for patients with Bacterial Vaginosis (BV), based on sequencing data. It focuses on patients labeled with a recurrence type of **No Initial Response**, **Immediate Recurrence**, **Delayed Recurrence**, and **Successful Response**. 

## Dataset
Here we use an edited dataset composed of subject diagnostic information and vaginal microbiota of 132 HIV positive Tanzanian women (including 39 who received metronidazole treatment for BV) with added columns for BV status and Recurrence Type. Original dataset is accessible here.

## Project Files
diagnosis_data.csv -- Edited dataset from Hummelen et al. (2010) containing initial and follow-up tests (Amsel score, Nugent score, pH, OTUs, etc.) with added features BV status and Recurrence Type. 

classification.csv -- Taxonomical classification for identified OTUs from Hummelen et al. (2010)

## Installation 
You can run the script from the terminal by following the steps below. 
1. Create and name folder in a directory of your choice (ie. Downloads > tutorial)
2. Download diagnosis_data.csv, classification.csv, and re_fig.py and store in the folder created in step 1.
3. Open terminal and navigate into the folder created in step 1, which should have the files from step 2. (ie. cd Downloads/tutorial)
4. Enter in the command line: python3 re_fig.py




