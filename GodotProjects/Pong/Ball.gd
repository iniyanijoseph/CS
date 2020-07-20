extends KinematicBody2D

var screensize
var velocity = Vector2()
var collisions
onready var lpaddle = get_parent().get_node("Paddle")
onready var rpaddle = get_parent().get_node("Paddle2")

func _ready():
	screensize = get_viewport_rect().size
	print(screensize)
	position = screensize / 2
	velocity = Vector2(-200, -200)
	
func _physics_process(_delta):
	collisions = move_and_collide(velocity/75)
	if collisions:
		velocity[0] = velocity[0] * -1

	if position.x <= 0:
		position = screensize / 2
		velocity = Vector2(-200, -200)
		rpaddle.score += 1
		
	if position.x >= screensize.x:
		position = screensize / 2
		velocity = Vector2(-200, -200)
		lpaddle.score += 1
	
	if rpaddle.score == 10 or lpaddle.score == 10:
		get_tree().quit()

func _process(_delta):
	screensize = get_viewport_rect().size
	if position.y >= screensize.y:
		velocity[1] = velocity[1] * -1
	if position.y <= 0:
		velocity[1] = velocity[1] * -1
