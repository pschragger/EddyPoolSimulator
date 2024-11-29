import pysim
from pysim.simulation import Sim
from pysim.systems import VanDerPol
import matplotlib.pyplot as plt

# Create a Simulation object

sim = Sim()
# Create and set up a system

sys = VanDerPol()
sys.store("x")

# Add the system to the simulation

sim.add_system(sys)

# Run the simulation
sim.simulate(20, 0.1)
# Plot the results
x = sys.res.x
plt.plot(x)
plt.show()
