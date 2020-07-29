extends MarginContainer

var zoom = 1.5
var screensize = OS.window_size
var health = 100
var score = 0

var projections = {}
onready var octopi = get_tree().get_nodes_in_group("Octopi")
var scale = rect_size/(screensize*zoom)
onready var healthbar = get_node("StaticBody2D/ProgressBar")

func _process(_delta):
	octopi = get_tree().get_nodes_in_group("Octopi")
	for item in projections:
		var objectposition = (item.position - Vector2(screensize.x/2, screensize.y/2))*scale + rect_size/2
		projections[item].position = objectposition
	healthbar.value = health
	if health <= 0:
		get_tree().reload_current_scene()
	for item in octopi:
		if not item in projections:
			var new_projection = get_node("Sprite").duplicate()
			add_child(new_projection)
			new_projection.show()
			projections[item] = new_projection

