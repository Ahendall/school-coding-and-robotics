// Removed Images for Simplification Purpouses

controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    CarGun = sprites.createProjectileFromSprite(img `IMAGE NOT AVAILABLE`, myPlayer, 125, 0)
})
info.onLifeZero(function () {
    game.over(false, effects.melt)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.destroy()
    info.changeScoreBy(10)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    otherSprite.destroy()
    info.changeScoreBy(-25)
})
let theEnemy: Sprite = null
let CarGun: Sprite = null
let myPlayer: Sprite = null
effects.clouds.startScreenEffect()
scene.setBackgroundColor(9)
myPlayer = sprites.create(img `IMAGE NOT AVAILABLE`, SpriteKind.Player)
myPlayer.setStayInScreen(true)
myPlayer.x = 10
controller.moveSprite(myPlayer, 0, 75)
game.onUpdateInterval(1000, function () {
    if (info.score() >= 1000) {
        game.over(true, effects.confetti)
    }
})
game.onUpdateInterval(1500, function () {
    theEnemy = sprites.createProjectileFromSide(img `IMAGE NOT AVAILABLE`, -26, 0)
    theEnemy.setKind(SpriteKind.Enemy)
    theEnemy.y = randint(10, 120)
})
