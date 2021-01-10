---
title: "DNNF: Deep Neural Network Falsification"
subtitle: Tool
image: /images/tools/dnnf.png
image_ratio: is-3by1
team: David Shriver, Sebastian Elbaum, Matthew Dwyer
github: dlshriver/DNNF
button_link: https://github.com/dlshriver/DNNF
---

DNNF is a framework for falsification of deep neural networks (DNN).
While many DNN verification techniques have been introduced in the past few years to enable the checking of DNN safety properties, these techniques are often limited in their applicability, due to simplifying assumptions about DNN structure or to high computational cost.
Falsification is a complementary approach to verification that seeks only to find violations to a safety property.
In the context of DNNs, adversarial attacks can be viewed as falsifiers for DNN local robustness properties.
While these techniques often scale to large real-world DNNs, they are currently limited in the range of properties they can falsify.
In <i>Reducing DNN Properties to Enable Falsification with Adversarial Attacks</i>, we introduce an approach for reducing a DNN and an associated safety property -- a correctness problem -- into an equivalid set of correctness problems formulated with robustness properties which can be processed by existing adversarial attack techniques.
DNNF is the implementation of that approach.
