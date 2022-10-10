# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:17:59 2022

@author: pqslab1082
"""
"""
The pulse sequence firstly prepared the absorption features for the transition of 1/2g --> 1/2e, and then
perform the T2 measurement for the transition
"""
from measurements.libs.QPLser.AWGmanager import HDAWG_PLser

###  Initiliase HDAWG system  ###
device = 'dev8416'  # device ID for G14.
awgMod = HDAWG_PLser(device)

sampling_rate=2.4E9 # Hz; Sampling rate, should be the same as what you set on the right panel!
ClockCycle = 1/(3.3333e-9) #Time length of one clock cycle -- wait command

## HDAWG parameters for pulse sequency 
Number_of_burning_pulses = 299 # Number of burning pulse repetitions  
Number_of_burning_back_pulses = 200 # Number of burn-back pulse repetitions 

centre_freq_burning=250E6 #Hz; Central frequency set to drive the AOM for burning 
chirpAmplitude_burning = 0.1 # V; amplitude of burning pulse 
freq_sweeping_burning=3E6 # Hz; set the scanning frequency range of burning pulse (the actual scanning range should be 4*freq_detuning)
burning_duration=0.6E-3 #s; burning time 

centre_freq_burning_back=268.45E6 # Hz; Central frequency set to drive the AOM for burn-back, 1/2g --> 1/2e
chirpAmplitude_burning_back = 0.025 # V; amplitude of burn-back
freq_sweeping_burning_back=0.7E6 #Hz; set the scanning frequency range of burn-back (the actual scanning range should be 4*freq_detuning)
burning_back_duration=0.1E-3 #s; burning time burn-back

centre_freq_pi=250E6 #Hz; Central frequency set to drive the AOM for pi/2 and pi pulses
pi_pulse_duration=4.0E-6 #s; Pulse duration of pi pulse
amplitude_half_pi = 0.066 # V; amplitude of pi/2 pulse
amplitude_pi = 0.066 # V; amplitude of pi pulse

centre_freq_shuffle=250E6#Hz; Central frequency of the shuffle pulse
chirpAmplitude_shuffle = 0.21 # V; amplitude of shuffling pulse
freq_sweeping_shuffle=10E6 #Hz; set the scanning frequency range of shuffling pulse
shuffle_duration=500e-6 #s; shuffling time

tau_0=11e-6 # s; first time delay between pi/2 and pi pulses
echo_width=3E-6 

### Load correct Sequence file ###
HDAWG_filename = ('C:\Codes\HDAWG\Sequences\T2_measurement_single_1to1_Wei.txt')

with open(HDAWG_filename, "r") as file:
    awg_string = file.read()
    awg_program = awg_string.format(
        sampling_rate=sampling_rate, # Hz; Sampling rate, should be the same as what you set on the right panel!
        ClockCycle = ClockCycle, #Time length of one clock cycle -- wait command
        Number_of_burning_pulses =Number_of_burning_pulses,
        Number_of_burning_back_pulses =Number_of_burning_back_pulses,
        centre_freq_burning=centre_freq_burning, #Hz; Central frequency set to drive the AOM for burning 
        chirpAmplitude_burning=chirpAmplitude_burning, # V; amplitude of burning pulse 
        freq_sweeping_burning=freq_sweeping_burning, # Hz; set the scanning frequency range of burning pulse (the actual scanning range should be 4*freq_detuning)
        burning_duration=burning_duration, #s; burning time  
        centre_freq_burning_back=centre_freq_burning_back, # Hz; Central frequency set to drive the AOM for burn-back  
        chirpAmplitude_burning_back = chirpAmplitude_burning_back, # V; amplitude of burn-back
        freq_sweeping_burning_back=freq_sweeping_burning_back, #Hz; set the scanning frequency range of burn-back (the actual scanning range should be 4*freq_detuning)
        burning_back_duration=burning_back_duration, #s; burning time burn-back
        centre_freq_pi=centre_freq_pi, #Hz; Central frequency set to drive the AOM for pi/2 and pi pulses
        pi_pulse_duration=pi_pulse_duration, #s; Pulse duration of pi pulse       
        amplitude_half_pi = amplitude_half_pi, # V; amplitude of pi/2 pulse
        amplitude_pi = amplitude_pi, # V; amplitude of pi pulse
        centre_freq_shuffle=centre_freq_shuffle, #Hz; Central frequency of the shuffle pulse
        chirpAmplitude_shuffle = chirpAmplitude_shuffle,# V; amplitude of shuffling pulse
        freq_sweeping_shuffle=freq_sweeping_shuffle, #Hz; set the scanning frequency range of shuffling pulse
        shuffle_duration=shuffle_duration, #s; shuffling time
        tau_0=tau_0, # s; first time delay between pi/2 and pi pulses
        echo_width=echo_width
        )
    
awgMod.compile(device, awg_program)

## Set HDAWG parameters/settings

## setup output channels 
awgMod.set_value(f"/{device}/sigouts/0/on", 1) # Channel 1 is ON
awgMod.set_value(f"/{device}/sigouts/1/on", 0)
awgMod.set_value(f"/{device}/sigouts/2/on", 0)
awgMod.set_value(f"/{device}/sigouts/3/on", 0)

awgMod.set_value(f"/{device}/sines/0/enables/0", 0)

awgMod.set_value(f"/{device}/system/awg/oscillatorcontrol", 0) # AWG Oscillator Control is OFF

#awgMod.set_value(f"/{device}/awg/enable", 1)
awgMod.set_value(f"/{device}/awgs/0/single",0) #Rerun sequence

awgMod.set_value(f"/{device}/triggers/out/0/source", 0) # set up trigger, AWG trigger 1
