FROM dromni/nerfstudio:1.1.4

# Solution from https://github.com/nerfstudio-project/nerfstudio/issues/2929
RUN sudo rm -rf /usr/lib/x86_64-linux-gnu/libcuda.so.1 \
    /usr/lib/x86_64-linux-gnu/libnvidia-*.so.1 \
    /usr/lib/x86_64-linux-gnu/libnvcuvid.so.1 \
    /usr/lib/x86_64-linux-gnu/libcudadebugger.so.1

USER root
RUN git clone https://github.com/nerfstudio-project/gsplat.git 
RUN pip install -r ./gsplat/examples/requirements.txt

RUN pip install torch==2.1.2

RUN pip install git+https://github.com/nerfstudio-project/gsplat.git

# Set the default shell to bash
SHELL ["/bin/bash", "-c"]

# Set the entrypoint to bash
ENTRYPOINT ["/bin/bash"]