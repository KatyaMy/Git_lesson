# https:/www.codewars.com/kata/5b36137991c74600f200001b/train/python

def kill_monsters(health, monsters, damage):
    hits = monsters//3
    remaining_monsters = monsters%3
    if not remaining_monsters:
        hits -= 1
    received_damage = damage*hits
    remaining_health = health - received_damage
    if remaining_health  <= 0:
        return "hero died"
    return f"hits: {hits}, damage: {received_damage}, health: {remaining_health}"
