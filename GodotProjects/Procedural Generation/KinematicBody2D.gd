extends KinematicBody2D
var velocity = Vector2(0, 0)
var speed = 300
var collisions
var firedirection = 77
var jumpforce = 400
var gravity = 800
var speedy = 0
var slide
var jump = false
var score = 0

func get_input(delta):
	velocity = Vector2(0, 0)
	if Input.is_action_pressed("Right"):
		velocity.x += speed
		firedirection = 77
	
	if Input.is_action_pressed("Left"):
		velocity.x -= speed
		firedirection = -77
	if Input.is_action_pressed("Jump"):
		if jump:
			speedy = -jumpforce
	
	speedy += gravity * delta
	
	velocity.y  = speedy
	velocity = move_and_slide(velocity, Vector2(0, -1))
	if is_on_floor():
		jump = true
	else:
		jump = false
		
func _process(delta):
	get_input(delta)
