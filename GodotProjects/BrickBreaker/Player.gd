extends KinematicBody2D

var velocity = Vector2(0, 0)
var collisions
var screensize = OS.window_size


func get_input():
	velocity = Vector2(0, 0)
	if Input.is_action_pressed("Left") and position.x > 0:
		velocity.x -= 3
	if Input.is_action_pressed("Right") and position.x < screensize.x:
		velocity.x += 3
		
func _process(_delta):
	get_input()
	collisions = move_and_collide(velocity)
