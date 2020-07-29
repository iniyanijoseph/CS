extends KinematicBody2D

var collisions
var points
var tastyimages = [preload("res://Sushi.png"), preload("res://Octopus.png"), preload("res://Shrimp.png"), preload("res://SalmonRoll.png")]
var disgustingimages = [preload("res://Turnip.png"), preload("res://Cabbage.png"), preload("res://Broccoli.png")]
onready var image = get_node("Sprite")
var screensize = OS.window_size
var speed = 1

func _ready():
	if int(rand_range(0, 2)) == 0:
		image.texture = tastyimages[rand_range(0, len(tastyimages))]
		points = rand_range(10, 20)
	else:
		image.texture = disgustingimages[rand_range(0, len(disgustingimages))]
		points = rand_range(-10, - 20)
	position.x = rand_range(40, 1000-40)

func _process(_delta):
	collisions = move_and_collide(Vector2(0, 2*speed))
	if collisions:
		if collisions.collider.is_in_group("Bowl"):
			get_parent().get_node("Bowl").score += points
			queue_free()
		else:
			queue_free()
	rotation += 0.01
