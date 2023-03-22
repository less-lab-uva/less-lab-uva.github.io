---
title: Mimicking Real Forces on a Drone Through a Haptic Suit to Enable Cost-Effective Validation
image: /images/projects/HapticSuit.png
date: 2023-05-29
team: Carl Hildebrandt, Wen Ying, Seongkook Heo, and Sebastian Elbaum
label: Robotics
sponsor: 'This work was funded in part through NSF grants #1924777 and AFOSR grant #FA9550-21-1-0164.'
---

Robots operate under certain forces that affect their behavior. For example, a drone meant to deliver packages must hold its pose as long as it operates under its weight and wind limits. Validating that such a drone handles external forces correctly is key to ensuring its safety. Nevertheless, validating the system's behavior under the effect of such forces can be difficult and costly. For example, checking the effects of different wind magnitudes may require waiting for the matching outdoor conditions or building specialized devices like wind tunnels. Checking the effects of different package sizes and shapes may require many slow and laborious iterations, and validating the combinations of wind gusts and package configurations is often hard to replicate. This work aims to overcome such challenges by mimicking external forces exercised on a drone with limited cost, setup, and space. The framework consists of a haptic suit device consisting of directional propellers that can be mounted onto a drone, a component to transform intended forces into setpoints for the suit's directional propellers, and a controller for the suit to meet those setpoints. We describe this in more detail in [this talk](https://www.youtube.com/watch?v=5_QmRLWMhes).