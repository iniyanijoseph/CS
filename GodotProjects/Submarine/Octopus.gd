extends KinematicBody2D

var velocity = Vector2()
var screensize = OS.window_size
var radar = OS.window_size/2
var collisions
onready var radarmap = get_parent().get_node("CanvasLayer/RadarMap")


func _process(delta):
	velocity = radar - position
	collisions = move_and_collide(velocity*delta/2)
	if collisions:
		radarmap.health -= 0.05
	if get_node("Button").pressed:
		queue_free()
		radarmap.score += 1


