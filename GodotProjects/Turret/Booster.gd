extends KinematicBody2D

var countdown = 200

func _process(_delta):
	if countdown <= 0:
		queue_free()
	countdown -= 1
