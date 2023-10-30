#Display settings
res = WIDTH,HEIGHT = 1200,800
fps = 60 #This should be set to a realistic, low value. 

player_pos = 1.5,5

player_angle = 0 #in radians

player_accel = .25
player_deccel = .8 #The rate at which velocity is lost after a player stops pressing. This value is multiplied by velocity, so a value of .5 would halve the velocity per second.
x_change = 0
y_change = 0
accelsens = .1 #How low x or y acceleration can go before it rounds to zero. This MUST be greater than the player_accel.
max_speed= 3

tankdimensions = 10, 10

player_rot_speed = 1 #Radians per second

# DO NOT CHANGE VALUES BELOW THIS LINE unless you're sure. They are calculated based off of earlier set values.
# They are not safe to change, as changing them could set off proportions. 

#Screen dimension multipliers. Multiply anything displayed by these to correct for changed resolution.
RESMULTX = res[0] / 1600 
RESMULTY = res[1] / 900

TANKDIMENSIONS = tankWidth, tankHeight = 10 * RESMULTX, 10 * RESMULTY
TANKCOORDINATEMULT = TANKCOORDINATEMULTX, TANKCOORDINATEMULTY =  100 * RESMULTX, 100 * RESMULTY
