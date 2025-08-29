Questions and Help...
#####################
:date: 2017-12-30 21:37
:author: rjfrank
:slug: questions-and-help
:status: published
:illustration: box_path.jpg

With the opening of the source code to Hersey being made public, we encourage questions be handled
via the Github `"issues" <https://github.com/randall-frank/heresy-assets/issues>`__ section for the game.   Previous to the open hosting of the sources, we had
a few questions posted and answered on this site.   We include them here for reference.

The Questions
*************


Ellen: Buying physical cards
============================

September 3, 2018 at 4:14 am

When you plan on purchasing the cards through the makeplayingcards.com store, what card size would you suggest? Also, what is the average cost of a full deck?

(We figured our own numbers for this but we want to save everyone else the initial confusion 🙂 )

FrogBoots: Reply
----------------

September 6, 2018 at 12:47 am

Hello,

I do wish their website would allow us to put this on their storefront as it would save you a lot of time. Unfortunately they force us to charge a profit to do so and we cannot take any money for Heresy because we used the public Space Cowboys SDK and it will not allow us to charge for it. Anyway to answer your question. The last time I ordered a deck, I ordered it like this:

(300gsm (Smooth)) (MPC Card Finish) Design Your Own Tarot Cards Playing Cards

2.75″X4.75″ (70×120mm) (78 Cards)Packaging: Shrink-Wrapped $16.15

(300gsm (Smooth)) (MPC Card Finish) Design Your Own Tarot Cards Playing Cards

2.75″X4.75″ (70×120mm) (69 Cards)Packaging: Shrink-Wrapped $15.85

So I split the deck into one 78 card deck and a second 69 card deck. The sizes and finishes are shown above. I think shipping was around $12, so ~$44 for a deck, shipped. I think we got the deck in about 10 days. If you do use them, make sure you get the proper front and back faces lined up first. It took a little work, but we were very happy with the results.
Does that help??


Annemarie van der Harst: Printing cards
=======================================

October 3, 2018 at 7:28 pm

I really like how you developed your own artwork for this fan scenario. I’m in the middle of wrapping up my own scenario (after 1.5 year of work, phew), but I’m looking forward to having a go at Heresy as well. Is part 2 still coming out this year?

I also have a practical question regarding printing. I was looking into using MPC for printing my fan scenario, but I notice that they suggest a safe area besides the regular bleeding area, warning you not to put any important info outside the red dotted line. Was the space between safe area and the bleeding area ever (or often) cut off in your deck? Judging by the way your cards came out in the picture above, it appears that at least for the base, the space outside the safe area was nicely kept. It would be a shame however if the cut is regularly off since that would mess with the nice panoramas of the scenes. I’m curious about your experience, hopefully you can help.
Kind regards and good luck on the progression of Heresy.

FrogBoots: Reply
----------------

November 1, 2018 at 2:25 am

Sorry for the delay in getting back to you Annemarie, I missed your original post.

We’d love to play your scenario, let us know when its ready to play. The Heresy story was originally planned to span three scenarios, and I still think that is the plan. We are actively working on 2 (have locations, a basic storyline, etc), but we have a long way to go (no art yet). If you asked me right now, I think late 2019 is probably the best guess. We do not have a hard timeline. It will come out when we like it. I can say that we shift to ancient Greece and continue play from the end of the first scenario.

On the MPC question, the best answer might be to look at the Python code in the git repo. We start with cards that are 825×1425. We then “smear” the outer rows/columns out 36 pixels, making a card that is 897×1497. For example along the horizontal axis we have 36 pixels of smear+825 pixels of content+36 pixels of smear = 897 pixels total. After printing, you never see the 36 pixel border (or see very little of it). Just make sure to stay away from the corners as they are rounded. IMHO, I would leave a 10-15 pixel internal border inside of the 825×1425, so lay out a 825×1425 card and don’t put any critical content in the outer 10 pixels. Embed that in a 897×1497 card where the extra pixels just replicate the outer rim and I think you will be pretty happy. We’ve used this scheme to print 4-5 different versions of Heresy and have never been disappointed. Does that help?
Good luck on your scenario as well. Half of the fun is in the writing!

Vladimirs Kacs: Card clarification
==================================

October 27, 2018 at 12:10 pm

I would like some clarifications on cards:

Isabel and Gaspar have gender based abilities, do they apply to opponents, allies or both?

Francisco’s ability says it costs TU. Does it cost “blue” TU (Just for Francisco) or “black” TU (for the whole party)?

Thank you for making this.

FrogBoots: Reply
----------------

November 1, 2018 at 2:43 am

Vladimirs, I hope you are enjoying the game. Sorry the instructions were unclear.
The intent was that Isabel and Gaspar’s abilities apply when the opponents are of the opposite gender. So if Gaspar was participating in a challenge where the opposing character is female, he would get a boost. I do not believe there are any challenges where the opponents are mixed (and I think we explicitly clarify the “interesting” cases). If there are any such mixed cases, I would probably suggest the benefits could be applied.

With Francisco, there is no additional TU cost involved in him using his ability. What you give up is the ability for him to use his natural “attack” during the TU that he uses his ability. For example, if he and Gaspar were in a combat challenge. In one regular group TU, Francisco could choose to (for the die roll in that round) not roll his attack (1 combat) and instead for that round Gaspar could attack with his natural 2 combat, but would act as if he had 5 (3+2) shields for that roll. If Gaspar were to take damage, Francisco would take the same damage as Gaspar takes. Basically, you are giving up Francisco’s attack roll during a specific TU and increasing the defense of another character on the same card (and sharing the damage if the character he protects gets hit). In any case, no additional TU cost (blue or black) is involved.

Does that help clarify things a bit?
If you have wording that might help clarify these points, please let us know and we may include it in a future regen or at least include it in the deck source code which we may release in the future.
You are most welcome, we really enjoyed putting Heresy together.

David: Puzzle hint
==================

December 30, 2018 at 12:06 am

Could you offer a hint about the Pink Square.

We’ve acquired Items 28, 29, 30, 31 and 11, 12, 13, 23.

FrogBoots: Reply
----------------

December 30, 2018 at 12:51 am

Hello,

First, thanks for playing, we hope you are enjoying the game. To answer your question, the locked door (pink square) is key to advancing into the next part of the game. Folks do seem to get stuck there. Let’s start with this: the four pieces of stained glass (items 28, 29, 30, 31) hold the key to opening the door. Some other players have suggested making it more obvious that solving the puzzle in those four items is needed to get past that door. If we revise the deck again, we will probably add that hint at least. I’ll go a little further and suggest that you could shine some light through those pieces of stained glass…

If you are still stuck and want an additional hint, let me know how to send you a private message and we’ll get you on your way.

Again, thanks for playing!

Mark Hughes: Card box template
==============================

June 7, 2021 at 10:55 am

Hi There,

Love the look of Heresy.

I’m keen to print a box to keep the cards in,
Do you have box template at all?

Many thanks

FrogBoots: Reply
----------------

January 14, 2025 at 4:25 pm

Unfortunately, we do not have a box template. We have done some box artwork that might be useful if one were to use a box configuration close to that of the standard T.I.M.E Stories boxes Box Art.

I should also note that all of the assets from the game are now available publicly from github (https://github.com/randall-frank/heresy-assets). You might find some useful imagery there.

BTW: if you happen to create such a template and are willing to contribute it to the project, please let us know. The ‘issues’ section of the github repo is probably the best place for that.

