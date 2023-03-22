---
title: Fuzzing Mobile Robot Environments for Fast Automated Crash Detection
image: /images/projects/Fuzzing.png
date: 2021-06-02
team: Trey Woodlief, Sebastian Elbaum, and Kevin Sullivan
label: Robotics
sponsor: 'This effort is supported by NSF Awards #1853374 and #1909414'
paperlink: https://ieeexplore.ieee.org/iel7/9560720/9560666/09561627.pdf
---

Testing mobile robots is difficult and expensive, and many faults go undetected. In this work we explore whether fuzzing, an automated test input generation technique, can more quickly find failure inducing inputs in mobile robots. We developed a simple fuzzing adaptation, Base-Fuzz, and one specialized for fuzzing mobile robots, Phys-Fuzz. Phys-Fuzz is unique in that it accounts for physical attributes such as the robot dimensions, estimated trajectories, and time-to-impact measures to guide the test input generation process. We evaluate Phys-Fuzz on a Clearpath Husky robot (above left) and find that for simple test generation scenarios as shown (above right), Phys-Fuzz has the potential to speed up the discovery of input scenarios that reveal failures, finding over 125% more than uniform random input selection and around 40% more than Base-Fuzz during 24 hours of testing. Phys-Fuzz continues to perform well in more complex scenarios, finding 56.5% more than uniform random input selection and 7.0% more than Base-Fuzz during 7 days of testing.