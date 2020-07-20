extends Label


onready var paddle = get_parent().get_node("Paddle2")

func _process(_delta):
	text = str(paddle.score)
