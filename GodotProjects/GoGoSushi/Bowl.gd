extends KinematicBody2D

var score = 0
var level = 1

func _process(_delta):
	if Input.is_key_pressed(KEY_LEFT) and position.x > 0:
		position.x -= 3
	if Input.is_key_pressed(KEY_RIGHT) and position.x < 1000:
		position.x += 3
	if Input.is_key_pressed(KEY_R):
		get_tree().reload_current_scene()
	if score > 100:
		score = 0
		level += 1
	if score < 0:
		get_tree().quit()
		
	get_parent().get_node("ProgressBar").value = score
	get_parent().get_node("Label").text = str(level)+":"+str(int(score))
