extends TileMap


var noise = OpenSimplexNoise.new()
var counter = 3
var deletionlist = []

func create_map(xpos, ypos, width, height):
	for x in range(width):
		for y in range(height):
			if y+ypos < noise.get_noise_2d(x + xpos, 0) * 50:
				continue
			set_cell(x+xpos, y+ypos, noise.get_noise_2d(x+xpos, y+ypos)*counter+counter)
	
func deletetile():
	var mousepos = world_to_map(get_global_mouse_position())
	for each in deletionlist:
		set_cell(mousepos.x, mousepos.y, -1)
	deletionlist.append(mousepos)
	


func _ready():
	randomize()
	noise.seed = randi()
	noise.octaves = 9
	create_map(-30, -30, 60, 60)

func _process(_delta):
	create_map(world_to_map($KinematicBody2D.position).x - 100, world_to_map($KinematicBody2D.position).y - 100, 200, 200)
#	deletetile()
