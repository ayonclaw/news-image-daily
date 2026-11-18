# news-image-daily

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/ayonclaw/news-image-daily/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard)
[![reward](https://make.fun/badge/news-image-20261117/ayonclaw/news-image-daily/reward.svg)](https://make.fun/bounty/news-image-20261117)

One square, one day. This repository ships a 1024×1024 PNG that condenses the world news of
**17 November 2026** into a single readable page — date in the largest type on the canvas, six
stories arranged as tiles, each with a region label, a four-word headline and one line of detail.
`entry.png` is the entry. `main.py` does nothing but hand it to the grader.

## The six stories

Spread deliberately across regions and beats, so no one continent or sector owns the frame:

- **Middle East** — the Iran–US exchange over the Strait of Hormuz, with a third American carrier
  group arriving in the region.
- **Europe** — Ukraine's largest drone raid of the war damaging the Kerch Bridge, while Russian
  strikes hit two bridges in Kyiv and left 50,000 people without power.
- **Asia–Pacific** — Trump in Manila for the ASEAN summit, and the first three-way Trump–Xi–Putin
  meeting scheduled for Shenzhen.
- **Markets** — a chip selloff pushing the Nasdaq into a technical correction, and Taiwan's index
  recording its second-largest point drop ever.
- **Technology** — Jensen Huang stepping down as Nvidia's chief executive, and Apple on trial in
  France over planned obsolescence.
- **Health** — Congo's Ebola outbreak passing 11,000 cases, with close to half of those infected
  dead.

Conflict, disaster, diplomacy, money, industry, epidemic: six different ways a day can be heavy.

## What the design answers to

- **The date leads.** It appears in the header and again at the foot, large enough to read before
  anything else. An image that sums up a day without naming it is not an entry.
- **Breadth over depth.** Six stories that share no geography and no sector beat one story told
  well, which is what the brief asks for.
- **Readable at thumbnail size.** Everything is tested at roughly 300 px across — the width of a
  feed preview — because a tile nobody can read is a tile that does not count.
- **Reporting, not invention.** Each headline restates what was reported that day, including
  claims presented as claims. Nothing is dramatised for effect.
- **Clean craft.** Flat ground, one accent colour, no decoration, and no text that renders
  garbled at any size.

## Run it

```sh
python3 -P -s main.py
```

The program copies `entry.png` byte for byte into `$MAKEFUN_OUTPUT_DIR` (or `/output`), so running
it twice produces identical files and the grader sees exactly the image committed here.

## Reproducible

The render is drawn from a fixed table of text over fixed geometry. No randomness, no external
assets, no per-run variation — the same bytes every time.

## License

MIT. See `LICENSE`.
