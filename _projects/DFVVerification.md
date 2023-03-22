---
title: "Distribution Models for Falsification and Verification of DNNs"
image:   /images/projects/DFVVerification.svg
image_ratio: is-4by1
date: 2021-07-7
team: Felipe Toledo, David Shriver, Sebastian Elbaum, and Matthew B. Dwyer 
label: DNN
sponsor: 'This effort is supported by NSF Awards #1900676 and #2019239'
artifactlink: https://github.com/less-lab-uva/DFV-Artifact
paperlink: https://ieeexplore.ieee.org/iel7/9678507/9678392/09678590.pdf
---

DNN validation and verification approaches that are input distribution agnostic waste effort on irrelevant inputs and report  false  property  violations.  Drawing  on  the  large  body  of work  on  model-based  validation  and  verification  of  traditional systems, we introduce the first approach that leverages environmental models to focus DNN falsification and verification on the relevant  input  space.  Our  approach,  DFV,  automatically  builds an input distribution model using unsupervised learning, prefixes that  model  to  the  DNN  to  force  all  inputs  to  come  from  the learned distribution, and reformulates the property to the input space  of  the  distribution  model.  This  transformed  verification problem allows existing DNN falsification and verification tools to target the input distribution – avoiding consideration of infeasible inputs.