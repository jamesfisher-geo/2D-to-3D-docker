FROM nvidia/cuda:11.6.2-devel-ubuntu20.04

ARG COLMAP_GIT_COMMIT=3.10
ARG GAUSS_SPLAT_GIT_COMMIT=main
ARG CUDA_ARCHITECTURES=86
ENV QT_XCB_GL_INTEGRATION=xcb_egl

# Prevent stop building ubuntu at time zone selection.  
ENV DEBIAN_FRONTEND=noninteractive

# Prepare and empty machine for building.
RUN apt-get update && apt-get install -y \
    git \
    cmake \
    ninja-build \
    build-essential \
    libboost-program-options-dev \
    libboost-filesystem-dev \
    libboost-graph-dev \
    libboost-system-dev \
    libeigen3-dev \
    libflann-dev \
    libfreeimage-dev \
    libmetis-dev \
    libgoogle-glog-dev \
    libgtest-dev \
    libsqlite3-dev \
    libglew-dev \
    qtbase5-dev \
    libqt5opengl5-dev \
    libcgal-dev \
    libceres-dev \
    wget \
    unzip \
    libgl-dev \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

# Build and install COLMAP.
RUN git clone https://github.com/colmap/colmap.git
RUN cd colmap && \
    git fetch https://github.com/colmap/colmap.git ${COLMAP_GIT_COMMIT} && \
    git checkout FETCH_HEAD && \
    mkdir build && \
    cd build && \
    cmake .. -GNinja -DCMAKE_CUDA_ARCHITECTURES=${CUDA_ARCHITECTURES} && \
    ninja && \
    ninja install && \
    cd .. && rm -rf colmap

# Install guassian-splatting and create a conda environment
RUN git clone https://github.com/graphdeco-inria/gaussian-splatting --recursive --branch ${GAUSS_SPLAT_GIT_COMMIT}

WORKDIR /gaussian-splatting

ENV TORCH_CUDA_ARCH_LIST="3.5;5.0;6.0;6.1;7.0;7.5;8.0;8.6+PTX"

RUN conda update -n base conda
RUN conda install -n base conda-libmamba-solver
RUN conda config --set solver libmamba
RUN conda env create -f environment.yml
RUN conda init bash
#RUN echo "conda activate gaussian_splatting" >> ~/.bashrc
SHELL ["conda", "run", "-n", "gaussian_splatting", "/bin/bash", "-c"]

WORKDIR /
