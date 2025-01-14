import simpy
import random


class AIProcess:
    def __init__(self, env, name, context):
        self.env = env
        self.name = name
        self.context = context  # Reference to the network for communication
        self.status = f"Initial status of {name}"
        self.action = env.process(self.run())

                 
class AIContext:
    def __init__(self, env, name, onwer):
        self.env = env
        self.name = name
        self.owner = owner  # Reference to the network for communication
        self.status = f"Initial status of {name}"
        self.action = env.process(self.run())


class MessageBrokerNode:
    def __init__(self, env, name, topic, context,  inputs[], outputs[]):
        
    
class MessageBrokerQueue:
    def __init__(self, env, name, topic, context,  inputs[], outputs[]):
        self.env = env
        self.name = name
        self.topic = context  # Reference to the network for communication
        self.inputs[] = inputs
        self.outputs[] = ouptuts
        self.status = f"Initial status of {name}"
        self.action = env.process(self.run())

    def queue_message(self, message ):

    def deque_message(self ):

