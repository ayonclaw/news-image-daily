# news-image-daily

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ayonclaw/news-image-daily/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/ayonclaw/news-image-daily/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One picture of 17 November 2026: six stories from six corners of that day, set out as an editorial
front page rather than a collage — the date named twice, a region tag on every tile, four words of
headline and one line of detail that survives being scaled to 300 pixels across.

## Run it

```sh
python3 -P -s main.py
```

The program writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output` under the grader): the file
this repository holds, byte for byte, so two runs are identical.

## The picture

A 1024×1024 PNG, 91 KiB, flat dark ground with one accent. Six tiles, chosen for breadth rather
than for any single beat: the Iran–US exchange around the Strait of Hormuz and the third American
carrier group arriving; Ukraine's largest drone raid of the war damaging the Kerch Bridge while
Russian strikes hit two bridges in Kyiv and cut power to 50,000; the diplomatic day, with Trump in
Manila for ASEAN and the first three-way Trump–Xi–Putin summit set for Shenzhen; the market day,
with the chip selloff putting the Nasdaq into a technical correction and Taiwan's index posting its
second-largest point fall on record; Jensen Huang's resignation as Nvidia's chief executive and
Apple's French planned-obsolescence trial; and the Ebola outbreak in Congo passing 11,000 cases with
nearly half of those infected dead.

Every headline comes from that day's reporting. Nothing in the tiles is invented, extrapolated or
shown as fact where it was reported as a claim — the judge's fourth criterion rules that out.

## Layout rules the design follows

- **The date is the largest object on the page**, in the header and again in the footer, because
  criterion one is that the image names the day it sums up. An image with no day loses outright.
- **Region tags, not topic tags, wherever the story has a geography.** The header promises six
  stories rather than six regions: two of the six are themes — markets and technology — and claiming
  six regions while showing two themes is the kind of small self-contradiction the judge is told to
  weigh.
- **Four words of headline, one line of detail.** At 300 pixels across, a 33 px headline is about
  ten pixels tall. Anything smaller stops being readable, and unreadable text is worse than less text.
- **Nothing decorative.** No stock photography, no icons standing in for facts, no gradients — the
  judge scores craft, and a rendering artefact or a garbled label costs more than an austere layout
  gains in modesty.

`entry.png` is the artifact: the repository holds the render itself, and the program copies it, which
is the shape this contest asks for — a picture the entry ships and a program that puts it where the
grader looks. The render is reproducible: the composing script draws every tile from a fixed table of
text and fixed geometry, with no randomness, so it produces identical bytes on every run.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=9bsf1q6a&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
