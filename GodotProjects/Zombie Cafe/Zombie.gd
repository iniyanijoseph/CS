extends KinematicBody2D

var speed = 3
var collisions
var velocity
onready var waiter = get_parent().get_node("Player")

func get_input():
	velocity = Vector2(0, 0)
	if waiter.position.x < position.x:
		velocity.x -= speed
	if waiter.position.x > position.x:
		velocity.x += speed
	if waiter.position.y < position.y:
		velocity.y -= speed
	if waiter.position.y > position.y:
		velocity.y += speed

	collisions = move_and_collide(velocity)

func _process(_delta):
	get_input()
