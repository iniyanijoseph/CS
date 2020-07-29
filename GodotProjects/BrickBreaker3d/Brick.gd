extends KinematicBody

func _process(_delta):
	var collisions = move_and_collide(Vector3(0, 0, 0))
	if collisions:
		queue_free()
