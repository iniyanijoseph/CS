extends KinematicBody2D

var collisions
var velocity = Vector2(1, 1)

func _process(_delta):
	collisions = move_and_collide(velocity)
	if collisions:
		velocity.y *= -1
		velocity.x *= -1

