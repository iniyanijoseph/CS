extends KinematicBody2D

onready var player = get_parent().get_node("Hero")
var velocity = Vector2(0, 0)
var speed = 2
var oghealth = 3
var health = oghealth
var collisions
onready var healthbar = get_node("ProgressBar")

func _ready():
	position = Vector2(int(rand_range(50, 1250)), int(rand_range(5, 550)))

func _process(_delta):
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

	if health <= 0:
		var enemy = load("res://WillowTheWisp.tscn")
		enemy = enemy.instance()
		enemy.oghealth = oghealth + 2
		get_parent().add_child(enemy)
		player.score += 1
		queue_free()

	if collisions:
		if collisions.collider.is_in_group("Fireballs"):
			collisions.collider.queue_free()
			health -= player.attackvalue
		if collisions.collider.is_in_group("Daggers"):
			collisions.collider.queue_free()
			health = 0
	healthbar.value = health * 33
	
