FROM python:3.9-slim

# Install GCC and other build essentials
RUN apt-get update && apt-get install -y \
    gcc \
    make \
    cmake \
    git \
    openssh-client

# Install PySim and Cython
RUN pip install numpy cython pysim

# Set the working directory in the container
WORKDIR /app

# Copy SSH keys to the container
# Note: This is not secure for production use
# For secure use, consider Docker secrets or other secure methods
COPY ./.ssh/id_ed25519 /root/.ssh/id_ed25519
COPY ./.ssh/id_ed25519.pub /root/.ssh/id_ed25519.pub

# Set permissions for the SSH keys
RUN chmod 600 /root/.ssh/id_ed25519
RUN chmod 600 /root/.ssh/id_ed25519.pub
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

# Clone the Git repository
RUN git clone git@github.com:pschragger/EddyPoolSimulator.git

# Define the default command to run when the container starts
RUN bash