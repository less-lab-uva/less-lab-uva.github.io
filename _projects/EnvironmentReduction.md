---
title: Automated Environment Reduction for Debugging Robotic Systems
image: /images/projects/EnvironmentReduction.png
date: 2021-06-03
team: Meriel Stein and Sebastian Elbaum
label: Robotics
sponsor: 'This effort is supported by NSF Awards #1853374 and #1924777'
artifactlink: https://github.com/MissMeriel/DDEnv
paperlink: https://ieeexplore.ieee.org/iel7/9560720/9560666/09561997.pdf
---

Complex environments can cause robots to fail. Identifying the key elements of the environment associated with such failures is critical for a faster fault isolation and, ultimately, debugging those failures. In this work we present the first automated approach for reducing the environment in which a robot failed. Similar to software debugging techniques, our approach systematically performs a partitioning of the environment space causing a failure, executes the robot in each partition containing a reduced environment according to an ordering heuristic, and further partitions reduced environments that still lead to that same failure as in the original world. The technique is novel in the spatial-temporal partition strategies it employs to partition and order, and in how it manages the potential different robot behaviors occurring under the same environments. Our study of a ground robot on three failure scenarios (shown above) finds that environment reductions of over 95% are achievable within a 2-hour window.
