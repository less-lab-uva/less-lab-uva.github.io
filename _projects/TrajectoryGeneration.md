---
title: Feasible and Stressful Trajectory Generation for Mobile Robots
image: /images/projects/TrajectoryGeneration.gif
date: 2020-07-18
team: Carl Hildebrandt, Sebastian Elbaum, Matthew B. Dwyer, and Nicola Bezzo
label: Robotics
sponsor: 'This effort is supported by NSF Awards #1853374 and #1901769 as well as the U.S. Army Research Office Grant #W911NF-19-1-0054'
github: https://github.com/hildebrandt-carl/RobotTestGeneration
---

While executing nominal tests on mobile robots is required for their validation, such tests may overlook faults that arise under trajectories that accentuate certain aspects of the robot's behavior. Uncovering such stressful trajectories is challenging as the input space for these systems, as they move, is extremely large, and the relation between a planned trajectory and its potential to induce stress can be subtle. Additionally, each mobile robot will have a unique set of physical constraints that define how the robot can move. Thus, we need to ensure that the trajectories generated are feasible given the robot's physical constraints. This work aims at combining both a physical model of the mobile robot and a parametrizable scoring model to allow for the generation of physically valid yet stressful trajectories for mobile robots. We show an example of a stressful trajectory on the upper right where a sharp turn results in the drone overshooting its waypoint and colliding with the wall. We describe how we did this in more detail in [this talk](https://www.youtube.com/watch?v=CGzUuVX2b3k).