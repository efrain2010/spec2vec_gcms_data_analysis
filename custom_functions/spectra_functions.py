from matchms import Spikes
from matchms import Spectrum
import numpy as np
import random


def group_by_inchikey(spectrums):
    grouped_spectrum = []
    inchikeys = []
    for s in spectrums:
        inchikey = s.metadata.get('inchikey').split('-', 1)[0]
        if inchikey not in inchikeys:
            inchikeys.append(inchikey)
            grouped_spectrum.append([s]) 
        else:
            index = inchikeys.index(inchikey)
            grouped_spectrum[index].append(s)
    return grouped_spectrum

def grouped_by_same_mol(spectrums):
    group_spectra_same_molecule = random.sample([k for k in group_by_inchikey(spectrums) if len(k) == 2], 1000)
    return group_spectra_same_molecule

def grouped_by_diff_mol(spectrums):
    group_spectra_diff_molecule = [[g[0]] for g in grouped_by_same_mol(spectrums)]

    for k, e in enumerate(group_spectra_diff_molecule):
        diff_mol = random.sample(spectrums, 1)
        while e[0].metadata['inchikey'].split('-', 1)[0] == diff_mol[0].metadata['inchikey'].split('-', 1)[0]:
            diff_mol = random.sample(spectrums, 1)
        group_spectra_diff_molecule[k].append(diff_mol[0])
    
    return group_spectra_diff_molecule
    

def apply_powers(spectrum: Spectrum, c: float = 1.0, d: float = 1.0):
    spikes = spectrum.peaks.clone()
    mz = [m*c for m in spikes[0]]
    intensities = [m*c for m in spikes[1]]
    spikes = Spikes(mz=np.array(mz), intensities=np.array(intensities))
    spectrum.peaks = spikes
    return spectrum
    