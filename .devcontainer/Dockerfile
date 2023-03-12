FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

ENV LANG C.UTF-8

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        git \
        python3 \
        python3-pip

COPY requirements.txt .
RUN python3 -m pip --no-cache-dir install --upgrade -r requirements.txt

RUN ldconfig && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* ~/*