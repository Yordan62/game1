def on_overlap_tile(sprite, location):
    if controller.A.is_pressed():
        
        def on_throttle():
            global wood
            wood += 1
            if Math.percent_chance(2):
                tiles.set_tile_at(location, sprites.castle.tile_grass2)
        timer.throttle("chop", 1000, on_throttle)
        
        guy.say_text(wood)
scene.on_overlap_tile(SpriteKind.player,
    sprites.builtin.forest_tiles0,
    on_overlap_tile)

def on_a_pressed():
    if tiles.tile_at_location_equals(guy.tilemap_location(), sprites.builtin.forest_tiles0):
        pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

wood = 0
guy: Sprite = None
tiles.set_current_tilemap(tilemap("""
    test
"""))
guy = sprites.create(assets.image("""
    Guy1
"""), SpriteKind.player)
guy.set_scale(2, ScaleAnchor.MIDDLE)
controller.move_sprite(guy)
wood = 0
scene.camera_follow_sprite(guy)
