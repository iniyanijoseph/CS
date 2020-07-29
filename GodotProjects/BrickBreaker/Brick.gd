extends KinematicBody2D


func _process(delta):
	var collisions = move_and_collide(Vector2(0, 0))
