# 265Draw-seng-265

A colored-line-drawing program, that can generate SVG images based on geometric transformations.

Written by Phil Denhoff, Alex Welsh-Piedrahita, Joe Leong, and Eric Borth.


From the assignment description:

### Step B: add colour to lines_to_svg.py ###

Copy `lines_to_svg.py` to `lines_to_svg_colour.py`. Modify `lines_to_svg_colour.py` so that it accepts an optional colour as a sixth token in each line.

The legal colours are those contained in the file css_colours.txt. If no colour is specified, then the colour 'Black' must be used.

In `lines_to_svg_colour.py`, make only those changes needed to add colours.

To test `lines_to_svg_colour.py`:

1. Normal case:
```
python lines_to_svg_colour.py square_colour.txt > square_colour.svg
diff square_colour.svg square_colour_gold.svg
```
There should be no diff output.

2. Error case:
```
python lines_to_svg_colour.py bad_lines_file_colour.txt 2> test_B.txt > /dev/null
diff test_B.txt test_B_gold.txt
```
There should be no diff output.

### Step B: generate some SVG images ###

Present draft versions of your new generator and transformer.

Show the generated images.

Be prepared to discuss the generator and transformer code.

### Step C: complete the 265Draw app and documentation ###

The 265Draw framework consists of:
Generators
 - A generator, such as generate_tree.py, creates a new line file based solely on command-line parameters.

Transformers
 - A transformer, such as rings.py, creates a new line file based on command-line parameters as well as one or more existing line files.

Bash scripts
 - A bash script, such as rings.sh, uses generators, transformers and lines_to_svg.py to create new SVG files.
 
Apps
 - Each 265Draw app, such as TreeRings, consists of one or more generators, transformers and bash files. In addition, an app must provide a users manual, describing how to use the app, but not how the app has been implemented. For TreeRings, the manual is in TreeRings.html

In step C, you must provide a new 265Draw app. You may assume that the user understands basic two-dimensional geometry and can use a text editor. You may also assume that the user understands the shell commands required to run a bash script.

You may not assume that the user knows any Python or anything about programming.

You app must contain:
 - at least one new generator,
 - at least one new transformer,
 - a users manual in either HTML or PDF format, not exceeding three pages in length.

You must not modify `Line_Point.py`.

You must not modify `lines_to_svg.py`, except for the step B changes regarding colour.

You may use the Python modules `Line_Point`, `copy`, `math`, `re` and `sys`.

**You may not use any other Python modules.**
