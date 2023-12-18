FROM nvidia/cuda:11.6.2-devel-ubuntu20.04

# master | develop
ARG OPENMVS_GIT_COMMIT=master 

# Prevent stop building ubuntu at time zone selection.  
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -yq && apt-get -yq install \
    build-essential \
    git \
    cmake \
    libpng-dev \
    libjpeg-dev \
    libtiff-dev \
    libglu1-mesa-dev \
    libglew-dev \
    libglfw3-dev

# Build and install dependencies

# Eigen
RUN git clone https://gitlab.com/libeigen/eigen --branch 3.4 && \
    mkdir eigen_build && \
    cd eigen_build && \ 
    cmake . ../eigen -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda/ && \
    make && make install && \
    cd .. && rm -rf eigen_build eigen

# Boost
RUN apt-get -y install \
    libboost-iostreams-dev \
    libboost-program-options-dev \
    libboost-system-dev \
    libboost-serialization-dev


# OpenCV
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get install -yq libopencv-dev

# CGAL
RUN apt-get -yq install \
    libcgal-dev \
    libcgal-qt5-dev

# VCGLib
RUN git clone https://github.com/cdcseacave/VCG.git vcglib

# Build and install openMVS
RUN git clone https://github.com/cdcseacave/openMVS.git --branch ${OPENMVS_GIT_COMMIT} && \
    mkdir openMVS_build && \
    cd openMVS_build && \
    cmake . ../openMVS -DCMAKE_BUILD_TYPE=Release -DVCG_ROOT=/vcglib -DOpenMVS_USE_CUDA=ON -DCMAKE_LIBRARY_PATH=/usr/local/cuda/lib64/stubs/ -DCUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda/ -DCUDA_INCLUDE_DIRS=/usr/local/cuda/include/ -DCUDA_CUDART_LIBRARY=/usr/local/cuda/lib64 -DCUDA_NVCC_EXECUTABLE=/usr/local/cuda/bin/ && \
    make -j4 && \
    make install && \
    cd .. && rm -rf openMVS_build vcglib

# Add binaries to path
ENV PATH /usr/local/bin/OpenMVS:$PATH

