extends KinematicBody2D

var velocity = Vector2(0, 0)
var score = 0
var collisions

func _process(_delta):
	velocity = Vector2(0, 0)
	if Input.is_key_pressed(KEY_W):
		velocity.y -= 2
	if Input.is_key_pressed(KEY_S):
		velocity.y += 2
	if Input.is_key_pressed(KEY_A):
		velocity.x -= 2
	if Input.is_key_pressed(KEY_D):
		velocity.x += 2
	collisions = move_and_collide(velocity)
	get_parent().get_node("Label").text = str(score)
	if score == 5:
		get_tree().reload_current_scene()
