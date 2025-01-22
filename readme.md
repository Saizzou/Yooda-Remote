<div align="center">
<h1 align="center">Yooda Remote</h1>
  <h2 align="center">Wiring</h2>
<img align="center" alt="Diagramm" src="Diagramm.png" >
</div>
<br>
<br />

# Info
This is my Setup to Use my Yooda Shutter Remote with Home Assistant at home. There is a Network Remote official from Yooda which is much more expensive tho. 

I used an 8 Port Relay, but you don't have to you can also use a 4 Port Relay. You could expand the Project if you can solder better than me, you also can add the "Stop" and the "Right" Button and use them with Relay 24 and 4. But be careful when soldering the "Right" Button because you can harm the Remote very easily!

## You need:
1- A Raspberry Pi 3,4,5 or Zero

2- A Relay Module 4/8 

3- Some Jumper Cables

4- Know How to Solder the Remote Wires

5- SSH Access to your Raspberry Pi

*6 - Optional : SSH Command for Home Assistant -> https://github.com/AlexxIT/SSHCommand 

*7 - Optional : Add Buttons which Trigger SSH Command (SSHCommand needs sudo when you trigger remotely the Raspberry Pi)

## Run it with

`python ./yooda-remote.py [remote Nr 0-15] [open|close]`


## Extend the Project (IDEAS)
I think the whole system could be done with an ESP32 or ESP8266 which is way more cheaper than using a Raspberry. Also it would be much compacter. I will give it a try oneday but for now my Home Assistant is working very well!

<div align="center">
  <h2 align="center">My Home Assistant Example</h2>
<img align="center" alt="Diagramm" src="HA-with Yooda-Remote" >
</div>
