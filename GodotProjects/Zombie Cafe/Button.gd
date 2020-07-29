extends Button

func _process(delta):
	if pressed:
		get_tree().change_scene("res://Game.tscn")
