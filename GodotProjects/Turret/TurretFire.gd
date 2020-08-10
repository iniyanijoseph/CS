extends KinematicBody2D

onready var player = get_parent().get_node("Hero")
onready var particles = get_node("Particles2D")
var collisions
var velocity
var divisionfactor = 30
var countdown = 120

func _ready():
	velocity = player.position - position
	collisions = move_and_collide(velocity/divisionfactor)
	particles.rotation = get_angle_to(player.position) + 80

func _process(_delta):
	collisions = move_and_collide(velocity/divisionfactor)
	if countdown == 0:
		queue_free()
	countdown -= 1