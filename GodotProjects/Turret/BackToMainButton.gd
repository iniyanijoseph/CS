extends Button



func _process(_delta):
	if pressed:
		get_tree().change_scene("res://HomePage.tscn")