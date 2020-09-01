---
title: Mixed-Reality Testing
image: /images/projects/mixedreality.png
image_ratio: is-13by1
date: 2015-01-21
---
THis research aims to find a testing technique that reduces the consequences of unexpected or stochastic behavior when moving from simulation to reality. This is important as the unexpected behaviors are common due to both the underlying non-deterministic machine learning algorithms, and the difference in fidelity between simulation and reality.

Our research has led to the development of a technique that we call mixed-reality testing. This technique allows developers to specify the ratio of realism to simulation experienced during a test’s execution. This benefits developers as they can gradually increase the realism of tests as the development continues, thus preventing unexpected behaviors when switching directly from simulation to reality. Secondly, developers can run potentially destructive tests, such as obstacle avoidance, by only simulating the parts of the simulation, which can damage the autonomous system such as the obstacle. This mitigates the cost associated with collision due to unforeseen or stochastic behavior produced by the software running on the autonomous system.