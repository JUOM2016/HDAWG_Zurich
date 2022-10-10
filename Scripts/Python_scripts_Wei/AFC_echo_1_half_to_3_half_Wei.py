# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:05:00 2022

@author: pqslab1082
"""

from measurements.libs.QPLser.AWGmanager import HDAWG_PLser
import os
import numpy as np

###  Initiliase HDAWG system  ###
device = 'dev8416'  # device ID for G14.
awgMod = HDAWG_PLser(device)
command_table=1

sampling_rate=2.4E9 # Hz; Sampling rate, should be the same as what you set on the right panel!

Number_of_burning_pulses = 499 # Number of burning pulse repetitions  
Number_of_burning_back_pulses = 300 # Number of burn-back pulse repetitions 
Number_of_cleaning_pulses = 260 # Number of clean pulse repetitions 

centre_freq_burning=250E6; #Hz; Central frequency set to drive the AOM for burning 
#chirpAmplitude_burning = 0; # V; amplitude of burning pulse 
chirpAmplitude_burning = 0.15; # V; amplitude of burning pulse 
freq_sweeping_burning=3.5E6 # Hz; set the scanning frequency range of burning pulse (the actual scanning range should be 4*freq_detuning)
burning_duration=0.2e-3; # s; burning time 

centre_freq_burning_back=263.75E6; # Hz; Central frequency set to drive the AOM for burn-back
chirpAmplitude_burning_back = 0; # V; amplitude of burn-back
#chirpAmplitude_burning_back = 0.078; # V; amplitude of burn-back
freq_sweeping_burning_back=0.85e6; # Hz; set the scanning frequency range of burn-back (the actual scanning range should be 4*freq_detuning)
burning_back_duration=0.02e-3; # s; burning time burn-back

centre_freq_cleaning=252.7E6 # Hz; Central frequency set to drive the AOM for cleaning
chirpAmplitude_cleaning = 0 #  V; amplitude of cleaning
#chirpAmplitude_cleaning = 0.065 #  V; amplitude of cleaning
freq_sweeping_cleaning=1E6 # Hz; set the scanning frequency range of cleaning (the actual scanning range should be 4*freq_detuning)
cleaning_duration=0.1e-3 # s; burning time cleaning

centre_freq_shuffle=250E6; # Hz; Central frequency of the shuffle pulse
chirpAmplitude_shuffle = 0.21; # V; amplitude of shuffling pulse
freq_sweeping_shuffle=20E6; # Hz; set the scanning frequency range of shuffling pulse
shuffle_duration=3e-3; # s; shuffling time

Number_of_AFC_pulses = 75 # Repetition of AFC preparation pulses
centre_freq_AFC=247.6E6 # Centre frequency of AFC preparation pulses
amplitude_AFC=0.0
#amplitude_AFC=0.052 # Amplitude of AFC preparation pulses
AFC_width=4E6 # width of created AFC
num_of_AFC_holes=7 # Number of holes burnt ti generate the AFC
AFC_pulse_duration = 0.005e-3 # Pulse duration of AFC preparation pulses

centre_freq_AFC_echo_sine=247.6E6 # Centre frequency of input pulse
amplitude_AFC_echo=0.05 # Amplitude of input pulse
pulse_duration_AFC_echo=3E-6 # Full pulse duration of input pulse
gauss_pulse_width=600E-9 # FMHW of input pulse

#############*****************Create Command Table***********************############################################# 
if command_table==1:
    ### Save Location ###
    save_directory = 'C:/Codes/measurements/libs/QPLser/ZI_HDAWG_Scripts/Command_Tables/'
    ### file name ###
    file_name= 'CT_AFC_echo_1_half_to_3_half_Wei'
    ### Open the file ###
    f = open(os.path.join(save_directory+ file_name), 'w')
    ### Write the basic intro of the file ###
    f.write('{' + '\n' + '  '
        '"$schema": "http://docs.zhinst.com/hdawg/commandtable/v2/schema",' + '\n' + '  '
        '"header": {' + '\n' + '\t' + '"version": "0.2",' + '\n' + '\t' 
        '"UserString": "' + file_name + '",' + '\n' + '\t'  + '"partial": true,' + '\n' + '\t'  + '"description": "Command table for T2 measurement"' +  '\n' + '  },' + '\n'
        '  "table": [' + '\n')
### Write the index assigning ###
    a=np.arange(0,num_of_AFC_holes)
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
#############**********************************************************############################################# 

## Load correct Sequence file
HDAWG_filename = ('C:\Codes\HDAWG\Sequences\AFC_echo_1_half_to_3_half_Wei.txt')

with open(HDAWG_filename, "r") as file:
    awg_string = file.read()
    awg_program = awg_string.format(
        sampling_rate=sampling_rate, # Hz; Sampling rate, should be the same as what you set on the right panel!
        Number_of_burning_pulses =Number_of_burning_pulses,
        Number_of_burning_back_pulses =Number_of_burning_back_pulses,
        Number_of_cleaning_pulses=Number_of_cleaning_pulses,
        centre_freq_burning=centre_freq_burning, #Hz; Central frequency set to drive the AOM for burning 
        chirpAmplitude_burning=chirpAmplitude_burning, # V; amplitude of burning pulse 
        freq_sweeping_burning=freq_sweeping_burning, # Hz; set the scanning frequency range of burning pulse (the actual scanning range should be 4*freq_detuning)
        burning_duration=burning_duration, #s; burning time  
        centre_freq_burning_back=centre_freq_burning_back, # Hz; Central frequency set to drive the AOM for burn-back  
        chirpAmplitude_burning_back = chirpAmplitude_burning_back, # V; amplitude of burn-back
        freq_sweeping_burning_back=freq_sweeping_burning_back, #Hz; set the scanning frequency range of burn-back (the actual scanning range should be 4*freq_detuning)
        burning_back_duration=burning_back_duration, #s; burning time burn-back
        centre_freq_cleaning=centre_freq_cleaning,
        chirpAmplitude_cleaning=chirpAmplitude_cleaning,
        freq_sweeping_cleaning=freq_sweeping_cleaning,
        cleaning_duration=cleaning_duration,
        centre_freq_shuffle=centre_freq_shuffle, #Hz; Central frequency of the shuffle pulse
        chirpAmplitude_shuffle = chirpAmplitude_shuffle,# V; amplitude of shuffling pulse
        freq_sweeping_shuffle=freq_sweeping_shuffle, #Hz; set the scanning frequency range of shuffling pulse
        shuffle_duration=shuffle_duration, #s; shuffling time
        AFC_width=AFC_width,
        num_of_AFC_holes=num_of_AFC_holes,
        amplitude_AFC=amplitude_AFC,
        AFC_pulse_duration=AFC_pulse_duration,
        Number_of_AFC_pulses=Number_of_AFC_pulses,
        centre_freq_AFC=centre_freq_AFC,
        amplitude_AFC_echo=amplitude_AFC_echo,
        pulse_duration_AFC_echo=pulse_duration_AFC_echo,
        centre_freq_AFC_echo_sine=centre_freq_AFC_echo_sine,
        gauss_pulse_width=gauss_pulse_width,
        
        )
    
awgMod.compile(device, awg_program)
awgMod.upload_command_table(device, command_table='CT_AFC_echo_1_half_to_3_half_Wei')

### Set HDAWG parameters/settings ###

awgMod.set_value(f"/{device}/sines/0/enables/0", 0)

awgMod.set_value(f"/{device}/triggers/out/0/source", 0) # set up trigger, Output 1 Marker 1

## setup output channels 
awgMod.set_value(f"/{device}/sigouts/0/on", 1) # Channel 1 is ON
awgMod.set_value(f"/{device}/sigouts/1/on", 0)
awgMod.set_value(f"/{device}/sigouts/2/on", 0)
awgMod.set_value(f"/{device}/sigouts/3/on", 0)

awgMod.set_value(f"/{device}/awgs/0/single",0) #Rerun sequence