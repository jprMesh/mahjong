# HK Mahjong
HK Mahjong engine, written in Python
Made by bored college students

## Rules of HK Mahjong

### Setup
* Tiles are shuffled face down on the table.
* Each player will create a wall of tiles in front of them, 18 wide and 2 high, face down
* Roll dice to determine who goes first
* Highest roll becomes the East wind, then going to South, West, and North counterclockwise
* Turn order is counterclockwise starting from East
* The starting wind is East, and the indicator is given to the East seat
* The East seat rolls the dice to determine which wall to break first, beginning with the next wall
* From the left of the wall from the perspective of the wall's builder, 
*     count the dice-roll-number of tiles from the left and break from there
* Each player will take 4 tiles at a time until everyone has 12 tiles
* All tiles drawn are then set upright in front of the player, forming their hand
* The East player will then draw a tile from the wall and then skip over one tile and take a 14th tile
* The remaining players will then draw their 13th tile in order
* The East player then discards a tile to the center of the table, face up, and the game begins

### Win Conditions
* Most win condition hands contain 4 triplets and a pair
* A triplet can either be three-of-a-kind of one tile, or a straight of three consecutive numbers, suited
* A three-of-a-kind is called a 'pung', and a three-straight is called a 'chi'
* It is possible to reach a four-of-a-kind, known as a 'kong'
* There are other winning hands that don't follow the above model, more on those later

### Player Turns
* A turn in Mahjong consists of drawing a tile from the wall (in the order the tiles were dealt)
* The player will then choose a tile in his/her hand to discard into the middle of the table, face up
* If a discarded tile can be used by another player to complete a pung:
  * That other player can call 'pung' and take the tile and use it to complete the pung
  * The tiles used in the pung are then placed in front of the player, face up
  * The stealing player then discards a tile, and play resumes from the stealing player's position
  * Some players' turns may be skipped because of this
* If a discarded tile can be used by another player to complete a chi:
  * The discarded tile can only be taken if it was discarded by the player to the left
  * That is, chi tiles can only be taken from the preceding player in turn order
  * The tiles used in the chi are then placed in front of the player, face up
  * If 'chi' and 'pung' is called on the same discard, then 'pung' has precedence
  * If 'chi' is called by multiple players on the same tile, then the first to do so wins

### Revealing a Player's Tiles
* The only time tiles are laid in front of a player is if that player steals a discard from another player
  * If a pung or chi is self-drawn from the wall, they do not need to reveal their tiles
  * Therefore, it is possible to steal a tile as a 'kong', which works similarly to calling 'pung'
* When taking a tile to complete a 'kong', an extra tile is drawn from the back of the wall
  * A tile is then discarded as normal
* If a player has laid a pung of tiles in front of them and then draws the 4th:
  * That player can choose to complete the kong and draw another tile form the back of the wall
  * This action can occur at any time, but only if the tile was self drawn
* If a flower/season tile is ever drawn, it is immediately placed in front of the player who drew it
  * A replacement tile from the back of the wall is then drawn, and play continues as normal
  * Flowers and seasons are used for bonus points, more on scoring later

### Scoring
* Points are awarded to the winning player based on their winning hand, plus flower/season tiles
  * Because some winning hands are easier to achieve than others, they are worth fewer points
  * For example, a hand containing only chi and a pair is worth less than one of all pungs and a pair
  * Points can only be earned each round by the player with the winning hand
* In addition to points awarded from the hand, additional points can be earned through other factors
  * For example, if the winning tile was drawn by the winning player himself, an extra point is earned
  * If the winning tile was used to complete a chi and was the middle tile, an extra point is earned
  * The wind indicator also shows how extra points can be earned
    * A pung of the prevailing wind is worth an additional point
    * A pung of your seat wind is worth an additional point
    * If the player's seat wind is also the prevailing wind, he/she can obtain both of these bonuses
    * Every four rounds, the wind changes to the next wind in seating order (E, S, W, N, E)
  * A pung of any of the three dragons is worth an additional point
* If a player discards a tile that is stolen by another player to win the game, then they lose points equal to half of the winning hand's value, rounded down (excluding flowers)
* Play continues until a player reaches a certain point goal, and is then determined the winner of the game

*Rules can be modified to suit players' needs*