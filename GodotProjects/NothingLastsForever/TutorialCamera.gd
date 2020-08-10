extends KinematicBody2D

func _process(_delta):
	var collisions = move_and_collide(Vector2(2, 0))
	if collisions:
		var _throwaway = get_tree().change_scene("res://HomePage.tscn")
