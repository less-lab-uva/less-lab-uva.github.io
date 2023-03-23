---
title: Measuring and Mitigating Gaps in Structural Testing
image: /images/projects/icse23-soneya.png
date: 2023-03-23
team: Soneya Binta Hossain, Matthew Dwyer, Sebastian Elbaum, Anh Nguyen-Tuong
label: Foundational
sponsor: 'This material is based in part upon work supported by the National Science Foundation under award 2129824, by the DARPA ARCOS program under contract FA8750-20-C-0507, by The Air Force Office of Scientific Research under award number FA9550-21-0164, and by Lockheed Martin Advanced Technology Laboratories.'
artifactlink: https://github.com/soneyahossain/hcc-gap-recommender
---

Code coverage is used by millions of developers in thousands of organizations on a daily basis. Despite this popularity, code coverage has well-understood limitations demonstrated by the software engineering research community, such as not providing enough insight into test oracles’ quality. In this research, we compute coverage gaps, a metric to detect the undertested program structures by analyzing the existing test oracles. We then propose a lightweight intra-procedural flow-insensitive static analysis technique that uses the system under test (SUT) and the coverage gaps as inputs to recommend actionable feedback to the developers to complement the test suite with additional test oracles, which demonstrated to improve the fault-detection effectiveness of the test suite.
