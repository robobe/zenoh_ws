FROM ubuntu:22.04

ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create a non-root user
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
  # Add sudo support for the non-root user
  && apt-get update \
  && apt-get install -y sudo \
  && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME\
  && chmod 0440 /etc/sudoers.d/$USERNAME \
  && rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
   && apt-get -y install --no-install-recommends \
      python3 \
      python3-pip \
      python3-venv \
      git \
      build-essential \
      curl \
      vim \
      wget \
      tmux \
      tmuxp \
      iputils-ping \
      net-tools \
   && apt-get autoremove -y \
   && apt-get clean -y \
   && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

COPY .devcontainer/.tmux.conf /etc/tmux.conf



COPY .devcontainer/client-container/requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt