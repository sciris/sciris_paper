---
title: 'Sciris: A cohesive Python library to enable efficient and sustainable development of domain-specific research applications. '
tags:
  - python
  - scientific software development
  - computational science
authors:
  - name: Cliff C. Kerr
    orcid: 0000-0003-2517-2354
    corresponding: true
    affiliation: 1 
  - name: Paula Sanz-Leon
    orcid: 0000-0002-1545-6380
    affiliation: 1
  - name: Romesh G. Abeysuriya
    orcid: 0000-0002-9618-6457
    affiliation: "1, 2"
  - name: George L. Chadderdon
    orcid: 0000-0002-3034-2330
    affiliation: 3
  - name: Vlad-Ştefan Harbuz
    affiliation: 3
  - name: Parham Saidi
    affiliation: 3  
  - name: James Jansson
    affiliation: 3
  - name: Maria del Mar Quiroga
    orcid: 0000-0002-8943-2808
    affiliation: 3
  - name: Rowan Martin-Hughes
    orcid: 0000-0002-3724-2412
    affiliation: 3
  - name: Sherrie Kelly
    orcid: Sherrie Kelly
    affiliation: 3
  - name: Jamie A. Cohen
    orcid: 0000-0002-8479-1860
    affiliation: 3
  - name: Robyn M. Stuart
    orcid: 0000-0001-6867-9265
    affiliation: 3
  - name: Anna Nachesa
    affiliation: 3

affiliations:
 - name: Institute for Disease Modeling, Global Health Division, Bill \& Melinda Gates Foundation, Seattle, USA
   index: 1
 - name: Burnet Institute, Melbourne, Victoria, Australia 
   index: 2
 - name: Affiliation TBC by author
   index: 3
date: 21 September
bibliography: paper.bib

# JOSS required sections
# A list of the authors of the software and their affiliations, using the correct format 

# A summary describing the high-level functionality and purpose of the software for a diverse, non-specialist audience.

# A Statement of need section that clearly illustrates the research purpose of the software and places it in the context of related work.

# A list of key references, including to other software addressing related needs. Note that the references should include full names of venues, e.g., journals and conferences, not abbreviations only understood in the context of a specific discipline.

# Mention (if applicable) a representative set of past or ongoing research projects using the software and recent scholarly publications enabled by it.

# Acknowledgement of any financial support.

---

# Summary
Sciris is a cohesive collection of tools that enables an easy and simple
interaction with foundational libraries from the scientific Python ecosytem
(e.g., `numpy`, `scipy`, and `matplotlib`), as well as with libraries with
broader scope such as `multiprocessing` and `pickle`. Sciris purpose is the
facilitation and acceleration of the development and delivery process of
easy-to-use domain-specific scientific software. This has been achieved by
creating classes and methods that simplify interfaces to frequently used
supporting functionality,  which is essential for the development of robust
software applications, but may divert the focus from the actual problem to be
solved. Some of Sciris key features include: ensuring consistent dictionary,
list, and array types(e.g., this would enable users to provide inputs to a
class or method as either lists or arrays); enabling referencing ordered
dictionary elements by index; simplifying datetime arithmetic by allowing
users to provide either a date string or a datetime object; simplifying the
saving and loading of files and complex objects; and, simplifying the
parallelisation of common operations. Sciris makes writing scientific code in
Python faster, more pleasant and more readable for diverse non-specialist
audiences. This means that with Sciris users can get more done with less
code, without the need to reinvent the wheel, and spend less time looking
things up on StackOverflow (or the other 20+ tabs with the documentation of
every single library your new application is built upon). Further, Sciris
offers an extension to build webapps for in Python: ScirisWeb. In contrast to
Plotly Dash (ref) and Streamlit (ref), which have limited options for
customization, ScirisWeb is modular, so users have control over which subset
of modules to use for which aspects of any project. 

The name Sciris, a combination of Scientific + Iris (Greek word for
"rainbow"), thus honours the wide spectrum and diversity of commonly done
 scientific tasks, as well as the well established low-level interfacing
 libraries required in the development of scientific computing applications.


# Statement of need
<!-- 
  Maybe reduce this section.
 -->

With the increasing availability of large volumes of data and computing
resources, scientists across multiple fields of research have been able to
tackle increasingly complex problems. But to harness those resources, using
and developing domain-specific software have become ubiquitous activities in
scientific projects. Commensurate with the complexity of problems, these software-related
activities have also become increasingly complex, creating a steep learning
curve, especially for scientists without extensive computer programming
literacy, and increasing the burden of code review [@burden-codereview]. 

<!-- NOTE: find a paper of papers where they do a survey of the state of scientific code production, to justify the 
  "large fraction"
 -->
The current reality of a large fraction of scientific code production is that any workflow
(e.g., either a full cycle in the development of a new software library, or
in the execution of a one-off individual analysis) very often relies on
multiple codebases, including but not limited to: low-level libraries,
domain-specific open-source software, self-developed and/or inherited
swiss-army-knife toolboxes -- whose original developer may or may not be
around to pass on undocumented wisdom. Several scientific communities have
adopted collaborative, community-driven, open-source software projects due to
the significant savings in development costs and increases in code quality
that they afford [@kerr2019epidemiology] (e.g., astropy
[@robitaille2013astropy], nilearn [@nilearn] and fmriprep
[@esteban2019fmriprep]). Despite this progress, a large fraction of
scientific software efforts remain a solo adventure, leading to an increase
in the proliferation of tools that reinvent the wheel. 

<!-- NOTE: astropy and nilearn get a mention because here of their scale e
and the size of the core developer team. There are other libraries such as seaborn and pingouin that are also
open-source projects, but still are heavily developed and maintained by a single developer -->


