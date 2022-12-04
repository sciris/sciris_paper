---
title: 'Sciris: Simplifying scientific software in Python'

tags:
  - python
  - scientific software development
  - computational science
  - high-performance containers
  - numerical utilities
  - plotting

authors:
  - name: Cliff C. Kerr
    orcid: 0000-0003-2517-2354
    corresponding: true
    affiliation: "1, 2" 
  - name: Paula Sanz-Leon
    orcid: 0000-0002-1545-6380
    affiliation: 1
  - name: Romesh G. Abeysuriya
    orcid: 0000-0002-9618-6457
    affiliation: "1, 3"
  - name: George L. Chadderdon
    orcid: 0000-0002-3034-2330
    affiliation: 3
  - name: Vlad-Ştefan Harbuz
    affiliation: 4
  - name: Parham Saidi
    affiliation: 4
  - name: James Jansson
    affiliation: 5
  - name: Maria del Mar Quiroga
    orcid: 0000-0002-8943-2808
    affiliation: 3
  - name: Rowan Martin-Hughes
    orcid: 0000-0002-3724-2412
    affiliation: 3
  - name: Sherrie L. Kelly
    orcid: Sherrie Kelly
    affiliation: 3
  - name: Jamie A. Cohen
    orcid: 0000-0002-8479-1860
    affiliation: 1
  - name: Robyn M. Stuart
    orcid: 0000-0001-6867-9265
    affiliation: "1, 3"
  - name: Anna Nachesa
    affiliation: 6

affiliations:
 - name: Institute for Disease Modeling, Global Health Division, Bill \& Melinda Gates Foundation, Seattle, USA
   index: 1
 - name: School of Physics, University of Sydney, Sydney, Australia
   index: 2
 - name: Burnet Institute, Melbourne, Victoria, Australia 
   index: 3
 - name: Saffron Software, Bucharest, Romania
   index: 4
 - name: Kirby Institute, University of New South Wales, Sydney, Australia
   index: 5
 - name: Google Inc., Zürich, Switzerland
   index: 6

date: 2 December 2022
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

