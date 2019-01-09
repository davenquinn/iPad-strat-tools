# iPad-strat-tools

This is a basic toolset for collecting stratigraphic data in the field
on an iPad, and rendering a seamless high-resolution stratigraphic column
that can be exported for publication or handed off to other software
such as Illustrator or Procreate for completion.

It includes a description of an iPad workflow for section-measuring,
a set of PDF section axes to use as a GoodNotes template, and a command-line
tool, `stack-section`, that stacks rendered section pages into a complete column.
Other tools can be added as needed.

# The workflow: stratigraphic measurement in GoodNotes

The iPad Pro, with its Apple Pencil, has the potential to completely change
how we do field geology. One of the clearest demonstrations of its potential is
using it to measure a section in the field – gone are the days of tediously
scanning your field notebook, massive layouts in Photoshop, and finicky graphics
tablets. Or transcribing onto sheets of vellum.

Stylus-enabled note-taking apps allow drawing like paper on a consistent set
of axes, in an intuitive and robust way. They also support progressive enhancement
in a way their Rite-in-the-Rain cousins cannot — by the time you're out of the
field, you're much of the way to your publication-quality sections!

[GoodNotes](https://www.goodnotes.com/) is one of the best note-taking apps
we have encountered for the iPad, and the workflow described here is tailored to
its use. Other note-taking apps like [Paper](https://paper.bywetransfer.com/)
might also be useful, and the tool(s) presented here can be modified to support
their use.

## A standardized template

The first step to using GoodNotes for measurement is to create a stratigraphic
template. Not having to re-label your axes every ~10-20 meters of stratigraphy is
a huge time-saver in the field, and keeping the scale and page placement identical
allows automated stitching and resizing of section images.
A basic PDF template for a stratigraphic column
is [included in this repository](images/section-template.pdf). This is
based on the "Graph Paper" template in GoodNotes, which includes a 1 cm grid by
default (given the page size of 5.82 x 7.42 in assigned by GoodNotes, which is
generally smaller than the real size of your iPad's screen).

To use this template, download it to the *Files* app on your iPad.
Then, in GoodNotes, open the *Template Library* from *Options* > *Template Library*
and then add the PDF to a folder of your choice.

A new template optimized for your desired set of section axes can be made using
the "Graph Paper" template in GoodNotes. Export your new PDF from GoodNotes and
re-import it as a *Template* to use it as the basis for a notebook.

## Using it in the field

We tested this stratigraphic measurement technique during summer 2018.
Four teams with iPads measured ~5-10 sections over a 1.5-week field
campaign in the Naukluft Mountains of Namibia. The technique helped a
diverse group of workers maintain a consistent measurement scale and render
detailed data. It also enabled sharing sections between groups in the evenings
and easy daily backups using AirDrop. The iPads were pretty robust in the field.

Screen use in direct sunlight was a present but not debilitating problem. More
significant was the need to ensure a full day's use from the iPad, while it is
under load with the screen on a high brightness setting. A field notebook should
be kept as a backup, and a power bank should be carried at all times. Users should
expect to recharge the iPad nightly.

## Stitching together a production section

After returning from the field, you'll want to standardize your sections,
remove extraneous annotation, and make them conform to a consistent graphical
style. This could mean artistic rendition and/or painting in patterns such as the
[USGS FGDC Geologic Patterns](https://davenquinn.com/projects/geologic-patterns).

The first (and currently, only) command-line tool in this toolkit is a Python-based
script to stitch together sections that were created using the provided template
(although it can be adapted to others). Parts of the Python code are an adaptation
of earlier code that I wrote for collating sections from scanned images of
field notebook pages. However, the standard size and orientation of a digital
notebook page makes extraction of images from GoodNotes far easier.

The command line creates a tall image representing a completed section
from all of the pages in the pdf, which are assumed to move upwards through
the section. Optionally, the image will be split into several equal parts of
less than a certain pixel height. This is helpful when reasonably-sized images
are needed for loading into other software. For instance, for the iPad drawing
app *Procreate*, the maximum allowed single dimension for an image is 16384 pixels;
if an image exceeds this size, it will be scaled to fit.

## Command-line usage

After installation, the command-line tool should be usable at te

```
Usage: stack-section [OPTIONS] <pdf-input> <png-output>

  Stack a stratigraphic column drawn on multiple pages using a cm-gridded
  GoodNotes template to composite png image(s) of the entire section.

  <pdf-input> is a multipage PDF file
      (presumably exported from GoodNotes).
  <png-output> is a filename for the output PNG
      (it will be suffixed with _1,_2, etc.
      if output is split by --max-height).

Options:
  --clip-left FLOAT        [cm] Left crop (default: 0)
  --clip-right FLOAT       [cm] Right crop (default: 0)
  --height-per-page FLOAT  [cm] Height of section on single page
                           (default: 15). Assumes that the section is centered
                           on the vertical axis of the page.
  --dpi INTEGER            [px/inch] Resolution of output
                           (default: 300).
  --max-height INTEGER     [px] Threshold to split output image
                           if too tall (no default). If not specified, doesn't
                           split the image at all. A value of <=16384 px
                           allows the image to be imported without scaling
                           into Procreate
  --help                   Show this message and exit.
```
