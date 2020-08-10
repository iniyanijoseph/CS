extends Sprite

func _process(_delta):
	if get_parent().get_node("PlayButton").pressed:
		var _throwaway = get_tree().change_scene("res://Game.tscn")
	if get_parent().get_node("TutorialButton").pressed:
		var _throwaway = get_tree().change_scene("res://Tutorial.tscn")
