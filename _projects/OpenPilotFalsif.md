---
title: 'Determining Property Violations through Network Falsification: A Case Study of OpenPilot'
image: /images/projects/OpenPilotfalsif.png
date: 2023-07-01
team: Meriel von Stein and Sebastian Elbaum
label: DNN
sponsor: 'This work was supported in part by NSF Award #1924777 and AFOSR Award #FA9550-21-1-0164.'
artifactlink: https://github.com/MissMeriel/openpilot-falsification
paperlink: https://dl.acm.org/doi/10.1145/3551349.3559500
---

Openpilot is an open source system to assist drivers by providing features like automated lane centering and adaptive cruise control. Like most systems for autonomous vehicles, Openpilot relies on a sophisticated deep neural network (DNN) to provide its functionality, one that is susceptible to safety property violations that can lead to crashes.
To uncover such potential violations before deployment, we investigate the use of falsification, a form of directed testing that analyzes a DNN to generate an input that will cause a safety property violation. 
Specifically, we explore the application of a state-of-the-art falsifier to the DNN used in OpenPilot, which reflects recent trends in network design.
Our investigation reveals the challenges in applying such falsifiers to real-world DNNs, conveys our engineering efforts to overcome such challenges, and showcases the potential of falsifiers to detect property violations and provide  meaningful counterexamples.
Finally, we  summarize the lessons learned as well as the pending challenges for falsifiers to realize their potential on systems like OpenPilot.