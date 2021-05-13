---
title: Fuzzing Mobile Robot Environments for Fast Automated Crash Detection
image: /images/projects/tbd.jpeg
date: 2015-01-20
team: Andrew Elsey, Kevin Sullivan, and  Sebastian Elbaum. Contributions by multiple undergraduates
label: Foundational
---

Code drives robots, space vehicles, weapons systems, and cyber-physical systems more generally, to interact with the world. Yet in most cases, code consists of machine logic stripped of real world semantics. This means that there is no way for the computing machine to prevent operations specified in code from violating physical constraints inherited from the physical world. Traditional programming semantics can tell us that the expression, 3.0 + 4.0 means 7.0, in the sense that 7.0 is the result of evaluating that expression. But our traditional conception of programming semantics does not address the questions, 3 of what, 4 of what, or 7 of what, or whether such a sum makes any physical sense. For example 3 meters plus 4 grams does not make physical sense. Major systems malfunctions have occurred due to the machine-permitted evaluation of expressions that have no well defined physical meanings. 

To improve the safety and reliability of cyber-physical systems,  we are developing and evaluating Peirce, a software infrastructure to pair software code with interpretations that map terms in code to formal specifications of their intended physical meaning (such as points, vectors, and transformations) so that the consistency of code with the physics of the larger system can be automatically checked. Peirce takes annotated source code and, using its formalized physical types in higher-order logic of a constructive logic proof assistant, determines the consistency of those physical types usages.  We are currently targeting and evaluating Peirce on robotics programs using ROS. For example, …### Missing statements from Andrew describing figures ####

3) Picture/Diagram/Visual Element

### Missing FIGURE ####
