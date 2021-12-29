namespace SpriteKind {
    export const Healer = SpriteKind.create()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    CarGun = sprites.createProjectileFromSprite(img`IMAGE NOT AVAILABLE`, myPlayer, 125, 0)
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    game.over(false, effects.dissolve)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Healer, function (sprite, otherSprite) {
    HealthBar.value += 25
    sprite.destroy()
    otherSprite.destroy()
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprite.destroy()
    otherSprite.destroy()
    info.changeScoreBy(10)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    HealthBar.value += -15
    otherSprite.destroy()
    info.changeScoreBy(-25)
})
let projectile: Sprite = null
let theEnemy: Sprite = null
let CarGun: Sprite = null
let HealthBar: StatusBarSprite = null
let myPlayer: Sprite = null
effects.clouds.startScreenEffect()
scene.setBackgroundColor(9)
myPlayer = sprites.create(img`IMAGE NOT AVAILABLE`, SpriteKind.Player)
myPlayer.setStayInScreen(true)
myPlayer.x = 10
controller.moveSprite(myPlayer, 0, 75)
HealthBar = statusbars.create(15, 2, StatusBarKind.Health)
HealthBar.attachToSprite(myPlayer, -20, 1)
HealthBar.value = 100
game.onUpdateInterval(1000, function () {
    if (info.score() >= 1000) {
        game.over(true, effects.confetti)
    }
})
game.onUpdateInterval(1500, function () {
    theEnemy = sprites.createProjectileFromSide(img`IMAGE NOT AVAILABLE`, -26, 0)
    theEnemy.setKind(SpriteKind.Enemy)
    theEnemy.y = randint(10, 120)
})
game.onUpdateInterval(10000, function () {
    projectile = sprites.createProjectileFromSide(img`IMAGE NOT AVAILABLE`, -50, 0)
    projectile.setKind(SpriteKind.Healer)
    projectile.y = randint(10, 120)
})
