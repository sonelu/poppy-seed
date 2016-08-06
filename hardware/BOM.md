This is the list of materials that are needed for the Poppy Seed:
<table>
<tr>
<th width=25%>Part</th align=center><th>Quantity</th><th>Description</th>
</tr>
<tr><td colspan=4><b>Servomotors</b></td></tr>
<tr><td>Dynamixel XL-320</td><td align=center>25</td><td>All the motors for Poppy Seed are XL-320, a very cost effective variant of Dynamixel servomotors that have impressive capabilities in a diminutive body. Please refer to the document [Torque and design] to understand more about why they might work in this project.</td></tr>
<tr><td colspan=4><b>3D printed parts</b></td></tr>
<tr><td><i>Arms</i></td></tr>
<tr><td>Hand left</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Hand right</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Forearm left</td><td align=center>1</td><td><a href="https://github.com/sonelu/Poppy-Seed/blob/master/hardware/3d%20parts/arms/forearm%20left%20small.stl">[link to the STL]</a></td></tr>
<tr><td>Forearm right</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Upper arm</td><td align=center>2</td><td>[link to the STL]</td></tr>
<tr><td>Arm connector</td><td align=center>2</td><td>[link to the STL]</td></tr>
<tr><td>Shoulder left</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Shoulder right</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td><i>Body</i></td></tr>
<tr><td>Chest</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Spine</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Abdomen</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Dual XL mount</td><td align=center>4</td><td>[link to the STL]. Used to connect two XL servo is a 90 degrees angle.</td></tr>
<tr><td>XL idle</td><td align=center>2</td><td>[link to the STL]. Used to provide the idle support for a dual XL-320 combination.</td></tr>
<tr><td><i>Legs</i></td></tr>
<tr><td>Foot left</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Foot right</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Shin left</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Shin right</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Thigh left</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Thigh right</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Hip connector</td><td align=center>2</td><td>[link to the STL]</td></tr>
<tr><td>Hip left</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Hip right</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Pelvis</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td><i>Head</i></td></tr>
<tr><td>Head face</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Head back</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td>Spacer</td><td align=center>2</td><td>[link to the STL]</td></tr>
<tr><td>Neck</td><td align=center>1</td><td>[link to the STL]</td></tr>
<tr><td colspan=4><b>Electronics</b></td></tr>
<tr><td>Raspberry Pi 3.0</td><td align=center>1</td><td>This is the main controller for the robot. We're using the 3.0 for the WiFi</td></tr>
<tr><td>USB WiFi Dongle</td><td align=center>1</td><td>We will use the built-in WiFi for creating a hotspot this WiFi dongle to connect to an exisiting WiFi network. See more details in the [Setup] document.</td></tr>
<tr><td>Waveshare 3.5inch LCD for Raspberry Pi</td><td align=center>1</td><td>I have included this display as it is widely avaialble and seems to be decently well supported. One of the isues we might have with it is that it uses both CE0 and CE1 SPI channels and that will conflict later with the HIPI board.</td></tr>
<tr><td>Interface HAT</td><td align=center>1</td><td>In principle this should be a HIPI HAT, but until that is avaialble I have hacked together a board that includes the Dynamixel interface, 9DOF IMU and a 3A regulator. Details are in the [Interface HAT] document</td></tr>
<tr><td>Stereo Amplifier 2X3W</td><td align=center>1</td><td>Again, this should be provided by the amplifier in the HIPI board. In the meantime we use a common amplifier from Adafruit and we will mount it separately in the head</td></tr>
<tr><td>Speakers 20x40mm 3W</td><td align=center>2</td><td>Some common version of speakers. Any 20x40mm format will do as long as they also are rated 3W or more.</td></tr>
<tr><td>Raspberry Pi camera</td><td align=center>1</td><td>For image processing</td></tr>
<tr><td>Hot-swap custom board</td><td align=center>2</td><td>This is a custom board made with a very low forward voltage equivalent Schotcky chip that alows us to connect 2 LiPo batteries in parallel without having rush current and to hot-swap one battery at a time when changing them. See the [Hotswap board] for details.</td></tr>
<tr><td>XL connectors hub custom board</td><td align=center>1</td><td>For AX connectors Robotis produces a standard hub board that allows you to hook up multiple cables together. Unfortunatelly there is no equivalent board for the XL cables so I had to build one. In addition this board had 4mm fixing holes that allow it to be placed in position using normal XL rivets.</td></tr>
</table>
