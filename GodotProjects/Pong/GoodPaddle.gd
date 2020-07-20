extends KinematicBody2D

var screensize
var score = 0
onready var ball = get_parent().get_node("Ball")

func _ready():
	screensize = get_viewport_rect().size
	position.y = (screensize.y / 2)

func _input(_event):
	screensize = get_viewport_rect().size
	if Input.is_key_pressed(KEY_W) and position.y > 45:
		position.y -= 5
	if Input.is_key_pressed(KEY_S) and position.y < screensize.y - 45:
		position.y += 5
	if ball.position.x >= screensize.x:
		score += 1
