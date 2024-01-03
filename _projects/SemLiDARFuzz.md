---
title: 'Generating Realistic and Diverse Tests for LiDAR-Based Perception Systems'
image: /images/projects/semLiDARFuzz.png
date: 2023-5-20
team: Garrett Christian, Trey Woodlief, and Sebastian Elbaum
label: Robotics
sponsor: 'This work was supported in part by NSF Awards #1924777 and #1909414, and AFOSR Award #FA9550-21-1-0164.'
artifactlink: https://github.com/less-lab-uva/semLidarFuzz
paperlink: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10172508
---

Autonomous systems rely on a perception component to interpret their  surroundings, and when   misinterpretations occur, they can and have led to serious and fatal system-level failures. Yet, existing methods for testing  perception software remain limited in both their capacity to efficiently generate test data that translates to real-world performance and in their diversity to capture the long tail of rare but safety-critical scenarios. These limitations are particularly evident for  perception systems based on LiDAR sensors, which have emerged as a crucial component in modern autonomous systems due to their ability to provide a 3D scan of the world and operate in all lighting conditions. To address these limitations, we introduce a novel approach for testing LiDAR-based perception systems by leveraging existing real-world data as a basis to generate realistic and diverse test cases through mutations that preserve realism invariants while generating inputs rarely found in existing data sets, and automatically crafting   oracles that identify potentially safety-critical issues in perception performance. We implemented our approach to assess its ability to identify perception failures, generating over 50,000 test inputs for five state-of-the-art LiDAR-based perception systems. We found that it efficiently generated test cases that  yield errors in perception that could result in real consequences if these systems were deployed and does so at a low rate of false positives.