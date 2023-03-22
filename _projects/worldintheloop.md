---
title: World in the Loop Simulation
image: /images/projects/MixedReality.gif
date: 2021-06-01
team: Carl Hildebrandt and Sebastian Elbaum
label: Robotics
sponsor: 'This effort is supported by NSF Awards #1853374 and #1924777'
artifactlink: https://github.com/hildebrandt-carl/MixedRealityTesting
paperlink: https://ieeexplore.ieee.org/iel7/9560720/9560666/09561240.pdf
---

Simulation is at the core of validating autonomous systems (AS), enabling the detection of faults at a lower cost and earlier in the development life cycle. However, simulation can only produce an approximation of the real world, leading to a gap between simulation and reality where undesirable system behaviors can go unnoticed. To address that gap, we present a novel approach, world-in-the-loop (WIL) simulation, which integrates sensing data from simulation and the real world to provide the AS with a mixed reality. WIL allows varying amounts of simulation and reality to be used when generating mixed reality. For example, in the figure above, the mixed reality is using the real world camera data with a simulated gate overlayed into the real world. Additionally, you can see that using WIL, we can detect bugs with a low cost of failure, as the drone collides with the gate at no physical cost to the drone. We are working on ways to expand this mixed reality with additional sensors, environments, and forces.