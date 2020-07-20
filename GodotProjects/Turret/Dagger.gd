extends KinematicBody2D

onready var player = get_parent().get_node("Hero")
onready var particles = get_node("Sprite")
var collisions
var velocity
var divisionfactor = 10

func _ready():
	position = player.position
	velocity = get_viewport().get_mouse_position() - player.position
	collisions = move_and_collide(velocity/divisionfactor)
	particles.rotation = get_angle_to(get_global_mouse_position())
func _process(_delta):
	collisions = move_and_collide(velocity/divisionfactor)
	particles.rotation += 1
	if position.distance_to(player.position) > 300:
		queue_free()
