extends Area2D

func _ready():
	set_process(true)

func _process(_delta):
	var colliding_areas = get_overlapping_bodies()
	for area in colliding_areas:
		if area.is_in_group("Player"):
			var _throwaway = get_tree().change_scene("res://ReloadPage.tscn")
