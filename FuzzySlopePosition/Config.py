#! /usr/bin/env python
#coding=utf-8

# This file contains all configuration for running the Fuzzy Slope Postion workflow.
from Nomenclature import *

## Stage 0: Configuration 
    
####    Required    ####
exeDir = r'E:\coding\Taudem5PCVS2010Soln_512\Taudem5PCVS2010\Release'  ## if the executable files' path has been exported to the environmental path, set exeDir to None
rootDir = r'E:\data\DEMs\pleasantvalley_pre'                               ## workspace
preprocess = False                                       ## if preprocessing for parameters' grids is needed, and True by default.
inputProc = 8                                            ## parallel processor's number
## Preprocessing for terrain attributes grid, need if preprocess is True
FlowModel = 0                                            ## 0 represents D8 flow model, and 1 represent D-infinity model                  
rawdem = r'E:\data\DEMs\pleasantvalley_pre\pvdem.tif'                                            ## input dem, be caution! DEM file should have one cell buffer
outlet = r'E:\data\DEMs\pleasantvalley_pre\outlet.shp'                                             ## input outlet shapefile, be caution! The outlet point should locate at least one cell inner the DEM boundary

## Selection of Typical Locations
                                                         ## TerrainAttrDict stores the terrain attributes' name and grid path. 'RPI' is required!
                                                         ## By default: TerrainAttrDict = {'RPI':RPI,'ProfC':ProfC_mask,'HorizC':HorizC_mask,'Slope':Slope}

TerrainAttrDict = {'RPI':r'E:\data\DEMs\pleasantvalley_pre\DinfParams\RPI.tif',\
                   'ProfC':r'E:\data\DEMs\pleasantvalley_pre\DinfParams\ProfC.tif',\
                   'Slope':r'E:\data\DEMs\pleasantvalley_pre\DinfParams\Slp.tif'}
                   #'HorizC':r'E:\data\DEMs\pleasantvalley\params\HorizC.tif',\
                   
                   #'Elev':r'E:\data\DEMs\pleasantvalley\params\DEM.tif'}
AutoTypLocExtraction = True
AutoInfParams = True
RdgExtractionInfo = [['RPI',0.99,1.0]]                   ## default RPI value range for Ridge, Shoulder, Back, Foot and valley.                                              
ShdExtractionInfo = [['RPI',0.9,0.95]]
BksExtractionInfo = [['RPI',0.5,0.6]]
FtsExtractionInfo = [['RPI',0.15,0.2]]
VlyExtractionInfo = [['RPI',0.0,0.1]]

####    Optional    ####
centerweight = 0.4                                       ## Center Smoothing Weight, default is 0.4, for Peuker Douglas algorithm
sideweight = 0.1                                         ## Side Smoothing Weight, default is 0.1, for Peuker Douglas algorithm
diagonalweight = 0.05                                    ## Diagonal Smoothing Weight, default is 0.05, for Peuker Douglas algorithm
maxMoveDist = 50                                         ## the maximum number of grid cells that the points in the input outlet shapefile will be moved before they are saved to the output outlet shapefile
numthresh = 20                                           ## the number of steps to divide the search range into when looking for possible threshold values using drop analysis
logspace = 'true'                                        ## 'true' means use logarithmic spacing for threshold values, 'false' means linear spacing

D8StreamThreshold = 100                                  ## for D8 stream extraction from DEM, default is 0, which means the value is determined by drop analysis
negD8StreamThreshold = 0                                 ## for D8 ridge extraction from negative DEM, default is 0, which indicate that the value is equal to D8StreamThreshold

D8DownMethod = 'Surface'                                 ## for D8DistDownToStream, it can be Horizontal, Vertical, Pythagoras and Surface, the default is 'Surface'
D8StreamTag = 1                                          ## for D8DistDownToStream, it should be integer, the default is 1
D8UpMethod =  'Surface'                                  ## for D8DistUpToRidge, it can be Horizontal, Vertical, Pythagoras and Surface, the default is 'Surface'
D8UpStats = 'Average'                                    ## for D8DistUpToRidge, it can be Average, Maximum, Minimum