Scientific software differs from commercial production software in that it is
a crucial component in the elaboration of scientific conclusions, and as such
it should be: re-runnable, repeatable, reproducible, reusable, and
replicable [@benureau2018re]. A key aspect to ensure these properties is
readability of tutorials, documentation and especially of code itself. But it
is essential to note that programming abstractions may not be a great way to
express human-readable scientific ideas, which is what scientific code should
convey (e.g., one would not put the user manual of a spectrophotometer under
the Methods section of a report). 

There are several notable libraries that follow this "simplifying interfaces"
approach to let researchers focus their time an efforts in solving problems,
prototyping solutions, deploying applications and educating their
communities. Some of these include PyTorch, seaborn
[@waskom2021seaborn], DataLad[@alchenko2021datalad], pingouin
[@vallat2018pingouin], Mayavi [@ramachandran2011mayavi] and PyVista
[@sullivan2019pyvista], just to name a few though there are many more. For
instance, PyTorch made models easier to write compared to TensorFlow. It is
used in production environments but its remains most popular in academic and
in research environments [@pytorch-research]. 

However, among the already existing libraries we did not encountered one that
would  handle the more complex semantics of, for instance powerful
containers, or parallelisation of trivial data-intensive operations.

Sciris traces its origins to 2014 to support development of the Optima suite
of models [@kerr2015optima]. We kept encountering the same issues and
inconveniences over and over while building scientific webapps, and began
collecting the tools we used to overcome these issues into a shared library.
While Python was and still is considered an easy-to-use language for
beginners, the motivation that shaped Sciris evolution was to further lower
the barriers to access, interact with, and orchestrate the numerous
supporting libraries we were using. We knew our endeavor paid off when in
early 2020 the combination of brevity and simplicity provided by Sciris was
crucial in (i) the faster-than-average development of Covasim
[@kerr2021covasim; @kerr2022python], and (ii) enabling further Covasim to
become one of the most widely adopted COVID models, used by students,
researchers and policy makers alike. In addition to Covasim, Sciris is
currently used in a number of scientific applications
[@kedziora2019cascade; @atomica; @fraser2021using] and since 2022 has been
designated as a critical project on the Python Pakacage Index (PyPI).

The current stable version of Sciris includes implementations of heavily used
code patterns and abstractions we have identified over the last 8 years, and
that we have demonstrated facilitate the development and deployment of
complex domain-specific scientific applications regardless of their scope and
scale, and further enables non-specialist audiences to interact with these
complex applications.

Sciris "stands on the shoulders of giants", and as
such is not intended as a replacement of those, bur rather as a strongly
idiomatic scientific crucible that will result in a more effective and
sustainable development process for solo-developers and teams alike
(including increasing the longevity [@perkel2020challenge] of new scientific
libraries). Sciris remains in active development and maintenance. We note
that ScirisWeb, while functional, is still in beta development.


<!-- NOTE: mention other libraries and how Sciris compares to them
 -->


<!-- NOTE: maybe cite a paper that discussed the number of scientific toolboxes that eventually die. 
Can help with the argument that Sciris may help prolong the longevity of scientific software.  -->


<!-- This may sound paradoxical -->
<!-- Sciris is domain-specific in the sense that it has been mostly developed by
researchers to be used by researchers. However, within the scope of scientific
software Sciris is domain-general because it can be used to develop
libraries for different research domains such as physics,
neuroscience or epidemiology.  -->


# Example
<!-- (perhaps mention a few of the libraries/dependencies) -->
The Sciris library offers a coordinating interface to multiple well
established and highly flexible Python libraries, yet their simultaneous use
in a single simple script may obscure the key logic of the scientific problem. 

For instance let us imagine that we want to randomly sample numbers from a
user-defined smooth function. In addition, we want to repeatedly draw numbers
for multiple levels of noise, and save these results in separate files. At a
later stage, we would like to load the independent files, "glue" them
together to reconstruct a surface embedded in 3D by interpolating the random
samples; and finally, we want to plot the random points and surface together.
Parallelizing the repeated draws and customizing the axes to render the 3D
scatter plot plus mesh can be quite cumbersome. The example 
\autoref{fig:showcase-code} presents two functionally identical scripts and
highlights that the one written with Sciris is much more succinct and
readable:

![Comparison of functionally identical script without Sciris (left) and with Sciris (right).\label{fig:showcase-code}](figures/sciris-showcase-code.png){ width=100% }


![Output of the script written with Sciris in Fig.\autoref{fig:showcase-code}.\label{fig:showcase-output} ](figures/sciris-showcase-output.png){ width=100% }



# Overview
Sciris has been designed to provide class- and function based implementations
of common operations ranging from merging ordered dictionaries, to providing
simplified interfaces to datetime arithmetic, and to limiting the execution
of a program based on resource usage irrespective of the operating system or
computational environment where the application is executed. 



ScirisWeb provides a ''just works'' solution using [Vuejs](https://vuejs.org/) for the frontend, [Flask](https://flask.palletsprojects.com/en/2.2.x/) as the web framework, [Redis](https://redis.io/) for the (optional) database and Matplotlib/[mpld3](https://github.com/mpld3/mpld3) for plotting. ScirisWeb  also enables users to use a a React (ref) frontend linked to an SQL database with Plotly figures, ScirisWeb can serve as the glue holding all of that together.


![Block diagram of the main functional components in Sciris.\label{fig:block-diagram}](figures/sciris-block-diagram-00.png){ width=100% }



<!-- Example: something as simple as providing an alias
moving average, rolling mean, rolling average, convolution  -->


# Acknowledgements
To be added


# References