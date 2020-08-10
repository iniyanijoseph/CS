extends KinematicBody2D

var velocity = Vector2(0, -1)
var collisions

func _process(_delta):
	collisions = move_and_collide(velocity)
	if collisions:
		velocity.y *= -1
		$CPUParticles2D.restart()
		$CPUParticles2D.rotation_degrees += 180
		if collisions.collider.is_in_group("Player"):
			var _throwaway = get_tree().reload_current_scene()
