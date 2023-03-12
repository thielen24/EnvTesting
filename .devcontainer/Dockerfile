FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

ENV NVIDIA_DRIVER_CAPABILITIES="compute,video,utility"

ENV LANG C.UTF-8
RUN apt-get update

# ==================================================================
# tools
# ------------------------------------------------------------------
RUN apt-get install -y --no-install-recommends \
        git

# ==================================================================
# python
# ------------------------------------------------------------------
RUN apt-get install -y --no-install-recommends \
        python3 \
        python3-pip

RUN python3 -m pip --no-cache-dir install --upgrade \
        numpy \
        scipy \
        pandas \
        scikit-image \
        scikit-learn \
        matplotlib \
        Cython \
        tqdm \
        jupyter \
        notebook \
        pytest

# ==================================================================
# pytorch
# ------------------------------------------------------------------

RUN python3 -m pip --no-cache-dir install --upgrade \
        future \
        numpy \
        protobuf \
        enum34 \
        pyyaml \
        typing
RUN python3 -m pip --no-cache-dir install --upgrade \
        --pre torch torchvision torchaudio -f \
        https://download.pytorch.org/whl/nightly/cu117/torch_nightly.html

# ==================================================================
# config & cleanup
# ------------------------------------------------------------------

RUN ldconfig && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* ~/*