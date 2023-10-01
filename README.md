# Sound Monitor (WIP)

SoundMonitor was born out of my need to track the volume level coming from my children's bedroom while I worked or gamed
on my PC in my office on the other side of the house. Due to my wife being responsible for the kids during the day, we 
agreed that I would be mainly responsible for responding to wake-ups during the night. Often I stay up later than my wife
to do personal projects, respond to pages when on-call, and gaming. Thus, I hit the problem of wanting to wear headphones
while also still being able to know if my children made noise.

I came up with the idea of running a small lavalier microphone to my children's bedroom, with an extension cord all the 
way back to my PC, thus having a way to directly track the volume level in their bedroom. You'll need to have something 
along these lines if you want to use this program in the same way.

Running `latest_live_microphone_levels.py` will present the GUI below, which tracks the volume coming from the chosen 
microphone, much like an earthquake monitor.

(screenshot)

This has been designed for putting onto a secondary PC monitor, so that I can work on my primary monitor, and my peripheral
vision picks up any sudden spikes in the graph.

This is the MVP (minimum viable product) for my use-case. I might improve it eventually, adding a way to choose the 
microphone via the GUI, and potentially features like setting the threshold for the volume, the length of time the graph
represents, etc.

*Disclaimer*  
I am far from being an expert in audio, so all the calculations used are just my best guess at what is appropriate, based
on a number of hours of research and then testing what produces an understandable graph. Keep in mind that this is also
based on the microphone that I'm using, so if you use this with different equipment you may want to adjust the calculations.

---
## Usage

The ID of the microphone to use is currently hard-coded, as this is enough for my use-case. The first step is to run 
`get_audio_devices.py`, which returns a list of the device names and their ID's.

Find the ID of the microphone you want to use and then change the DEVICE_ID parameter on line 14 in 
`latest_live_microphone_levels.py`.

Then run `latest_live_microphone_levels.py` to see the current volume levels coming from the microphone.

---
Secondarily to the GUI generally working pretty well, I've discovered that sometimes I'm too focused to notice spikes in 
the graph, so I found out how to pipe the sound from the microphone directly into my headphones, alongside whatever other 
sounds I'm listening to. Instructions on how to do this can be found 
[here](https://www.addictivetips.com/windows-tips/output-mic-sound-to-speakers-windows-10/). 

You may also want to consider digitally boosting the volume level of the microphone, you might be surprised how much this
can compensate when using a tiny cheap lavalier microphone. See 
[here](https://www.lifewire.com/increase-mic-volume-on-windows-10-5180856) for how to do that.