[Sciris](https://github.com/sciris/sciris) is a collection of tools that simplifies use of the foundational libraries in the scientific Python ecosystem (such as NumPy for math and Matplotlib for plotting), as well as with libraries of broader scope, such as `multiprocess` (for parallelization) and `pickle` (for saving and loading objects). The purpose of Sciris is to accelerate the development of scientific software. This is achieved by providing classes and functions that provide easy access to frequently used low-level functionality, which, while valuable for developing robust software applications, diverts focus from the scientific problem being solved. Some of Sciris' key features include: ensuring consistent dictionary, list, and array types (e.g., enabling users to provide inputs as either lists or arrays); enabling ordered dictionary elements to be referenced by index; simplifying datetime arithmetic by allowing users to provide dates in various formats, including strings; simplifying the saving and loading of files and complex objects; and simplifying the parallel execution of code. Sciris makes writing scientific code in Python faster, more pleasant, and more accessible, especially for people without extensive training in software development. With Sciris, users can achieve the same functionality with fewer lines of code, avoid reinventing the wheel, and spend less time looking up solutions on Stack Overflow. Sciris also forms the basis of ScirisWeb, an additional set of tools for building Python webapps. In summary, Sciris aims to streamline the wide spectrum of tasks commonly required when developing scientific software tools.


# Statement of need

With the increasing availability of large volumes of data and computing resources, scientists across multiple fields of research have been able to tackle increasingly complex problems. But to harness these resources, the need to develop and use domain-specific software has become a ubiquitous part of scientific projects. Commensurate with the complexity of problems, these software-related activities have also become increasingly complex, creating a steep learning curve and an increasing burden of code review [@burden-codereview].

The current reality of scientific code production is that any workflow (e.g., either a full cycle in the development of a new software library, or in the execution of a one-off individual analysis) very often relies on multiple codebases, including but not limited to: low-level libraries; domain-specific open-source software; and self-developed and/or inherited Swiss-army-knife toolboxes -- whose original developer may or may not be around to pass on undocumented wisdom. Several scientific communities have adopted collaborative, community-driven, open-source software approaches due to the significant savings in development costs and increases in code quality that they afford [@kerr2019epidemiology] (e.g., `astropy` [@robitaille2013astropy], `nilearn` [@nilearn] and `fmriprep` [@esteban2019fmriprep], [HoloViz's libraries](https://holoviz.org)). Despite this progress, a large fraction of scientific software efforts remain a solo adventure leading to proliferation of tools where resources are largely spent reinventing wheels. Since the core purpose of scientific software is to support scientific conclusions, it must be be: re-runnable, repeatable, reproducible, reusable, and replicable [@benureau2018re]. 

Beyond these minimum requirements, low-level programming abstractions may get in the way of clarifying the science. For instance, one of the reasons PyTorch has become popular in academic and research environments is its success in making models easier to write compared to TensorFlow [@pytorch-research]. The need for libraries that provide "simplifying interfaces" for research applications is reflected by the development of various notable libraries in scientific Python ecosystem that have enabled researchers focus their time and efforts on solving problems, prototyping solutions, deploying applications and educating their communities. Some of these include PyTorch, seaborn [@waskom2021seaborn], DataLad [@halchenko2021datalad], pingouin [@vallat2018pingouin], hypothesis [@maciver2019hypothesis], Mayavi [@ramachandran2011mayavi] and PyVista [@sullivan2019pyvista], among many others.

Sciris (whose name comes from a combination of "scientific" and "iris", the Greek word for "rainbow") originated in 2014, initially created to support development of the Optima suite of models [@kerr2015optima]. We repeatedly encountering the same inconveniences while building scientific webapps, and so began collecting the tools we used to overcome them into a shared library. While Python was, and still is, considered an easy-to-use language for beginners, the motivation that shaped Sciris' evolution was to further lower the barriers to access, interact with, and orchestrate the numerous supporting libraries we were using.

For those reasons Sciris provides tools that will result in a more effective and sustainable scientific code production for solo developers and teams alike, and increased longevity [@perkel2020challenge] of new scientific libraries. Some of the key functional aspects that Sciris provides are: (i) brevity through simplifying interfaces; (ii) scientific idiomaticity; (iii) locally scoped forgiving and strict exception handling; and (iv) management of versioning. We expand on each of these below, but first provide a vignette that illustrates many of Sciris' features.


# Vignette

The Sciris library offers a straightforward interface to various well-established Python libraries. Writing a script that uses these libraries directly can obscure the key logic of the scientific problem, while Sciris aims to simplify common tasks as much as possible.

For example, imagine that we wish to sample random numbers from a user-defined function with varying noise levels, save the intermediate calculations, and plot the results. In vanilla Python, each of these operations is somewhat cumbersome. \autoref{fig:showcase-code} presents two functionally identical scripts and highlights that the one written with Sciris is much more succinct and readable:

![Comparison of a functionally identical script without Sciris (left) and with Sciris (right), showing a nearly five-fold reduction in lines of code. The resulting plot is shown in \autoref{fig:showcase-output}. \label{fig:showcase-code}](figures/sciris-showcase-code.png){ width=100% }

![Output of the codes shown in \autoref{fig:showcase-code}, without Sciris (left) and with Sciris (right). The two are identical except for the new high-contrast colormap available in Sciris. \label{fig:showcase-output}](figures/sciris-showcase-output.png){ width=100% }

This vignette illustrates many of Sciris' most-used features, including timing, parallelization, high-performance containers, file saving and loading, and plotting. For the parts of the script that differ, Sciris reduces the number of lines required from 33 to 7, a 79% decrease.


# Design philosophy

The aim of Sciris is to make common tasks simple. The current stable version of Sciris (2.0.5) includes implementations of heavily used code patterns and abstractions that facilitate the development and deployment of complex domain-specific scientific applications, and helps non-specialist audiences interact with these applications. We note that Sciris "stands on the shoulders of giants", and as such is not intended as a replacement of these libraries, but rather as an interface that facilitate a more effective and sustainable development process through the following principles:

*Brevity through simplifying interfaces*. Sciris packages common patterns requiring multiple lines of code into single, simple functions. With these functions one can succinctly express and execute frequent plotting tasks (e.g., `sc.commaticks`, `sc.dateformatter`, `sc.plot3d`); ensure consistent types and merging containers (e.g., `sc.toarray`, `sc.mergedicts`, `sc.mergelists`), or line-by-line performance profiling (`sc.profile`). Brevity is also achieved by extending functionality of well established objects (e.g., `OrderedDict` via `sc.odict`) or methods (e.g., `isinstance` via `sc.checktype` that enables the comparison of objects against higher-level types like `listlike`).

*Dejargonification*. Sciris aims to use plain function names (i.e., `sc.smooth`, `sc.findnearest`, `sc.safedivide`) so that the resulting code is as scientifically and human-readable as possible (e.g., contrast `sc.findinds()` with the functionally similar `np.nonzero()[0]`). Further, some Sciris functions map onto Matlab equivalents (e.g., `sc.tic` and `sc.toc`; `sc.boxoff`), to reduce the learning curve for scientists with this background.

*Forgiving and strict exception handling*. Across many complex classes and methods, Sciris uses the keyword `die`, enabling users to set a locally scoped level of strictness in the handling of exceptions. If `die=False`, Sciris is more forgiving and softly handles exceptions by using its default (opinionated) behavior. This could be simply printing a message and returning `None` so users can decide how to proceed. If `die=True`, it directly raises the corresponding exception and message. This reduces the need for try-catch blocks, which can distract from the code's scientific logic.

*Management of versioning information*. Keeping track of dates, authors, code version, plus additional notes or comments is an essential part of scientific projects. Sciris provides methods to easily save and load metadata to/from figure files, including Git information (`sc.savefig`, `sc.gitinfo`, `sc.loadmetadata`), as well as shortcuts for comparing module versions (`sc.compareversions`) or enforcing them (`sc.require`).

Our investments in Sciris paid off when in early 2020 its combination of brevity and simplicity proved crucial in enabling the rapid development of the Covasim model of COVID-19 transmission [@kerr2021covasim; @kerr2022python]. Covasim's relative simplicity and readability, based in large part on its heavy use of Sciris, enabled it to become one of the most widely adopted models of COVID-19, used by students, researchers and policymakers in over 30 countries. 

In addition to Covasim, Sciris is currently used by a number of other scientific software tools, such as [Optima HIV](https://github.com/optimamodel/optima) [@kerr2015optima], [Optima Nutrition](https://github.com/optimamodel/nutrition) [@pearson2018optima], the [Cascade Analysis Tool](https://cascade.tools) [@kedziora2019cascade], [Atomica](https://atomica.tools) [@atomica], Optima TB [@gosce2021optima], the [Health Interventions Prioritization Tool](http://hiptool.org) [@fraser2021using], [SynthPops](https://synthpops.org) [@synthpops], and [FPsim](https://fpsim.org) [@o2022fpsim].


# Overview of key features

Sciris provides class- and function-based implementations of common operations ranging from parallelization to improved object representation; here we illustrate a smattering of key features in greater detail. Further information can be found at [https://docs.sciris.org](https://docs.sciris.org). Documentation includes installation instructions (`pip install sciris`), for both [Sciris](https://github.com/sciris/sciris) and [ScirisWeb](https://github.com/sciris/scirisweb), usage instructions, and [style guidelines](https://sciris.readthedocs.io/en/latest/style_guide.html).

\autoref{fig:block-diagram} illustrates the functional modules of Sciris.

![Block diagram of the Sciris' functionality, grouped by high-level concepts and types of tasks that are commonly performed in scientific code.\label{fig:block-diagram}](figures/sciris-block-diagram-03.png){ width=100% }

## High-performance containers
One of the key features in Sciris is `sc.odict`, a flexible container representing an associative array with the best-of-all-worlds across lists, dictionaries, and numeric arrays. This is based on `OrderedDict` from [`collections`](https://docs.python.org/3/library/collections.html), but supports list methods like integer indexing, key slicing, and item inserting:

```Python
> my_odict = sc.odict(foo=[1,2,3], bar=[4,5,6]) 
> my_odict['foo'] == my_odict[0]                
> my_odict[:].sum() == 21                       
> for i, key, value in my_odict.enumitems():    
     print(f'Item {i} is named {key} and has value {value}')
```

## Numerical utilities
`sc.findinds` matches even if two things are not exactly equal due to differences in numeric type (e.g., floats vs. integers). The code shown below produces the same result as calling `np.nonzero(np.isclose(arr, val))[0].`
```Python
> sc.findinds([2,3,6,3], 3) 
array([1,3])
```

<!-- ### Don't paint it black  
`sc.vectocolor` converts a 1D array of N values into an Nx3 array
of RGB values according to the current colormap. `sc.arraycolor` extends this functionality to multidimensional arrays. 
 -->
## Parallelization
A frequent hurdle scientists face is parallelization. Sciris provides `sc.parallelize`, which acts as a shortcut for using `multiprocess.Pool()`. Importantly, this function can also iterate over more complex arguments. It can either use a fixed number of CPUs or allocate dynamically based on load (`sc.loadbalancer`). Users can also specify a fixed number of CPUs to be used. The example below shows three equivalent ways to iterate over multiple arguments:
```Python
> def f(x,y):
>     return x*y

> out1 = sc.parallelize(func=f, iterarg=[(1,2),(2,3),(3,4)])
> out2 = sc.parallelize(func=f, iterkwargs={'x':[1,2,3], 'y':[2,3,4]})
> out3 = sc.parallelize(func=f, iterkwargs=[{'x':1, 'y':2}, 
                                            {'x':2, 'y':3}, 
                                            {'x':3, 'y':4}])

> assert out1 == out2 == out3
```

## Plotting

, with the results shown in \autoref{fig:plotting-example}:

```Python
> sc.options(font='Garamond') # Custom font
> x = sc.daterange('2022-06-01', '2022-12-31', as_date=True) # Create dates
> y = sc.smooth(np.random.randn(len(x))**2*1000) # Create smoothed random numbers
> c = sc.vectocolor(y, cmap='turbo') # Set colors proportional to y values
> plt.scatter(x, y, c=c) # Plot the data
> sc.dateformatter() # Custom date axis formatter
> sc.commaticks() # Add commas to y-axis ticks
> sc.setylim() # Reset the y-axis limits
> sc.boxoff() # Remove the top and right axis spines
```

![Example of plot customizations via Sciris, including x- and y-axis ticks and the font.\label{fig:plotting-example}](figures/plotting-example.png){ width=70% }




# ScirisWeb



ScirisWeb provides a solution using [Vuejs](https://vuejs.org/) for the frontend, [Flask](https://flask.palletsprojects.com/en/2.2.x/) as the web framework, [Redis](https://redis.io/) for the (optional) database and Matplotlib/[mpld3](https://github.com/mpld3/mpld3) for plotting. ScirisWeb also enables users to use a React frontend linked to an SQL database with Plotly figures, ScirisWeb can serve as the glue holding all of that together. In contrast to [Plotly Dash](https://github.com/plotly/dash) and [Streamlit](https://streamlit.io/), which have limited options for customization, ScirisWeb is completely modular, so users can choose which features they use for a project. 


# Acknowledgements

The authors wish to thank David P. Wilson, William B. Lytton, and Daniel J. Klein for their sponsorship of the Sciris project. David J. Kedziora, Dominic Delport, Kevin M. Jablonka, Meikang Wu, and Dina Mistry provided helpful feedback on and support for the Sciris library. Sciris development was made possible by financial support from the United States Defense Advanced Research Projects Agency (DARPA) Contract N66001-10-C-2008 (2010–2014), the World Bank Assignment 1045478 (2011–2015), the Australian National Health and Medical Research Council (NHMRC) Project Grant APP1086540 (2015–2017), the Australian Research Council (ARC) Discovery Early Career Research Award (DECRA) Fellowship Grant DE140101375 (2014–2019), Intellectual Ventures (2019–2020), and the Bill \& Melinda Gates Foundation (2020–present).


# References