DinfStreamThreshold = 0                                  ## for Dinf stream extraction from DEM, default is 0, which means the value is equal to D8StreamThreshold
negDinfStreamThreshold = 0                               ## for Dinf ridge extraction from negative DEM, default is 0, which means the value is equal to DinfStreamThreshold

DinfDownStat = 'Average'                                 ## used for D-infinity distance down, Average, Maximum, Minimum, and Average is the default
DinfDownMethod = 'Surface'                               ## Horizontal, Vertical, Pythagoras, Surface, and Surface is the default
DinfDistDownWG = ''                                      ## weight grid, the default is none
propthresh = 0.0                                         ## The proportion threshold parameter where only grid cells that contribute flow with a proportion greater than this user specified threshold (t) is considered to be upslope of any given grid cell
DinfUpStat = 'Average'                                   ## same as DinfDownStat
DinfUpMethod = 'Surface'                                 ## same as DinfDownMethod

## Selection of Typical Locations
RdgTag = 1
ShdTag = 1
BksTag = 1
FtsTag = 1
VlyTag = 1

ExtLog = True                                            
                                                        ## if AutoTypLocExtraction is false, please uncomment the following five lines, and modified by yourself.
if not AutoTypLocExtraction:
    RdgExtractionInfo = [['RPI',0.99,1.0],['ProfC',0.00,1.0],['Slope',0.0,1.0],['Elev',285.0,2000.0]]                                                    
    ShdExtractionInfo = [['RPI',0.9,0.95],['ProfC',0.005,1.0]]
    BksExtractionInfo = [['RPI',0.5,0.6],['ProfC',-0.0001,0.0001],['Slope',10.0,90.0]]
    FtsExtractionInfo = [['RPI',0.15,0.2],['ProfC',-1.0,-0.005]]
    VlyExtractionInfo = [['RPI',0.0,0.1],['ProfC',-0.0001,0.0001],['Slope',0.0,1.0]]
## Fuzzy slope position inference
                                                         ## when AutoInfParams is Ture, the program will generate inference parameters automatically.
                                                         ## if AutoInfParams is False, it means users can edit either the InferenceInfo below or the InfConfig.dat in Config Folder. 
# Default	w1	r1	k1	w2	r2	k2
# B         6	2	0.5	6	2	0.5
# S         6	2	0.5	1	0	1
# Z         1	0	1	6	2	0.5
InfFuncParam = [['B',6,2,0.5,6,2,0.5],['S',6,2,0.5,1,0,1],['Z',1,0,1,6,2,0.5]]
if not AutoInfParams:
    RdgInferenceInfo = [['RPI','S',0.1,2,0.5,1,0,1],['ProfC','S',0.005,2,0.5,1,0,1],['Slope','Z',1,0,1,5,2,0.5]]
    ShdInferenceInfo = [['RPI','B',0.05,2,0.5,0.05,2,0.5],['ProfC','S',0.005,2,0.5,1,0,1],['Slope','B',5,2,0.5,5,2,0.5]]
    BksInferenceInfo = [['RPI','B',0.3,2,0.5,0.3,2,0.5],['ProfC','B',0.005,2,0.5,0.005,2,0.5],['Slope','S',5,2,0.5,1,0,1]]
    FtsInferenceInfo = [['RPI','B',0.05,2,0.5,0.05,2,0.5],['ProfC','Z',1,0,1,0.005,2,0.5],['Slope','B',5,2,0.5,5,2,0.5]]
    VlyInferenceInfo = [['RPI','Z',1,0,1,0.1,2,0.5],['ProfC','B',0.005,2,0.5,0.005,2,0.5],['Slope','Z',1,0,1,5,2,0.5]]
else:
    RdgInferenceInfo = []
    ShdInferenceInfo = []
    BksInferenceInfo = []
    FtsInferenceInfo = []
    VlyInferenceInfo = []

CalSecHardSlpPos = False                                ## calculate second harden slope position or not
CalSPSI = False                                         ## calculate SPSI (Slope Position Sequence Index) or not, Be Caution, only when CalSecHardSlpPos is True, CalSPSI can be True
SPSImethod = 1                                          ## only when CalSPSI is True, the SPSImethod would be used. It can be 1,2,3
DistanceExponentForIDW = 8                              ## the default is 8
