Project Title
=============

Our title is *Hunter TeXNet* following the tradition of LeCun's *LeNet*
Neural Network architecture [@lecun1998gradient 7] but our investigation
will not be limited to these models.

Description
===========

Previous Work
-------------

The prospect of accurately transcribing mathematical expression into a
markup representation is enticing because it opens the doors for
bringing new life to old mathematical texts or those for which the
source code is unavailable.

A Harvard project called *What you get is what you see*
([Wygiwys]{.smallcaps}) by [@deng2016you] details strategies for machine
translation of mathematical notation using an attention-based
encoder-decoder neural model. Notably, the researchers were interested
in the influence of markup alone on the efficacy of a model --- without
the user providing explicit information about underlying grammars
[@deng2016you 1].

Objectives
----------

Our goal is to build on previous work with a system that exploits the
recursive nature of mathematical language and that has high invariance
to the typeface used. We hope to achieve this by combining an Optical
Character Recognition (OCR) model, that operates on atomic tokens, while
an outer model parses the input and segments the image into these
tokens. Our motivation behind this line of reasoning is the view of
Mathematics as a Chomsky Normal Form language [@miller1998ambiguity]. We
explain this more in our Synthetic Example.

Viewing this as two separate problems means we can isolate learning the
grammar from character recognition complexity. This idea isn't new: one
essential component of [Wygiwys]{.smallcaps} provides spatial
understanding which is factored into later layers of their Neural
Network (ANN) [@deng2016you 4], but the final model does not explicitly
separate grammar from characters. We intend on de-coupling the concerns
to open up doors for grammar model reuse. Then, different typefaces may
be learned separately by the OCR model.

As mentioned in [@deng2016you], the model is sensitive to what we choose
as an "atomic token." We will build on their findings. Also, they
mention that the model is vulnerable to ambiguities in LaTeX itself ---
that different inputs may result in the same output. We will also use a
normalized form of LaTeX to mitigate this issue. Another similarity is
that we will generate `png` images and do pre-processing using
`imagemagick`'s `convert` utility.

### Innovations

Our research differs because we will employ models to learn the
underlying grammar of mathematical notation and character recognition
explicitly and independently.

We want to use this specialization to segment the image and dispatch an
OCR model on specific subsets of the image. This may allow for us to
translate expressions of arbitrary length, complexity, and typeface with
no reduction in performance.

By partitioning this task, we also hope to reduce dependency on Neural
Networks. Tentatively, we're investigating using an ANN with Long Short
Term Memory architecture (LSTM) for grammar because of prior research:
LSTM models are able to derive meaning in context, which is important
for grammar recognition [@deng2016you 1]. Then, we explore Support
Vector Machines with kernel functions for OCR for a more compact model
with comparable performance because of their history with OCR tasks.

### Synthetic Example

When considering the following formula, we wouldn't want our model to be
confused --- is the 0 stacked on top of the 1 or are they on separate
lines? (text-based rendition of example, see proposal pdf document).

```
     /          \
    |   0    2   |
f = |            |
    |   1    3   |
     \          /
```

 To us it's intuitive to break up the task of understanding
this expression into two distinct steps: first, recognize that we are in
some form of a nested environment, handle it (the outer { in this case),
then recursively parse the next internal portion (in this case, the
first line of the nested structure).

Instead of taking the expression in as a whole, we hope to build a
system that pays attention to specifically the portions of the text that
are "outer" before recursively translating the inner function. As this
is both of our first experiences with OCR or machine translation, we
hope to learn much more about ANN's and other models capable of parsing
recursive structures. Hopefully then, we be able to translate this
intuitive reasoning into a model that uses this assumption of recursive
structure for performance benefits.

Tasks and Roles
===============

Of course distribution of work at this stage is tentative and subject to
any new findings. Blake will complete the first 3, and Alex will
complete the second 3.

1.  Mine a greater number of examples from real world text, expanding
    the corpus by doubling the number of images compared to the Deng
    database.

    1.  Find the examples that the Harvard model cannot accommodate.

    2.  Find real-world data to augment the Harvard database.

2.  Create model to learn the spatial grammar of arbitrary markup.

    1.  Recursively search the image, assigning semantic markup for
        every child node in the search.

    2.  Recognize "base cases", that is, segment the image into atomic
        tokens for dispatch to the OCR recognizer.

3.  Create a high-performance OCR engine that recognizes characters.

    1.  Begin with the standard Computer Modern typeface in LaTeX (and
        all of its mathematical fonts).

    2.  Investigate the difference in performance between a single OCR
        engine responsible for the token translation of all typefaces we
        test compared to individual OCR models for each typeface.

Topics
======

Machine Learning
----------------

1.  Optical Character Recognition (OCR)

2.  Image Segmentation / Document Recognition

3.  Artificial Neural Network (ANN)

    1.  Natural Language Processing (NLP)

    2.  Long Short Term Memory in ANN's

    3.  Recurrence and Convolution in ANN's

4.  Support Vector Machines (SVM)

Deliverables
============

Required Objectives
-------------------

At the submission deadline, we will have the following prepared:

1.  all data generated and normalized, building on the work of the
    Harvard team;

2.  all source code containing our finished models and documentation;

3.  research paper outlining the intricacies of our models and their
    performance on generated examples;

4.  a live demo of the model; and

5.  a 2 minute video.

Stretch Goals
-------------

Minimal interactive web front-end where a user will be able to upload an
image of a mathematical expression and receive the LaTeX code associated
with it. This would also serve as the platform for one of our demos.

Evaluation
==========

We will evaluate our models with a confusion matrix, Hamming distance,
and statistic where appropriate. Similarly to the Harvard team, we use
the perplexity metric, common to machine translation tasks
[@jelinek1977perplexity 1]. We will pay special attention to evaluating
how well our model handles nested structures compared to the models in
[Wygiwys]{.smallcaps}.
