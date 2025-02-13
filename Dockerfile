FROM debian:latest

RUN apt-get update && apt-get install -y --no-install-recommends build-essential curl libfreetype6-dev libhdf5-dev libpng-dev libzmq3-dev pkg-config python3-dev rsync unzip zlib1g-dev zip libjpeg8-dev hdf5-tools libhdf5-serial-dev python3-pip python3-setuptools
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa && apt update
RUN apt-get update && apt-get -y --no-install-recommends install \
    sudo \
    wget \
    build-essential \
    pkg-config \
    python3.8 \
    python3.8-dev \
    python3.8-venv \
    python-dev \
    python3-dev \
RUN apt-get update && apt install --reinstall python3-apt -y
RUN pip3 install --upgrade pip
RUN apt-get update && apt -y --no-install-recommends install \
    git \
    cmake \
    autoconf \
    automake \
    libtool \
    gstreamer-1.0 \
    gstreamer1.0-dev \
    libgstreamer1.0-0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    gstreamer1.0-doc \
    gstreamer1.0-tools \
    gstreamer1.0-x \
    gstreamer1.0-alsa \
    gstreamer1.0-gl \
    gstreamer1.0-gtk3 \
    gstreamer1.0-qt5 \
    gstreamer1.0-pulseaudio \
    python-gst-1.0 \
    libgirepository1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    libcairo2-dev \
    gir1.2-gstreamer-1.0 \
    python3-gi \
    python-gi-dev \
    python3-setuptools \
    ffmpeg
RUN apt-get clean && \
        rm -rf /var/lib/apt/lists/*
RUN pip3 install -U pip -v

RUN pip install --no-cache-dir -r requirements.txt

LABEL authors="kevintf"

ENTRYPOINT ["top", "-b"]