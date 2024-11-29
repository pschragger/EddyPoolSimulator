import simpy
import networkx as nx
import random

# Define message passing delay constants
LAN_DELAY = 1  # LAN delay in milliseconds
WAN_DELAY = 5  # WAN delay in milliseconds
SIM_TIME = 50  # Total simulation time

class SoftwareObject:
    def __init__(self, env, name, network):
        self.env = env
        self.name = name
        self.network = network  # Reference to the network for communication
        self.status = f"Initial status of {name}"
        self.action = env.process(self.run())

    def send_message(self, target, message, network_type):
        """Send a message to another software object via a specified network."""
        delay = self.network.get_delay(network_type)
        yield self.env.timeout(delay)
        print(f"{self.env.now}: {self.name} sent message to {target.name} via {network_type} - '{message}'")
        self.network.deliver_message(target, message)

    def receive_message(self, message):
        """Handle received messages."""
        print(f"{self.env.now}: {self.name} received message - '{message}'")
        self.status = f"Updated at {self.env.now}"

    def run(self):
        """Simulate behavior of the software object."""
        while True:
            # Send a status update to others
            for obj in self.network.objects:
                if obj != self:
                    network_type = "LAN" if random.random() > 0.5 else "WAN"
                    message = f"Status from {self.name}"
                    self.env.process(self.send_message(obj, message, network_type))
            yield self.env.timeout(10)  # Wait some time before next update


class Network:
    def __init__(self, env):
        self.env = env
        self.objects = []

    def add_object(self, obj):
        """Register a software object in the network."""
        self.objects.append(obj)

    def get_delay(self, network_type):
        """Return delay based on the network type."""
        if network_type == "LAN":
            return random.uniform(LAN_DELAY, LAN_DELAY * 1.5)
        elif network_type == "WAN":
            return random.uniform(WAN_DELAY, WAN_DELAY * 1.5)

    def deliver_message(self, target, message):
        """Deliver a message to the target software object."""
        self.env.process(target.receive_message(message))


    
    def run(self):
        """Process the message queue."""
        while True:
            if self.message_queue:
                # Process the first message in the queue
                target, message, timestamp = self.message_queue.pop(0)
                yield self.env.timeout(1)  # Simulate network processing time
                target.receive_message(message)
                print(f"{self.env.now}: Delivered message to {target.name} - '{message}'")
            else:
                # If no messages, yield for a small time to prevent busy waiting
                yield self.env.timeout(0.1)
        
# Simulation setup
env = simpy.Environment()
network = Network(env)

# Create software objects and add them to the network
obj_A = SoftwareObject(env, "A", network)
obj_B = SoftwareObject(env, "B", network)
obj_C = SoftwareObject(env, "C", network)

network.add_object(obj_A)
network.add_object(obj_B)
network.add_object(obj_C)

# Run the simulation
env.run(until=SIM_TIME)
