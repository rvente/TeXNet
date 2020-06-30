/*
 * Ralph 'Blake' Vente
 * Filter out non rendering expressions from source corpus
 * Usage: node filterNonRendering.js > dest
 */

const fs = require("fs");
const katex = require("katex");
const readline = require("readline");

const file = readline.createInterface({
  input: fs.createReadStream("normalized_out.txt"),
  output: process.stdout,
  terminal: false,
});

successes = 0;
failures = 0;
file.on("line", (line) => {
  if (rendering(line)) {
    console.log(line);
    successes++;
  } else {
    failures++;
  }
}).on('close', () => {
  console.error('good', successes, "bad", failures)
})
;

function rendering(el) {
  try {
    katex.renderToString(el, {
      displayMode: false,
      macros: {
        "\\RR": "\\mathbb{R}",
      },
    });
    return true;
  } catch {
    return false;
  }
}
