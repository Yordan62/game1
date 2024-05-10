scene.onOverlapTile(SpriteKind.Player, sprites.builtin.forestTiles0, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    if (controller.A.isPressed()) {
        timer.throttle("chop", 1000, function on_throttle() {
            
            wood += 1
            if (Math.percentChance(2)) {
                tiles.setTileAt(location, sprites.castle.tileGrass2)
            }
            
        })
        guy.sayText(wood)
    }
    
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    if (tiles.tileAtLocationEquals(guy.tilemapLocation(), sprites.builtin.forestTiles0)) {
        
    }
    
})
let wood = 0
let guy : Sprite = null
tiles.setCurrentTilemap(tilemap`
    test
`)
guy = sprites.create(assets.image`
    Guy1
`, SpriteKind.Player)
guy.setScale(2, ScaleAnchor.Middle)
controller.moveSprite(guy)
wood = 0
scene.cameraFollowSprite(guy)
