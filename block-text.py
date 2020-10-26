from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()

mc.postToChat("Hello world")
x, y, z = mc.player.getTilePos()                                                  
#x, y, z = mc.player.getPos()

mc.postToChat("LEAVES")
mc.setBlock(x+1, y, z, 18)
mc.postToChat("WOOD")
mc.setBlock(x, y+1, z, 17)
mc.postToChat("COAL_ORE")
mc.setBlock(x, y, z+1, 16)
mc.postToChat("Crafting Table")
mc.setBlock(x-1, y, z+1, 58)
mc.postToChat("Furnace")
mc.setBlock(x, y+2, z-2, 61)
mc.postToChat("Fence")
mc.setBlock(x+1, y, z-1, 85)
mc.postToChat("Bedrock")
mc.setBlock(x, y+4, z-2, 7)
mc.postToChat("Wool")
mc.setBlock(x-3, y, z-2, 35)
mc.postToChat("Bookshelf")
mc.setBlock(x, y, z+5, 47)
mc.postToChat("Glowstone")
mc.setBlock(x, y+2, z, 89)


#COAL_ORE             16
#WOOD                 17
#LEAVES               18
#Crafting Table       58
#furnace              61
#Fence				  85
#Bedrock			   7
#Wool				  35
#Bookshelf			  47
#Glowstone			  89