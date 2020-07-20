extends KinematicBody2D

onready var player = get_parent().get_node("Hero")
onready var particles = get_node("Particles2D")
var collisions
var velocity
var divisionfactor = 50
var quitter = 0

func _ready():
	position = player.position
	velocity = get_viewport().get_mouse_position() - player.position
	collisions = move_and_collide(velocity/divisionfactor)
	particles.rotation = get_angle_to(get_global_mouse_position()) + 80
func _process(_delta):
	collisions = move_and_collide(velocity/divisionfactor)
	if quitter >= 3:
		queue_free()
