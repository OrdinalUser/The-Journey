---
authors:
  - Skyte
slug: collatz_conjecture_visualizer
draft: false
categories:
  - Uncategorized
tags:
  - Python
  - Math
  - Visualization
date:
  created: 2026-02-13
  updated: 2026-02-14
links:
  - Wikipedia: https://en.wikipedia.org/wiki/Collatz_conjecture
---

# Collatz Conjecture Visualizer

![Collatz trajectories](../../assets/thumbnails/collatz_conjecture_visualizer.png)

How long until any number reaches 1? A quick Plotly exploration of one of
math's most stubborn open problems. An example one-off to test out MkDocs.

<!-- more -->

## The idea

Pick any positive integer. If it's even, divide by 2. If it's odd, multiply
by 3 and add 1. Repeat. The conjecture says you'll always reach 1 — but
nobody's been able to prove it.

I wanted to see what the trajectories actually *look like* for a range of
starting numbers, so I threw together a quick visualizer.

## The code

```python title="Collatz Sequence Visualizer"
--8<-- "docs/assets/src/collatz_conjecture_visualizer.py"
```

![Plot Result](../../assets/thumbnails/collatz_conjecture_visualizer.png)

## What I found

Most numbers collapse to 1 pretty quickly, but some shoot up wildly before
coming back down. The log-scale plot makes this clear — you get these
beautiful cascading arcs.

A few things that stood out:

- **27** takes 111 steps and peaks at **9232** before settling. For such a
  small starting number, that's a wild ride.
- Numbers just above powers of 2 tend to resolve almost instantly (they just
  halve their way down).
- The overall shape on a log scale looks almost fractal.

## Takeaway

Sometimes the simplest rules produce the most chaotic behavior. This took
about 20 minutes to write and I spent way longer just staring at the plots.
