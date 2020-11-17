FROM mlfcore/base:1.0.0

# Install the conda environment
COPY environment.yml .
RUN conda env create -f environment.yml && conda clean -a

# Activate the environment
RUN echo "source activate mlfcore_test" >> ~/.bashrc
ENV PATH /home/user/miniconda/envs/mlfcore-test/bin:$PATH

# Dump the details of the installed packages to a file for posterity
RUN conda env export --name mlfcore-test > mlfcore-test_environment.yml

# Currently required, since mlflow writes every file as root!
USER root
