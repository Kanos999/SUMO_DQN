import traci
import sumolib

sumobin = sumolib.checkBinary('sumo-gui')
environment = "environments/cross.sumocfg"

traci.start([sumobin, '-c', environment])

step = 0
while step < 1000:
    traci.simulationStep()
    step += 1

traci.close()