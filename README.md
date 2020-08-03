# spec2vec_gnps_data_analysis

Analysis of mass spectra in GC/MS samples using spec2vec and matchms repositories

## To test first download Spec2vec and matchms repos

    conda env create --file conda/environment-dev.yml
    conda activate gcms-analysis
    cd ../path_to/matchms
    python setup.py install
    cd ../path_to/spec2vec_gcms_data_analysis
    jupyter notebook
    