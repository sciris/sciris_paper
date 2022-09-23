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
Sciris is a cohesive collection of tools that enables simple interaction with
foundational libraries from the scientific Python ecosystem(e.g., `numpy`,
`scipy`, and `matplotlib`), as well as with libraries of broader scope, such
as `multiprocessing` and `pickle`. The purpose of Sciris is to facilitate and
accelerate the development and delivery of easy-to-use domain-specific
scientific software. This is achieved by providing classes and methods that
simplify the interface to frequently used functionality which, while
essential for the development of robust software applications, diverts focus
from the actual problem being solved. Some of Sciris' key features include:
ensuring consistent dictionary, list, and array types (e.g., enabling users
to provide inputs to a class or method as either lists or arrays); enabling
ordered dictionary elements to be referenced by index; simplifying datetime
arithmetic by allowing users to provide either a date string or a datetime
object; simplifying the saving and loading of files and complex objects; and,
simplifying the parallelisation of common operations. Sciris makes writing
scientific code in Python faster, more pleasant and more readable for a
diverse non-specialist audience. This means that with Sciris users can get
more done with less code, without the need to reinvent the wheel, and spend
less time looking things up on StackOverflow (or the other 20+ tabs with the
documentation of every single library your new application is built upon).
Further, Sciris offers an extension to build webapps in Python: ScirisWeb. In
contrast to [Plotly's Dash](https://github.com/plotly/dash) and [Streamlit](https://streamlit.io/), which have limited options for customization,
ScirisWeb is modular, so users can control which subset they use for a
project. 
<!-- NOTE: ^^^^ probably need to specify what sort of customisation is lacking in
Streamlit and Dash  -->

The name Sciris, a combination of Scientific + Iris (Greek word for
"rainbow"), thus honors the wide spectrum of tasks commonly required in the
 development of scientific computing applications.

# Statement of need
<!-- 
Need to reduce this section-->
With the increasing availability of large volumes of data and computing
resources, scientists across multiple fields of research have been able to
tackle increasingly complex problems. But to harness these resources, the
need to develop and use domain-specific software has become a ubiquitous part
of scientific projects. Commensurate with the complexity of problems, these
software-related activities have also become increasingly complex, creating a
steep learning curve and an increasing burden of code review
[@burden-codereview]. 

<!-- NOTE: need to find a recent paper where they show survey results of the state of scientific code production, to justify the "large fraction" phrase, I know i read one last year or the year before but i can't remember the authors. or journal. Maybe it was a blog post.  -->
The current reality of scientific code production is that any workflow
(e.g., either a full cycle in the development of a new software library, or
in the execution of a one-off individual analysis) very often relies on
multiple codebases, including but not limited to: low-level libraries;
domain-specific open-source software; and self-developed and/or inherited
swiss-army-knife toolboxes -- whose original developer may or may not be
around to pass on undocumented wisdom. Several scientific communities have
adopted collaborative, community-driven, open-source software approaches due
to the significant savings in development costs and increases in code quality
that they afford [@kerr2019epidemiology] (e.g., astropy
[@robitaille2013astropy], nilearn [@nilearn] and fmriprep
[@esteban2019fmriprep], [HoloViz's libraries](https://holoviz.org)). Despite
this progress, a large fraction of scientific software efforts remain a solo
adventure leading to proliferation of tools where resources have been spent
reinventing the wheel. 

<!-- NOTE: astropy and nilearn get a mention here because of their scale 
and the size of the core dev team. There are other libraries such as seaborn and pingouin that are also open-source projects, but still are heavily developed and maintained by a single developer -->
Scientific software differs from commercial production software in that it is
a crucial component in the elaboration of scientific conclusions, and as such
it should be: re-runnable, repeatable, reproducible, reusable, and
replicable [@benureau2018re]. A key aspect to ensure these properties is
readability of tutorials, documentation and especially of code itself. **But
it is essential to note that programming abstractions may not be a great way
to express human-readable scientific ideas, which is what scientific code
should convey**. For instance, one of the reasons PyTorch has become popular
in academic and in research environments is its success in making models
easier to write compared to TensorFlow [@pytorch-research]. 

The need for libraries that provide "simplifying interfaces" is reflected by
the development of various notable libraries in scientific Python ecosystem,
that have enabled researchers focus their time and efforts on solving
problems, prototyping solutions, deploying applications and educating their
communities.Some of these include PyTorch, seaborn
[@waskom2021seaborn], DataLad [@halchenko2021datalad], pingouin
[@vallat2018pingouin], hypothesis [@maciver2019hypothesis], Mayavi
[@ramachandran2011mayavi] and PyVista[@sullivan2019pyvista], just to name a
few though there are many more. 

Sciris itself traces its origins to 2014, initially created to support
development of the Optima suite of models[@kerr2015optima]. Among the
existing libraries at the time we had not found one that simplified the
complex semantics of powerful containers or the parallelisation of trivial
yet data-intensive operations. In our work, we kept encountering the same
inconveniences over and over while building scientific webapps, and so began
collecting the tools we used to overcome them into a shared library. While
Python was, and still is, considered an easy-to-use language for beginners,
the motivation that shaped Sciris' evolution was to further lower the
barriers to access, interact with, and orchestrate the numerous supporting
libraries we were using. 

For those reasons Sciris provides tools that will result in (i) a more effective and
sustainable scientific code production for solo-developers and teams alike, and
(ii) increased longevity [@perkel2020challenge] of new scientific libraries. 
Some of the key aspects that Sciris provides are:

*Brevity through simplifying interfaces*
By encapsulating common regular patterns that span multiple lines of code to do a simple task (i.e., `sc.fig3d`, `sc.ax3d`, `sc.hex2rgb`), or a necessary but less trivial task (e.g., `sc.printarr` pretty print numeric arrays with up to 3 axes, `sc.mergedicts` and `sc.mergenested`), and wrapping them in a function with a simple interface (e.g., one would not include the 'how-to-assemble' manual a spectrophotometer as part of a every report on protein analysis).

*Scientific idiomaticity*. Sciris promotes the use of human-readable named functions (i.e., `sc.smooth`, `sc.findnearest`, `sc.safedivide`) so that the resulting code is as scientifically and human-readable as possible. Further, we note that some of Sciris function names are similar to Matlab's (i.e., `sc.tic` and `sc.toc`). This is 
because there there is often a need to either translate from/to Matlab or R are, or to integrate code components written in multiple languages.

*Forgiving and strict exception handling*
Across many complex classes and methods, Sciris uses the keyword `die`, enabling users to set a locally scoped level of strictness in the handling of exceptions. If `die=False`, Sciris softly handles exceptions by using its default (opinionated) behavior. This could be simply printing a message and returning `None` so users can decide how to proceed. If `die=True`, it directly raises the corresponding exception and message. 

*Handling of versioning for reproducibility*

ADD something here

We confirmed our approach with Sciris had paid off when in early 2020 its
combination of brevity and simplicity provided was crucial in: (i) the
faster-than-average development of Covasim
[@kerr2021covasim; @kerr2022python]; and (ii) enabling Covasim to become one
of the most widely adopted COVID models, used by students, researchers and
policy makers alike. In addition to Covasim, Sciris is currently used in a
number of scientific applications
[@kedziora2019cascade; @atomica; @fraser2021using; @hiptool; @synthpops; @parestlib]
and since 2022 has been designated as a critical project on the Python
Package Index (PyPI).


# Example
<!-- (perhaps mention a few of the libraries/dependencies) -->
The Sciris library offers a coordinating interface to multiple well
established and highly flexible Python libraries. Writing a script that
directly uses multiple of these underlying libraries can obscure the key
logic of the scientific problem. Whereas the Sciris interface keeps the focus
on the science.

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

![Comparison of functionally identical script without Sciris (left) and with Sciris (right). The resulting plot is shown below. \label{fig:showcase-code}](figures/sciris-showcase-code-and-output.png){ width=100% }


# Overview
Sciris has been designed to provide class- and function based implementations
of common operations ranging from merging ordered dictionaries, to providing
simplified interfaces to datetime arithmetic, and to limiting the execution
of a program based on resource usage. \autoref{fig:block-diagram} shows the
functional modules of Sciris. 





![Block diagram of the main functional components in Sciris.\label{fig:block-diagram}](figures/sciris-block-diagram-00.png){ width=100% }


Documentation can be found at [https://sciris.readthedocs.io]
(https://sciris.readthedocs.io) with a detailed description on installation
instructions for both [Sciris](https://github.com/sciris/sciris) and
[ScirisWeb](https://github.com/sciris/scirisweb); [how-to-contribute guidelines](https://sciris.readthedocs.io/en/latest/contributing.html); and [style guide](https://sciris.readthedocs.io/en/latest/style_guide.html).  

Presentation/representation of messages, of types, of data, of objects, visualization 

## Key features
<!-- NOTE: present some key features (a subset of the docs)  
 -->

#### Containers 
One of the key features in Sciris is `odict`, a flexible container of an associative array representing the best-of-all-worlds across lists, dictionaries, and numeric arrays. An ordered dictionary, similar to the OrderedDict class from `collections`, but supports list methods like integer indexing, key slicing, and item inserting. It can also replicate defaultdict behavior via the `defaultdict` argument.

```Python
my_odict = sc.odict(foo=[1,2,3], bar=[4,5,6]) #
my_odict['foo'] == my_odict[0]                # Access by key or by index
my_odict[:].sum() == 21                       # Slices returned as numpy arrays by default
for i, key, value in my_odict.enumitems():    # Additional methods for iteration
    print(f'Item {i} is named {key} and has value {value}')
```

The function `sc.mergedicts`, by default, skips things that are not dictionaries (e.g., `None`), and allows keys to be set multiple times. The first dictionary supplied will be used for the output type (e.g. if the first dictionary is an `sc.odict`, an `sc.odict` will be returned). This function is useful for cases such as function (keyword) arguments where the default is simply set as `None` but later on a dictionary will be needed.

#### Dictionary functions.

```Python
sc.flattendict({'a':{'b':1,'c':{'d':2,'e':3}}})
{('a', 'b'): 1, ('a', 'c', 'd'): 2, ('a', 'c', 'e'): 3}


sc.flattendict({'a':{'b':1,'c':{'d':2,'e':3}}}, sep='_')
{'a_b': 1, 'a_c_d': 2, 'a_c_e': 3}
```


The function `sc.promotetolist` was developed so user-defined functions can
handle inputs like ``'a'``  or ``['a', 'b']``. In other words, if an argument
can either be a single thing (e.g., a single dictionary key) or a list
(e.g., a list of dict keys), this function can be used to do the conversion,
so it is always safe to iterate over the output.


Pretty object

The `die` keyword that provides different levels of safechecks/criticality of an error during execution for debugging.

#### Plotting and visualization 
vectocolor
arraycolor
rgb2hex
hex2rgb
fig3d
ax3d
commaticks
savefig including metadata
orderlegend



### Adaptive stochastic descent (ASD) optimization algorithm
Sciris provides an optimization algorithm that has been designed to replicate
the essential aspects of manual parameter fitting in an automated way.
Specifically, ASD uses simple principles to form probabilistic assumptions
about (a) which parameters have the greatest effect on the objective
function, and (b) optimal step sizes for each parameter
[@kerr2018optimization].



#### 
datetime arithmetic
now
day
daydiff
daterange


### ScirisWeb
ScirisWeb provides a solution using [Vuejs](https://vuejs.org/) for the frontend, [Flask](https://flask.palletsprojects.com/en/2.2.x/) as the web framework, [Redis](https://redis.io/) for the (optional) database and Matplotlib/[mpld3](https://github.com/mpld3/mpld3) for plotting. ScirisWeb  also enables users to use a React frontend linked to an SQL database with Plotly figures, ScirisWeb can serve as the glue holding all of that together.


<!-- Example: something as simple as providing an alias
moving average, rolling mean, rolling average, convolution  -->

### Concluding remarks
The current stable version of Sciris includes implementations of heavily used
code patterns and abstractions that facilitate the development and deployment
of complex domain-specific scientific applications, regardless of their scope
and scale, and further enables non-specialist audiences to interact with
these complex applications. Sciris "stands on the shoulders of giants", and
as such is not intended as a replacement of those, but rather as a strongly
idiomatic scientific crucible that will result in a more effective and
sustainable development process for solo-developers and teams alike, and
hopefully it will help increasing the longevity [@perkel2020challenge] of new
scientific libraries. Sciris is actively developed and maintained. We note
that ScirisWeb, while functional, is still in beta development.


<!-- NOTE: adapting from Cliff Big Software paper in 2019
  Third, if a single modeling framework is adopted to the exclusion of other modeling approaches, it limits the potential for gaining insight by comparing across many different models and may result in a ‘herd’ effect (Eaton et al. 2014).
 -->
As we mentioned before, there are many terrific libraries whose aim is to
provide simpler interfaces to different forms of scientific code across
multiple levels of complexity. Some of these have functionality that overlap
with Sciris, and while that may deserve the question of "aren't we
reinventing the wheel?", we notice that duplication is not always undesirable
process, as the community of scientific software developers still has a long
way to go to identify clear and universal principles of scientific code
design.


# Acknowledgements
To be added


# References