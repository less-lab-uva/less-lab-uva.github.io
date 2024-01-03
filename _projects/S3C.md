---
title: 'S<sup>3</sup>C: Spatial Semantic Scene Coverage for Autonomous Vehicles'
image: /images/projects/s3c.png
date: 2024-4-20
team: Trey Woodlief, Felipe Toledo, Sebastian Elbaum, and Matthew B Dwyer
label: Robotics
sponsor: 'This work was supported in part by NSF Awards #2129824 and #2312487, and AFOSR Award #FA9550-21-1-0164.'
artifactlink: https://github.com/less-lab-uva/s3c
paperlink: https://github.com/less-lab-uva/s3c/blob/main/S3C%20Spatial%20Semantic%20Scene%20Coverage%20for%20Autonomous%20Vehicles.pdf
---

Autonomous vehicles (AVs)  must be able to operate in a wide range of scenarios including those in the <i>long tail</i> distribution that include rare but safety-critical events.
The collection of sensor input and expected output datasets from such scenarios is crucial for the development and testing of such systems.
Yet, approaches to quantify the extent to which a dataset covers test specifications that capture critical scenarios remain limited in their ability to discriminate between inputs that lead to distinct behaviors, and to render interpretations that are relevant to AV domain experts.
To address  this challenge, we introduce S<sup>3</sup>C, a framework that abstracts sensor inputs to coverage domains that account for the <i>spatial semantics</i> of a scene. The approach
leverages scene graphs to produce a sensor-independent abstraction of the AV environment that is interpretable and discriminating.
We provide an implementation of the approach and a study for camera-based autonomous vehicles operating in simulation. The findings show that S<sup>3</sup>C outperforms existing techniques in  discriminating among classes of inputs that cause failures, and offers spatial interpretations that can explain to what extent a dataset covers a test specification. Further exploration of S<sup>3</sup>C with open datasets complements the study findings,  revealing the potential and shortcomings of deploying the approach in the wild.
