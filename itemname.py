import random

bases = """sword
axe
hammer
amulet
potion
broom
orb
cloak
armor
circlet
boots
bag
shield
shackles
glasses
helmet
book
bow
ring
socks
ointment
deck
fork
cart
boat
paper
arrows
apparatus
slippers
greaves
staff
skull
head
hand
glue
quiver
token
instrument
mirror
flask
keg
javelin
dagger
maul
shuriken
spiked chain
dust
gem
gate
carpet
candle
crystal ball
fortress
figurine
hat
portable ram
trap
box
ioun stone
horn
trinket
machine"""

locations = """
fantasy village
magic forest
dragon's lair
enchanted castle
elven city
dwarven mine
wizard's tower
haunted graveyard
orc stronghold
goblin cave
dark swamp
knight's training ground
sorcerer's academy
thieves' guild hideout
mermaid's cove
troll bridge
fairy glen
undead crypt
wizard's library
druidic grove
witch's hut
treasure-filled dungeon
mystical ruins
celestial observatory
elemental plane
astral realm
planar crossroads
forgotten temple
abyssal rift
angelic citadel
shadowy underworld
lycanthrope den
necromancer's sanctum
clockwork workshop
warlock's pact realm
underground city
beastman encampment
mysterious island
underwater cavern
timeless pocket dimension
arcane battleground
demon-infested wasteland
divine garden
floating fortress
jungle temple
mad alchemist's laboratory
phoenix nest
twisted labyrinth
ghost ship
oracle's sanctuary
giant's stronghold
golem foundry
dreamwalker's realm
vampire's castle
plague-ridden village
wandering nomad camp
entangled thicket
celestial court
abandoned celestial city
forgotten astral prison"""

creatures = """
dragon
goblin
orc
elf
dwarf
troll
gnome
kobold
centaur
minotaur
harpy
siren
merfolk
sphinx
unicorn
phoenix
werewolf
vampire
zombie
skeleton
ghost
demon
angel
fairy
giant
ogre
cyclops
hydra
chimera
griffin
wyvern
elemental
golem
gargoyle
lich
beholder
mind flayer
nymph
satyr
kraken
manticore
djinn
mummy
wraith
gorgon
kraken
pegasus
treant
lamia
basilisk
rakshasa
salamander
changeling
hobgoblin
tengu
mimic
rust monster
blink dog
displacer beast"""

spells = """
enchantment
evocation
illusion
conjuration
abjuration
transmutation
necromancy
divination
charm
hex
curse
blessing
summoning
compulsion
protection
fire
ice
lightning
earth
wind
water
shadow
light
healing
banishment
augmentation
teleportation
mind control
time manipulation
creation
destruction
hexbreaking
illusion
shape-shifting
warding
fortune-telling
invisibility
mind reading
telekinesis
fear
love
truth
memory manipulation
elemental manipulation
fate weaving
spiritual communion
phasing
soulbinding
telepathy
dreamwalking
alchemy
curses
blessings
illusion
prophecy
necromancy
weather manipulation
energy drain
astral projection
illusion
healing
enhancement
demonology
angelic intervention
teleportation
creation
hexbreaking
warding
fey magic
geomancy
songweaving
runecasting
starcalling
chronomancy
geomancy
psionics
planar manipulation
mind melding
polymorphing
molecular disruption
pyromancy
aquamancy
aeromancy
terramancy
cryomancy
celestial magic
transfiguration
curse-breaking
illusion
portal manipulation
spirit calling
divine intervention
time dilation
cosmic manipulation
cataclysmic spells
reanimation
perception alteration
dimensional manipulation
soul manipulation"""


enchantments = """flaming
frost
healing
adamantine
death
commanding elementals
flying
talking
awakened
teleportation
unlocking
lucky
unlucky
instant
illusion
illusionary
many things
dwarven
draconic
disguise
feindish
knowledge
toughness
serpentine
folding
theives
holding
devouring
alien
eldritch
fireball
archmage
cubic
crab
stars
wild
natural
lycanthrope (wolf)
ursanthrope (bear)
felinethrope (tiger)
smashing
horripilating
revivification
holy
unholy
gravity
paper
mechanical
electricity
sonic
endless water
cursed (make something up)
jousting
charming
swarming
swarming insects
snake
fuzzy
soft
lifestealing
vorpal
the sphere
ultimate evil
pure good
true neutral
tentacle
enemy detection
secret
wonder
vecna
fish command
sticky
creative
rulership
eyes
fire resistance
telekinesis
wishes
x-ray vision
animal influence
limitless
wild magic
the sewers
todd
love
life trapping
soul trapping
tripping
psychadelic
berserker
dry
elvenkind
displacement
winterlands
northern
levitating
arrow attraction
bat
manta ray
arachnida
drow
glamerous
free action
jumping
warmth
regeneration
annihilation
refridgeration
spherical
monkey
primal
psychic
woodlands
sharpness
smiting
bane of arthropods
fear
web
plane shift
winged
sun
son
spellguard
gaseous form
gaseous
valhalla
horned
golden lion
purple
enlargement
shrinking
slaying
tricky
awakened
unsheathed
prime
mystical
gleaming
enchanted
cursed
ancient
radiant
shadowy
whispering
ornate
runed
ethereal
intricate
glowing
forgotten
dreadful
celestial
fiery
frozen
arcane
serrated
ebon
gilded
luminous
sacrificial
arcane
malevolent
resplendent
vorpal
vengeful
vibrant
timeless
abyssal
otherworldly
necrotic
transcendent
perfected
empyreal
crimson
iridescent
eldritch
corrupted
thunderous
prismatic
harmonious
molten
umbral
blighted
harbinger
fey
pristine
titanic
ethereal
phantom
penumbral
verdant
infernal"""

#basesList = bases.split("\n")
#print(basesList)
enchantmentsList = enchantments.split("\n")
#print(enchantmentsList)

magicItemList = []

def makeItem(baseString = bases):
    base = getBase(baseString.split("\n"))
    enchantment = getEnchantment()
    magicItem = ""
    roll = random.randint(0,20) #rolls to see if it's
    if roll < 10:   #[ENCHANTMENT] [BASE] (10/21)
        magicItem += enchantment+" "+base
    elif roll == 20:#[ENCHANTMENT] [BASE] of [ENCHANTMENT 2] (1/21)
        enchantment2 = getEnchantment()
        magicItem += enchantment+" "+base+" of "+enchantment2
    else:        #or [BASE] of [ENCHANTMENT] (10/21)
        magicItem += base+" of "+enchantment
    return magicItem

def getEnchantment():
    return enchantmentsList[random.randint(0,len(enchantmentsList)-1)]

def getBase(ls):
    return ls[random.randint(0,len(ls)-1)]
