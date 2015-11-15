class Players:
	wind = ""	#E, S, W, N
	hand = []	#initialize empty hand list

	def __init__(self, wind, hand):
		self.wind = wind
		self.hand = hand

	#draw from the wall, normal animation
	def draw():
		hand.append(wall.pop())

	#draw from the wall, but have the animation draw from the back
	def backDraw():
		hand.append(wall.pop())

	#discard a tile, need to choose by mouse movements
	def discard(tile):
		hand.pop(tile)
