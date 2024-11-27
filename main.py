import os

player_position = {
	"x":0,
	"y":0
}

def move(direction):
	if direction == "d" or direction == "D":
		if player_position['x'] < 9:
			player_position['x'] += 1
	elif direction == "a" or direction == "A":
		if (player_position['x'] - 1 >= 0):
			player_position['x'] -= 1

	if direction == "s" or direction == "S":
		if player_position['y'] < 4:
			player_position['y'] += 1
	elif direction == "w" or direction == "W":
		if (player_position['y'] - 1 >= 0):
			player_position['y'] -= 1

while True:
	os.system('clear')

	print("_______________________")
	for y in range(5):
		print("\n")
		for x in range(10):
			if player_position['x'] == x and player_position['y'] == y:
				print("🦉", end="")
			else:
				print ("🟦", end="")

	print("\n")
	print("_______________________")

	direction = input("Next position (w,a,s,d): ")
	if direction == "fim":
		os.system('clear')
		break
	move (direction)

