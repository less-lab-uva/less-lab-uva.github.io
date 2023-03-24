---
title: "Input Distribution Coverage: Measuring Feature Interaction Adequacy in Neural Network Testing"
image: /images/projects/IDC.png
date: 2022-12-12
team: Swaroopa Dola, Matthew B. Dwyer, and Mary Lou Soffa
label: DNN
sponsor: 'This effort is supported by NSF Awards #2019239 and #2129824, by The Air Force Office of Scientiic Research under award #FA9550-21-0164, and by Lockheed Martin Advanced Technology Laboratories'
paperlink: https://dl.acm.org/doi/pdf/10.1145/3576040
artifactlink: https://github.com/less-lab-uva/InputDistributionCoverage
---

Input Distribution Coverage (IDC) is a framework for measuring the test adequacy of neural networks. IDC rejects invalid inputs and converts the valid inputs into feature vectors, which represent the feature abstractions of the test inputs in a low-dimensional space. IDC applies combinatorial interaction testing measures over the space of the feature vectors to measure test coverage. Experimental studies demonstrate that the test adequacy measures calculated by IDC capture the feature interactions present in the test suites.