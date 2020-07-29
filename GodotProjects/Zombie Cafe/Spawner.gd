extends Node2D

var countdown = 300
var amount = 1
var zombie = preload("res://Zombie.tscn")


func _process(delta):
	if countdown <= 0:
		for element in range(amount):
			var node = zombie.instance()
			node.position.x += 50
			get_parent().add_child(node)
			countdown = 300
	countdown -= 1
