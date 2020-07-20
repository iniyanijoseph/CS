extends Label


onready var paddle = get_parent().get_node("Paddle")

func _process(_delta):
	text = str(paddle.score)
