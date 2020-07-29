extends KinematicBody2D

var velocity = Vector2(-1.5, -1.5)
var collisions
var screensize = OS.window_size

func bounce():
	collisions = move_and_collide(velocity)
	if collisions:
		if collisions.collider.is_in_group("Brick"):
			collisions.collider.queue_free()
			velocity *= 1.05
		velocity.y *= -1
	if position.x > screensize.x or position.x < 0:
		velocity.x *= -1
	if position.y < 0:
		velocity.y *= -1


func _process(_delta):
	bounce()
