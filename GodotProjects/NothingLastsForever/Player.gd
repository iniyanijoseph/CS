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
onready var timer = get_node("Timer")
var score = 0

func _ready():
	timer.set_wait_time(10)
	timer.start()

func get_input(delta):
	velocity = Vector2(0, 0)
	if Input.is_action_pressed("Right"):
		$AnimatedSprite.play("Right")
		velocity.x += speed
		firedirection = 77
	
	if Input.is_action_pressed("Left"):
		$AnimatedSprite.play("Left")
		velocity.x -= speed
		firedirection = -77
	if Input.is_action_just_pressed("Jump"):
		if jump:
			speedy = -jumpforce
			$JumpSound.play()
	
	if not Input.is_action_pressed("Left") and not Input.is_action_pressed("Right"):
		$AnimatedSprite.play("Front")
	
	speedy += gravity * delta
	
	velocity.y  = speedy
	velocity = move_and_slide(velocity, Vector2(0, -1))
	if is_on_floor():
		jump = true
	else:
		jump = false

#func fire():
#	if Input.is_action_just_pressed("Fire"):
#		var node = load("res://Fireball.tscn").instance()
#		node.rotation = firedirection
#		node.position = position
#		if get_global_mouse_position().x < position.x:
#			node.velocity.x = -4
#			node.rotation_degrees = -90
#		if get_global_mouse_position().x > position.x:
#			node.velocity.x = 4
#			node.rotation_degrees = 90
#		get_parent().add_child(node)
#		$ShootSound.play()


func _process(delta):
	get_input(delta)
	# fire()
	if position.y > 800:
		$AnimatedSprite.rotation += 0.1
	if position.y > 2400:
		var _throwaway = get_tree().reload_current_scene()
	
	$ProgressBar.value = timer.time_left * 10
	$RichTextLabel.text = str(score)
	

func _on_Timer_timeout():
	var _throwaway = get_tree().reload_current_scene()
