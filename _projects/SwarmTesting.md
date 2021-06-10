---
title: Testing Drone Swarm for Configuration Bugs
image: /images/projects/SwarmTesting.png
date: 2021-03-11
team: Chijung Jung, Sebastian Elbaum, and Yonghwi Kwon
label: Robotics
---

Swarm robotics collectively solve problems that are challenging for individual robots, from environmental monitoring to entertainment. The algorithms enabling swarms allow individual robots of the swarm to plan, share, and coordinate their trajectories and tasks to achieve a common goal. Such algorithms rely on a large number of configurable parameters that can be tailored to target particular scenarios. This large configuration space, the complexity of the algorithms, and the dependencies with the robots’ setup and performance make debugging and fixing swarms configuration bugs extremely challenging.

This project proposes Swarmbug, a swarm debugging system that automatically diagnoses and fixes buggy behaviors caused by misconfiguration (e.g., crashes in 4 swarm algorithms shown in the Figure). The essence of Swarmbug is the novel concept called the degree of causal contribution (Dcc), which abstracts impacts of environment configurations (e.g., obstacles) to the drones in a swarm via behavior causal analysis. Swarmbug automatically generates, validates, and ranks fixes for configuration bugs. We evaluate Swarmbug on four diverse swarm algorithms. Swarmbug successfully fixes four configuration bugs in the evaluated algorithms, showing that it is generic and effective. We also conduct a real-world experiment with physical drones to show the Swarmbug’s fix is effective in the real-world.

This figure shows buggy behaviors in four swarm algorithms: (a) drone crashes into dynamic obstacle (black square), (b) drones crash into the static obstacle (octagon), (c) drone moves to unsafe zone (red box), and (d) drone (green sphere) crashes into the static obstacle (red sphere).