---
title: "Ldx: Causality Inference By Lightweight Dual Execution"
abstract: "Causality inference, such as dynamic taint anslysis, has many applications (eg, information leak detection). It determines whether an event e is causally dependent on a preceding event c during execution. We develop a new causality inference engine LDX. Given an execution, it spawns a slave execution, in which it mutates c and observes whether any change is induced at e. To preclude non-determinism, LDX couples the executions by sharing syscall outcomes. To handle path differences induced by the perturbation, we …"
date: 2016-01-01
venue: "Proceedings of the Twenty-First International Conference on Architectural Support for Programming Languages and Operating Systems, ASPLOS '16, Atlanta, GA, USA, April 2-6, 2016"
paperurl: https://dl.acm.org/doi/abs/10.1145/2872362.2872395
authors: "Yonghwi Kwon, Dohyeong Kim, William N. Sumner, Kyungtae Kim, Brendan Saltaformaggio, Xiangyu Zhang and Dongyan Xu"
awards: ""
---