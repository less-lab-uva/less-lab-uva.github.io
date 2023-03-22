---
title: Improving Software Engineering Tools Via SMT Selection 
image: /images/projects/sibyl_pipeline.png
date: 2023-03-22
team: Will Leeson, Matthew B. Dwyer, and Antonio Filieri
label: Foundational
sponsor: 'This material is based in part upon work supported by the National Science Foundation under award 2129824, by the DARPA ARCOS program under contract FA8750-20-C-0507, by The Air Force Office of Scientific Research under award number FA9550-21-0164, and by Lockheed Martin Advanced Technology Laboratories.'
artifactlink: https://github.com/will-leeson/sibyl
---

SMT solvers are often used in the back end of different software engineering tools---e.g., program verifiers, test generators, or program synthesizers. There are a plethora of algorithmic techniques for solving SMT queries. Among the available SMT solvers, each employs its own combination of algorithmic techniques that are optimized for different fragments of logics and problem types. The most efficient solver can change with small changes in the SMT query, which makes it nontrivial to decide which solver to use. Consequently, designers of software engineering tools often select a single solver, based on familiarity or convenience, and tailor their tool towards it. Choosing an SMT solver at design time misses the opportunity to optimize query solve times and, for tools where SMT solving is a bottleneck, the performance loss can be significant.

In this work, we present Sibyl, an automated SMT selector based on graph neural networks (GNNs). Sibyl creates a graph representation of a given SMT query and uses GNNs to predict how each solver in a suite of SMT solvers would perform on said query. Sibyl learns to predict based on features of SMT queries that are specific to the population on which it is trained -- avoiding the need for manual feature engineering. Once trained, Sibyl makes fast and accurate predictions which can substantially reduce the time needed to solve a set of SMT queries.