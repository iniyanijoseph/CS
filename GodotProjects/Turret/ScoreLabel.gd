extends Label

onready var player = get_parent()

func _process(_delta):
	text = str(player.score)
