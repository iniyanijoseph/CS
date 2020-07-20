extends Node2D

onready var octopus = preload("res://Octopus.tscn")
var node
var countdown = 0
var screensize = OS.window_size


func _process(_delta):
	if countdown <= 0:
		node = octopus.instance()
		node.position = Vector2(int(rand_range(0, screensize.x)), int(rand_range(0, screensize.y)))
		get_parent().add_child(node)
		countdown = 300
	countdown -= 1
