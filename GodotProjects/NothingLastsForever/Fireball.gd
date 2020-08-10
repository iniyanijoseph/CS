extends KinematicBody2D

var velocity = Vector2(0, 0)
var collisions

func _ready():
	collisions = move_and_collide(velocity)

func _process(_delta):
	collisions = move_and_collide(velocity)
	if collisions:
		queue_free()
