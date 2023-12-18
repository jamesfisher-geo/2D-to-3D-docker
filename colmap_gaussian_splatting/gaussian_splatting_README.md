# How to build COLMAP and Gaussian Splatting using Docker

## Requirements

- Host machine with at least one NVIDIA GPU/CUDA support and installed drivers
  (to support dense reconstruction).
- Docker (for CUDA support 19.03+).

## Quick Start

1. Check that Docker >=19.03 installed on your host machine:

    ```
    docker --version
    ```

2. Check that you have an NVIDIA driver installed on your host machine:

    ```
    nvidia-smi
    ```

<!-- 3. Setup the nvidia-toolkit on your host machine:

    For Ubuntu host machines: `./setup-ubuntu.sh`

    For CentOS host machines: `./setup-centos.sh`

      *Find these in the COLMMAP repo** -->

3. Build the docker container

    ```
    docker build -t="colmap_gauss:latest" --build-arg CUDA_ARCHITECTURES=86 -f Dockerfile .
    ```

4. Run the docker container and mount to your project directory

    ```
    docker run --gpus all -w /working -v <workspace directory>:/working -it colmap_gauss:latest
    ```

    This will put you in a directory (inside the Docker container) mounted to
    the local path you specified. Now you can run COLMAP binaries and Gaussian Splatting scripts on your own.

    Make sure to activate the `gaussian_splatting` conda environment

    ```
    conda activate gaussian_splatting
    ```

    Create and train a Gaussian Splatting model from COLMAP matches features with the following:

    ```
    python ../gaussian-splatting/convert.py -s .
    ```
    **Note:** This will executy COLMAP porcesses to generate a sparse point cloud and undistort images. The images should be place in a subfolder named `input`
    ```
    python ../gaussian-splatting/train.py -s .
    ```

    enter `exit` to exit the docker container


## Troubleshooting

Install an NVIDIA driver and NVIDIA container runtime:

```
sudo apt install ubuntu-drivers-common
sudo ubuntu-drivers autoinstall
```

If you failed to install the above, check the appropriate NVIDIA driver by yourself and install it:

```
ubuntu-drivers devices
e.g.
sudo apt install nvidia-driver-455
```
