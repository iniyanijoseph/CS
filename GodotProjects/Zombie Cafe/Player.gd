extends KinematicBody2D

var speed = 4
var velocity
var collisions
var coffee = preload("res://Coffee.tscn")
var firelimit = 50
var health = 100

func get_input():
	velocity = Vector2(0, 0)
	if Input.is_action_pressed("UP"):
		velocity.y -= speed
	if Input.is_action_pressed("DOWN"):
		velocity.y += speed
	if Input.is_action_pressed("LEFT"):
		velocity.x -= speed
	if Input.is_action_pressed("RIGHT"):
		velocity.x += speed
	
	collisions = move_and_collide(velocity)

func damage():
	if collisions:
		if collisions.collider.is_in_group("Zombie"):
			health -= 1
	if health <= 0 or Input.is_action_pressed("QUIT"):
		get_tree().change_scene("res://Home.tscn")
	get_node("Energy").value = health
	
func shootcoffee():
	if Input.is_action_pressed("Fire") and firelimit < 0:
		var node = coffee.instance()
		node.position = position
		node.velocity = get_global_mouse_position() - position
		node.velocity *= Vector2(2, 2)
		get_parent().add_child(node)
		firelimit = 50
	firelimit -= 1

func _process(_delta):
	get_input()
	damage()
	shootcoffee()
