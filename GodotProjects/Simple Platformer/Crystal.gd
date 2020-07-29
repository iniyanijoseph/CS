extends RigidBody2D

onready var hook = get_node("Hook")

func _ready():
	hook.contact_monitor = true


func hookon():
	if Input.is_action_just_pressed("ui_select") and len(hook.get_colliding_bodies()) == 0:
		hook.friction = 1
		hook.apply_impulse(Vector2(0, 0), get_global_mouse_position() - position)

func restartscene():
	if Input.is_action_just_pressed("Restart"):
		get_tree().reload_current_scene()

func _process(_delta):
	hookon()
	restartscene()
