# How to run Nerfstudio using Docker

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

    Lookup the correct `CUDA_ARCHITECTURES` value to use for your GPU [here](https://docs.nerf.studio/quickstart/installation.html).

    ```
    docker build --build-arg CUDA_ARCHITECTURES=86 -t nerfstudio .
    ```

4. Run the docker container and mount to your project directory

    ```
    docker run --gpus all -w /working -v <workspace directory>:/working/ -v<caching dir>:/home/user/.cache/ -p 7007:7007 -it --shm-size=12gb nerfstudio:latest
    ```


## Preprocess 360-degree images for COLMAP alignment and Gaussian Splatting training

See [this](https://docs.nerf.studio/quickstart/custom_dataset.html#data-equirectangular) for more info

```bash
ns-process-data images --camera-type equirectangular --images-per-equirect 14 --crop-factor 0 0.2 0 0 --data {data directory} --output-dir {output directory}
```

ns-process-data images --camera-type equirectangular --images-per-equirect 14 --crop-factor 0 0.2 0 0 --data ./spherical_images --output-dir ./planar_images