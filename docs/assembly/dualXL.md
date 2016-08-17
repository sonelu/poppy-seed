# Dual XL-320 Assembly

You will need two assemblies of XL-320 in the torso: one in the upper part and one in the lower part. They provide the X-Y DOF for that part of the body. Unfortunatelly there are no standard parts from Robotis that allows the XL-320 to be mounted in a 90 degree position, so we will have to print some parts that will fulfill this scope.

The assembly instructions will apply to both the upper and lower torso, the only difference will be the IDs of the servos you will use.

To build a dual XL-320 assembly you will need:
![_DSF9023.JPG](./img/_DSF9023.JPG)

* 2 Dynamixel XL-320 preconfigured with the IDs (34, 35 for the upper torso and 31, 32 for the lower torso)
* 2 Dual XL mount 3D printed parts
* 1 Dual XL idle 3D printed part (in the picture there is an older version of the part, the one in the STL repository is slighly different, but not that much)
* 2 short XL cables: these are cables that were made from one standard 110mm XL-320 cable that was cut in two and connectors were added to the cut sides. Unlike the AX cables, Robotis does not sell cables shorter than 110mm for XL-320 and for some assemblies that is too long and can get in the way of other moving parts. We might try to see if it would be possible to produce some custom cables that can be commercialized in the future, but if you are really interested in robotics with Dynamixel servos it might be a good idea to invest in a relativelly unexpensive but reliable crimper and stripper. Alternativelly you can chose to use the standard 110mm cables instead of the shortered ones, but be careful obout how they are routed.
* 1 normal XL cable 110mm
* 1 custom made XL hub; this is the equivalent of the AX hub produced by Robotis that allows you to connect 3 cables together. Unfortunatelly there is no equvalent for XL servos, so we'll have to make it ourselved. The one you see is made on a simple strip board simply soldering 5 XL Molex connectors and adding 2 4mm holes that we will use to rivet the board in place.


