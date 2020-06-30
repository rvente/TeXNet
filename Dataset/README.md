This is our dataset, mined from January 2018's arXiv source code.
`normalized_out.txt` contains upwards of 500 thousand examples of LaTeX mathematical
expressions, normalized. `im2latex170k.txt` is the same raw data also cleaned to eliminate
non-compiling examples and to facilitate deep learning tasks. That set of experessions is
the source of the training, test, and validation sets.

Additionaly, `filtered_sequences.txt` offers expressions that render with KaTeX. This is the
cleaned dataset you probably want to start with. I also removed really long sequences there too.

![Preprocessing](https://raw.githubusercontent.com/rvente/TeXNet.ai/master/Final-Paper/assets/harvest.svg)

We contribute substantially to the preprocessing pipeline including reducing false
matches (for mathematical expressions) and unifying LaTeX patterns for normalization.
As such, we only need the formula2image scripts in the data-gen-utils repository.

The generated images are on [Kaggle](https://www.kaggle.com/rvente/im2latex170k).

Special thanks to [Brian Newbold](http://bnewbold.net/), an internet archivist, who provided
the raw form of the data we pre-processed. Details in the paper.

## Using the cleaning script

Be sure to `npm install` and run `node filterNonRendering.js > <destination-file>`. The file read in
will be `normalized_out.txt` by default, changable at will.
