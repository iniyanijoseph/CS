extends KinematicBody2D

var velocity = Vector2(0, 0)
var collisions

func move(delta):
	collisions = move_and_collide(velocity * delta)
	
	if collisions:
		if collisions.collider.is_in_group("Zombie"):
			collisions.collider.queue_free()
		queue_free()
		get_parent().get_node("Spawner").amount += 1

func _process(delta):
	move(delta)
