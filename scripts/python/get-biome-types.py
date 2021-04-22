from os import listdir
from os.path import isfile, join

biomesFile = open('../../config/__meta/biomeTypes.json')
biomesFile.close()
allTypes = {}

biomeFilesPath = '../../mods/OpenTerrainGenerator/worlds/Far From Home 6/WorldBiomes'
allBiomeFiles = [file for file in listdir(biomeFilesPath) if isfile(join(biomeFilesPath, file))];
print(allBiomeFiles);