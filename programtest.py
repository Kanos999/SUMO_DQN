import traci
import sumolib

environment = "environments/cross.sumocfg"
sumobin = sumolib.checkBinary('sumo-gui')

traci.start([sumobin, '-c', environment, '--start'])  

print("Connected to TraCI")

traffic_light_ids = traci.trafficlight.getIDList()
for tid in traffic_light_ids:
    traci.trafficlight.setProgram(tid, "0")
    # traci.trafficlight.setRedYellowGreenState(tid, "gggggggggggg")

step = 0
while step < 1000:
    traci.simulationStep()
    step += 1

traci.load(['-c', environment, '--start'])

print("Connected to TraCI")

traffic_light_ids = traci.trafficlight.getIDList()
for tid in traffic_light_ids:
    traci.trafficlight.setProgram(tid, "0")
    # traci.trafficlight.setRedYellowGreenState(tid, "gggggggggggg")

step = 0
while step < 1000:
    traci.simulationStep()
    step += 1

traci.close()

# program 0 is in environments/cross/cross.net.xml 161-170

#<tlLogic id="0" type="static" programID="0" offset="0">
#    <phase duration="33" state="GGgrrrGGgrrr"/>
#    <phase duration="3"  state="yygrrryygrrr"/>
#    <phase duration="6"  state="rrGrrrrrGrrr"/>
#    <phase duration="3"  state="rryrrrrryrrr"/>
#    <phase duration="33" state="rrrGGgrrrGGg"/>
#    <phase duration="3"  state="rrryygrrryyg"/>
#    <phase duration="6"  state="rrrrrGrrrrrG"/>
#    <phase duration="3"  state="rrrrryrrrrry"/>
#</tlLogic>
