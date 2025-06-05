Heresy Tools
############
:date: 2017-12-30 21:33
:author: rjfrank
:slug: the-tools
:status: published
:illustration: box_inn.jpg

A little history...
*******************

Heresy began life as a google doc.  In fact, the entire deck was originally written,
without any imagery, in google docs.  At some point we needed to move to a graphics
toolset as one can only go so far without card graphics. After some consideration
of potential tools we decided to write a deck "compositing" tool. Think LaTeX for
T.I.M.E Stories decks.  The result is a command line Python application that 
"builds"  T.I.M.E Stories card images from a textual (XML) representation of a 
deck. A major advantage of this approach is that we can "rebuild" the cards for 
a deck from their source text and image assets at any time.

What can it do?
***************

The Heresy, Python-based toolset is capable of laying out and rendering cards in 
various forms.  It is capable of generating individual PNG files for the top and
bottom of each card in the deck as well as Letter and A4 format PDF files of the
whole deck and the composite PNG file 'deck' images used by Tabletop Simulator
from the same XML source.  The tool has the ability to generate cards padded out
with the bleeding region needed for printing services like makeplayingcards.com.

How does it work?
*****************

The tools work on a 'deck' file, an XML formatted description of a T.I.M.E Stories
deck.  A deck contains lists of cards (e.g. Items, plans, characters, etc).  Each
card contains a set of text or image blocks that can be sized, rotated and placed
on the card.  Individual items have the concept of 'depth' which controls the
compositing order of the various card elements. Finally, every type of card has
a "default" card that it can inherit from as base layer.  This makes it very easy
to do things like add the item number to all item cards by adding it to the 
default card with a depth that ensures it is visible over (or under) other content.

The deck XML schema describes text styles and images as "assets" that can be 
referenced by name on the cards. One can even refer to subsections of a source 
image file as an image, making it very simple to crop out portions of a larger 
image (or a single image of a location into cards) and use them in additional 
places. We often import the Space Cowboys' SDK at the start of a new scenario 
for consistency with other decks.

At the heart of the deck is the representation of a card face. Every card has 
a top and a bottom face with a different collection of renderable items. The 
final rendered card is a composite of the current card items and any items 
from the default card for the current card type.  The items from the card and 
the default card are merged and sorted by depth (layers) that determine the 
order of the item compositing.  There are rectangle, image and text items. The 
text item plays a key role as much of the story is told through these items. 
The text item allows for the application of "styles" to sections of text that 
are common over all cards (e.g. all item references should be bold and green).
Text can include macros that substitute for actual card names, numbers, letters, 
etc.  These are computed when the card is rendered and help make sure that moving 
things around leaves most links intact. Image objects can even be embedded
(inline) into the text of a text item.  In short enough functionality to cover 
the needs of the Heresy story.

Prerequisites
*************

These tools are a work in progress, but if you are up for a challenge, we have 
opened up the tools so others can try to use them. The tools require Python 3.x 
with PySide6 to run.  At present, the primary tool is a command line deck builder.
There is also a GUI deck builder being written, but folks working on Heresy found 
we did not need more that the command line tool. The tool itself is available 
in source code form via git (`randall-frank/heresy-card-builder: Tools for 
manipulating T.I.M.E Stories card decks 
<https://github.com/randall-frank/heresy-card-builder>`__) and most recently, 
the tools can be installed in your own Python interpreter via: 

.. code-block:: bash

    pip install heresycardbuilder

|

| `PyPi link <https://pypi.org/project/heresycardbuilder/>`__.  The Heresy XML deck 
| source was developed on github, and is also publicly available 
| at `heresy-assets <https://github.com/randall-frank/heresy-assets>`__.

|

* Have fun!  The Heresy Team
