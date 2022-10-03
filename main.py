from psychopy import gui
from cardioception.HRD.parameters import getParameters
from cardioception.HRD.task import run
# Create a GUI and ask for high-evel experiment parameters
g = gui.Dlg()
g.addField("participant", initial="Participant")
g.addField("session", initial="HRD")
g.addField("Serial Port:", initial="COM4")
g.addField("Setup:", initial="behavioral")
g.show()
# Set global task parameters here
parameters = getParameters(
    participant=g.data[0],
    session=g.data[1],
    serialPort=g.data[2],
    setup=g.data[3],
    nTrials=72,
    exteroception=True,
    nBreaking=18,
    screenNb=0,
    catchTrials=0,
    systole_kw={"data_format": "7"}
    )
# Run task
run(parameters, confidenceRating=True, runTutorial=True)

parameters["win"].close()
