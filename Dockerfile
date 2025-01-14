FROM python:3.9-slim

# Install GCC and other build essentials
RUN apt-get update && apt-get install -y \
    gcc \
    make \
    cmake \
    git \
    openssh-client
    
#install sshd server
RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir /var/run/sshd

run apt-get install -y emacs-x11 x11-xserver xauth

# Configure SSH
RUN echo 'root:tester' | chpasswd  # Set root password
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Create a user and set a password
RUN useradd -m simuser && \
    echo "simuser:puddle" | chpasswd

EXPOSE 22
# Start the SSH service
CMD ["/usr/sbin/sshd", "-D"]

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

#Define the default command to run XEmacs
CMD ["xemacs"]