---
title: 'PhysCov: Physical Test Coverage for Autonomous Vehicles'
image: /images/projects/PhysCov.gif
date: 2023-07-23
team: Carl Hildebrandt, Meriel von Stein, and Sebastian Elbaum
label: Robotics
sponsor: 'This work was funded in part through NSF grants #1924777 and #1909414, and AFOSR grant #FA9550-21-1-0164.'
artifactlink: https://github.com/hildebrandt-carl/PhysicalCoverage
paperlink: https://dl.acm.org/doi/pdf/10.1145/3597926.3598069
---

Adequately exercising the behaviors of autonomous vehicles is fundamental to their validation. However, quantifying an autonomous vehicle’s testing adequacy is challenging as the system’s behavior is influenced both by its state as well as its physical environment. To address this challenge, our work builds on two insights. First, data sensed by an autonomous vehicle provides a unique spatial signature of the physical environment inputs. Second, given the vehicle’s current state, inputs residing outside the autonomous vehicle’s physically reachable regions are less relevant to its behavior. Building on those insights, we introduce an abstraction that enables the computation of a physical environment-state coverage metric, PhysCov. The abstraction combines the sensor readings with a physical reachability analysis based on the vehicle’s state and dynamics to determine the region of the environment that may affect the autonomous vehicle. It then characterizes that region through a parameterizable geometric approximation that can trade quality for cost. Tests with the same characterizations are deemed to have had similar internal states and exposed to similar environments and thus likely to exercise the same set of behaviors, while tests with distinct characterizations will increase PhysCov. A study on two simulated and one real system’s dataset examines PhysCovs’s ability to quantify an autonomous vehicle’s test suite, showcases its characterization cost and precision, investigates its correlation with failures found and potential for test selection, and assesses its ability to distinguish among real-world scenarios. We describe this in more detail in [this talk](https://www.youtube.com/watch?v=NAGcOydSh6s).