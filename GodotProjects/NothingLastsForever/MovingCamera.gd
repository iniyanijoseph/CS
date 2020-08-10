extends Area2D

func _process(_delta):
	position.x += 5
	if position.x > 3000:
		var _throwaway = get_tree().change_scene("res://HomePage.tscn")
