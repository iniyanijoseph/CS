extends KinematicBody2D

var velocity = Vector2(0, 2)
var collisions
var screensize = OS.window_size

func _process(_delta):
	collisions = move_and_collide(velocity)
	if position.y > screensize.y or position.y < screensize.y:
		velocity.y = -velocity.y
