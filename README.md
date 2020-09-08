# LESS Lab Website

Our lab website: https://less-lab-uva.github.io

This repository contains the site used by the Less Lab @ UVA. This site was built using [Jekyll](https://jekyllrb.com). The original sites theme is based on [bulma-clean-theme](https://github.com/chrisrhymes/bulma-clean-theme), a theme created by [C.S. Rhymes](https://dev.to/chrisrhymes). 

## Adding Information

Adding information is as easy as opening the appropriate folder (listed below) and adding a markdown file with the correct information. 

* [Team Members](./_team) :  `_team`
* [Projects](./_projects) :  `_projects`
* [Tools and Datasets](./_tools) :  `_tools`
* [Gallery Images (about section)](./_gallery) :  `_gallery`
* [Publications](./_publications) :  `_publications`

More information on what format the markdown file should be is listed under the appropriate headings below.

**Note:** We are currently working on a way to pull publications automatically. However, you can still manually add or edit your publications by editing the appropriate markdown file's content.


### Team Members

To add a team member, add your markdown file to the `_team` folder. The fields which need to be filled in are:

* **first_name**: (required) Your first name.
* **last_name**: (required) Your last name.
* **picture**: (optional) A picture of you, preferably in the folder `/images/team/`. **Note:** the image needs to be square.
* **website**: (optional) A link to your personal website.
* **dblp_uri**: (optional) A link to your dblp bib file. By adding this, we will automatically add your publications to the publications tab.
* **tier**: (required) This needs to be one of the following (Professors, Postdoctoral Students, Graduate Students, Undergraduate Students, Previous Students).

An example of a complete team member markdown file is shown below:

```markdown
---
first_name: Mary Lou
last_name: Soffa
picture: /images/team/marylou.jpg
website: www.cs.virginia.edu/~soffa/index.html%3Fp=6.html
dblp_uri: https://dblp.org/pid/s/MaryLouSoffa.bib
tier: Professors
---
```

### Projects

To add a project to the website, add a markdown file to the `_project` folder. The fields which need to be filled in are:

* **title**: (required) The title of your project.
* **image**: (optional) An image that will be displayed as a banner for your project, preferably in the folder `/images/projects/`. **Note** it is best to use an image that longer vertically than horizontally for best formatting.
* **image_ratio**: (optional) What ratio the image is, used to format the final image. Defaults to `is-3by1`. A complete list of ratios is available [here](https://bulma.io/documentation/elements/image/).
* **team**: (optional) A list of team members separated by commas.
* **date**: (required) The date your project was created in the format `YYYY-MM-DD`, used for sorting.

You can then add your project details below the data fields using the standard markdown format. For a guide on basic markdown formatting, take a look at this [link](https://www.markdownguide.org/cheat-sheet).

An example of a complete project would look as follows:

```markdown
---
title: Neural Network Verification
image: /images/projects/neural_networks.png
team: Carl Hildebrandt, Felipe Toledo
date: 2015-01-22
---

Lorem ipsum dolor sit amet.

### Subtitle

We tried to:
* create
* a
* list

This is how you make something **bold** wow!
```

### Tools and Datasets

To add a tool or dataset to the website, add a markdown file to the `_tools` folder. The fields which need to be filled in are:

* **title**: (required) The title of your tool or dataset.
* **subtitle**: (required) A subtitle for your tool or dataset. Generally used to describe what you are presenting, i.e. is it a tool, dataset, artifact?
* **image**: (optional) An image that will be displayed as a banner for your project, preferably in the folder `/images/tools/`. **Note** it is best to use an image that longer vertically than horizontally for best formatting.
* **image_ratio**: (optional) What ratio the image is, used to format the final image. Defaults to `is-3by1`. A complete list of ratios is available [here](https://bulma.io/documentation/elements/image/).
* **button_link**: (required) A link to your tool or dataset.
* **github**: (optional) A link to the GitHub repository where the tool or dataset can be found.
* **team**: (optional) A list of team members separated by commas.

You can then add your tool details below the data fields using the standard markdown format. For a guide on basic markdown formatting, take a look at this [link](https://www.markdownguide.org/cheat-sheet).


An example of a complete tool or dataset markdown file is shown below:

```markdown
---
title: Feasible and Stressful Trajectory Generation for Mobile Robots
subtitle: Tool Artifact
image: /images/tools/traj_gen.gif
description: 
button_link: https://hildebrandt-carl.github.io/RobotTestGenerationArtifact/
github: hildebrandt-carl/RobotTestGeneration
team: Carl Hildebrandt, Sebastian Elbaum, Matthew Dwyer, Nicola Bezzo
---

While executing nominal tests on mobile robots is...
```

### Gallery Images

To add a gallery image to the website, add a markdown file to the `_gallery` folder. The fields which need to be filled in are:

* **image**: (required) A link to the image you want to display, preferably in the folder `/images/gallery/`. 
* **description**: (optional) A short description of the image.
* **image_ratio**: (optional) What ratio the image is, used to format the final image. Defaults to `is-3by1`. A complete list of ratios is available [here](https://bulma.io/documentation/elements/image/).
* **date**: (required) The date your image was taken in the format `YYYY-MM-DD`, used for sorting.

An example of a complete gallery markdown file is shown below:

```markdown
---
image: /images/gallery/carltalk.jpg
description: Carl giving a talk on his recently published work on creating stressful trajectories for robots.
ratio: is-4by3
date: 2020-03-22
---
```

### Publications

We have developed a way to automatically pull your publications using the `dblp_uri` tag from your team profile. However, you can also add a publication manually. To add a publication to the website, add a markdown file to the `_publications` folder. The fields which need to be filled in are:

* **title**: (required) The title of your publication
* **date**: (required) The date your publication was published in the format `YYYY-MM-DD`.
* **venue**: (optional) The venue your publication was published in. You are able to add both HTML and markdown to this field. 
* **paperurl**: (optional) A link to your paper.
* **authors** (optional) A list of authors separated by commas.

An example of a complete publication markdown file is shown below:

```markdown
``
---
title: "At The End Of Synthesis: Narrowing Program Candidates"
date: 2017-01-01
venue: "39th IEEE/ACM International Conference on Software Engineering: New Ideas and Emerging Technologies Results Track, ICSE-NIER 2017, Buenos Aires, Argentina, May 20-28, 2017"
paperurl: https://doi.org/10.1109/ICSE-NIER.2017.7
authors: "David Shriver, Sebastian G Elbaum and Kathryn T Stolee"
---
```

## Automatically Updating Publications

To update the publications, all you need to do is run the `UpdatePublications.py` script. To do that you can run the following command in your terminal:
```bash
$ python3 UpdatePublications.py
```
