extends KinematicBody2D

var speed = 4
var collision
var node
var score = 0
var health = 10
onready var attacklist = [[preload("res://Fireball.tscn"), 50, 50], [preload("res://Dagger.tscn"), 400, 400]]
onready var healthbar = get_node("HealthBar")
onready var particles = get_node("CPUParticles2D")
var attack = 0
var lifecountdown = 30
var switchcountdown = 0
var attackvalue = 1

func quittoleaderboard():
	var _randomvariable = get_tree().change_scene("res://HomePage.tscn")


func _process(_delta):
	if Input.is_key_pressed(KEY_W) or Input.is_key_pressed(KEY_UP):
		collision = move_and_collide(Vector2(0, -speed))
	if Input.is_key_pressed(KEY_A) or Input.is_key_pressed(KEY_LEFT):
		collision = move_and_collide(Vector2(-speed, 0))
		get_node("Sprite").flip_h = true
		particles.emitting = false
	if Input.is_key_pressed(KEY_S) or Input.is_key_pressed(KEY_DOWN):
		collision = move_and_collide(Vector2(0,speed))
	if Input.is_key_pressed(KEY_D) or Input.is_key_pressed(KEY_RIGHT):
		collision = move_and_collide(Vector2(speed, 0))
		get_node("Sprite").flip_h = false
		particles.emitting = true

	if Input.is_key_pressed(KEY_R):
		var _randomvalue = get_tree().reload_current_scene()

	if Input.is_mouse_button_pressed(1):
		if attacklist[0][1] >= attacklist[0][2]:
			node = attacklist[0][0].instance()
			get_parent().add_child(node)
			attacklist[0][1] = 0
	if Input.is_mouse_button_pressed(2) and switchcountdown >= 30:
		if attacklist[1][1] >= attacklist[1][2]:
			node = attacklist[1][0].instance()
			get_parent().add_child(node)
			attacklist[1][1] = 0
		switchcountdown = 0
	
	if collision:
		if collision.collider.is_in_group("Enemies") and lifecountdown >= 30:
			health -= 1
			if health <= 0:
				quittoleaderboard()
			lifecountdown = 0
		if collision.collider.is_in_group("EvilFire") and lifecountdown >= 30:
			health -= 0.5
			collision.collider.queue_free()
			if health <= 0:
				quittoleaderboard()
			lifecountdown = 0
		if collision.collider.is_in_group("Boosters"):
			attackvalue += 0.5
			collision.collider.queue_free()
		if collision.collider.is_in_group("HealthBoosters"):
			health += 1
			collision.collider.queue_free()
	lifecountdown += 1
	if health > 30:
		health = 30

	for num in range(len(attacklist)):
		if attacklist[num][1] < attacklist[num][2]:
			attacklist[num][1] += 1
	switchcountdown += 1
	healthbar.value = health*10
