import os
import numpy as np


### Save Location ###
save_directory = 'C:/Codes/measurements/libs/QPLser/ZI_HDAWG_Scripts/Command_Tables/'


### file name ###

file_name= 'CT_AFC_1_half_to_3_half_Wei'


### Open the file ###
f = open(os.path.join(save_directory+ file_name), 'w')

### Write the basic intro of the file ###
f.write('{' + '\n' + '  '
        '"$schema": "http://docs.zhinst.com/hdawg/commandtable/v2/schema",' + '\n' + '  '
        '"header": {' + '\n' + '\t' + '"version": "0.2",' + '\n' + '\t' 
        '"UserString": "' + file_name + '",' + '\n' + '\t'  + '"partial": true,' + '\n' + '\t'  + '"description": "Command table for T2 measurement"' +  '\n' + '  },' + '\n'
        '  "table": [' + '\n')

### Write the index assigning ###
a=np.arange(0,8)
for i in range(0, len(a)):
    f.write('\t'+'{' + '\n'
          + '\t' + '  "index":'+str( i)+',' + '\n'
          + '\t' + '  "waveform": {' + '\n'
          + '\t' + '  "index":'+str( i) + '\n'
          + '\t' + '    }'
        )
    if i==len(a)-1:
        f.write('\t' + '}' + '\n')
    else:
        f.write('\t' + '},' + '\n')

### end parenthesis ###
f.write('  ]' + '\n' + '}')
### close the file###
f.close()