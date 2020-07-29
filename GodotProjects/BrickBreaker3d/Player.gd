extends KinematicBody

var velocity = Vector3(0, 0, 0)
var collisions

func _process(delta):
	velocity = Vector3(0, 0, 0)
	if Input.is_key_pressed(KEY_LEFT) and translation.x > -10:
		velocity.x -= 2
	if Input.is_key_pressed(KEY_RIGHT) and translation.x < 66:
		velocity.x += 2
	collisions = move_and_collide(velocity)
