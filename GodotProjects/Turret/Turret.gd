extends KinematicBody2D


var fireangle
var cooldown = 200
onready var player = get_parent().get_node("Hero")
var velocity = Vector2(0, 0)
var collisions
var speed = 2.5

func movement():
	if position.x > player.position.x:
		velocity = Vector2(-speed, 0)
		collisions = move_and_collide(velocity)
	if position.x < player.position.x:
		velocity = Vector2(speed, 0)
		collisions = move_and_collide(velocity)
	if position.y > player.position.y:
		velocity = Vector2(0, -speed)
		collisions = move_and_collide(velocity)
	if position.y < player.position.y:
		velocity = Vector2(0, speed)
		collisions = move_and_collide(velocity)
	velocity = Vector2(0, 0)
	collisions = move_and_collide(velocity)
	


func _process(_delta):
	if player.score >= 100:
		movement()
	fireangle = get_angle_to(player.position) + 80
	if cooldown <= 0:
		var fire = load("res://TurretFire.tscn")
		fire = fire.instance()
		fire.position = Vector2(position.x, position.y - 30)
		get_parent().add_child(fire)
		cooldown = 200
	cooldown -= 1
