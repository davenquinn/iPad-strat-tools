# The `stack-section` command-line tool

## Installation

`stack-section` is a command-line application written in Python. Right now, the
way to install it is to *clone* the Github repository to your local machine using
```
> git clone https://github.com/davenquinn/iPad-strat-tools.git
```

Then, install the module to your system:
```
> pip install -e iPad-strat-tools
```

Installation requires the `imagemagick` application to be available on your system,
which can be tricky for Windows users.
![Documentation for the *Wand* Python module](docs.wand-py.org/en/0.5.0/guide/install.html)
may suggest ways to solve this issue.

## Command-line usage

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
