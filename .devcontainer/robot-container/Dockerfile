FROM humble:dev

# ** [Optional] Uncomment this section to install additional packages. **
#
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
   && apt-get -y install --no-install-recommends \
    tmux \
    tmuxp \
    iputils-ping \
    net-tools \
    && apt-get autoremove -y \
   && apt-get clean -y \
   && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=dialog

COPY .devcontainer/.tmux.conf /etc/tmux.conf

COPY .devcontainer/zenoh-bridge-ros2dds_0.11.0_amd64.deb /tmp
RUN dpkg -i /tmp/zenoh-bridge-ros2dds_0.11.0_amd64.deb