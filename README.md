# spec2vec_gnps_data_analysis

Analysis of mass spectra in GC/MS samples using spec2vec and matchms repositories

## To test first download Spec2vec and matchms repos

conda create --name gmcs_analysis python=3.7
conda activate gmcs_analysis
conda install --channel nlesc --channel bioconda --channel conda-forge spec2vec
conda install --channel nlesc --channel bioconda --channel conda-forge matchms