---
title: Fuzzing Mobile Robot Environments for Fast Automated Crash Detection
image: /images/projects/Simplego-to-goalscenario
date: 2015-01-20
team: Trey Woodlief, Sebastian Elbaum, Kevin Sullivan
label: Robotics
---

<a name="FuzzingRobots"></a>

Testing mobile robots is difficult and expensive, and many faults go undetected. In this work we explore whether fuzzing, an automated test input generation technique, can more quickly find failure inducing inputs in mobile robots. We developed a simple fuzzing adaptation, Base-Fuzz, and one specialized for fuzzing mobile robots, Phys-Fuzz. Phys-Fuzz is unique in that it accounts for physical attributes such as the robot dimensions, estimated trajectories, and time-to-impact measures to guide the test input generation process. We evaluate Phys-Fuzz on a Clearpath Husky robot (figure a) and find that for simple test generation scenarios as shown below (figure b), Phys-Fuzz has the potential to speed up the discovery of input scenarios that reveal failures, finding over 125% more than uniform random input selection and around 40% more than Base-Fuzz during 24 hours of testing (figure c). Phys-Fuzz continues to perform well in more complex scenarios, finding 56.5% more than uniform random input selection and 7.0% more than Base-Fuzz during 7 days of testing. 

### pointer to video ? ##

** This effort is supported by NSF grants **