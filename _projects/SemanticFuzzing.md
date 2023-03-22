---
title: Semantic Image Fuzzing of AI Perception Systems
image: /images/projects/semantic_fuzzing.png
date: 2022-05-27
team: Trey Woodlief, Sebastian Elbaum, and Kevin Sullivan
label: Robotics
sponsor: 'This effort is supported by NSF Awards #1924777 and #190941'
paperlink: https://dl.acm.org/doi/pdf/10.1145/3510003.3510212
---

Perception systems enable autonomous systems to interpret raw sensor readings of the physical world. Testing of perception systems aims to reveal misinterpretations that could cause system failures.
Current testing methods, however, are inadequate. The cost of human interpretation and annotation of real-world input data is high, so manual test suites tend to be small. The simulation-reality gap reduces the validity of test results based on simulated worlds. And methods for synthesizing test inputs do not provide corresponding expected interpretations. To address these limitations, we developed _semSensFuzz_, a new approach to fuzz testing of perception systems based on semantic mutation of test cases that pair real-world sensor readings with their ground-truth interpretations. We implemented our approach to assess its feasibility and potential to improve software testing for perception systems. We used it to generate 150,000 semantically mutated image inputs for five state-of-the-art perception systems. We found that it synthesized tests with novel and subjectively realistic image inputs, and that it discovered inputs that revealed significant inconsistencies between the specified and computed interpretations. We also found that it produced such test cases at a cost that was very low compared to that of manual semantic annotation of real-world images.