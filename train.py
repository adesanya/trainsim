
class Train:
	def __init__(self, ID,station):
		self.trainid=ID
		self.station=station
		self.passangers=0

	def addPassangers(self, pcount):
		self.passangers+=pcount


if __name__=="__main__":
	print("Starting Simulation")

