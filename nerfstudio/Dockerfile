FROM dromni/nerfstudio:1.1.3

# Solution from https://github.com/nerfstudio-project/nerfstudio/issues/2929
RUN sudo rm -rf /usr/lib/x86_64-linux-gnu/libcuda.so.1 \
    /usr/lib/x86_64-linux-gnu/libnvidia-*.so.1 \
    /usr/lib/x86_64-linux-gnu/libnvcuvid.so.1 \
    /usr/lib/x86_64-linux-gnu/libcudadebugger.so.1

SHELL ["/bin/bash"]