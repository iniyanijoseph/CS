extends CPUParticles2D

func _ready():
	one_shot = true

func _process(_delta):
	emitting = false
	if Input.is_mouse_button_pressed(1):
		position = get_viewport().get_mouse_position()
		emitting = true
