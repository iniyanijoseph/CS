extends Node2D

var poweredups = []
onready var player = get_node("Hero")

func _ready():
	for _element in range(5):
		var enemy = load("res://WillowTheWisp.tscn")
		enemy = enemy.instance()
		add_child(enemy)

func _process(_delta):
	if player.score%10 == 0 and player.score != 0 and player.score:
		if player.score in poweredups:
			pass
		else:
			var booster = load("res://Booster.tscn")
			booster = booster.instance()
			booster.position = Vector2(int(rand_range(50, 950)), int(rand_range(50, 550)))
			add_child(booster)
			booster = load("res://HealthBooster.tscn")
			booster = booster.instance()
			booster.position = Vector2(int(rand_range(50, 950)), int(rand_range(50, 550)))
			add_child(booster)
			poweredups.append(player.score)
