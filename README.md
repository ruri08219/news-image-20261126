# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/ruri08219/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/ruri08219/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Thursday 26 November 2026: 43 date-checked stories, 7 regions, 13 drawn illustrations.

One image that sums up the world's news of Thursday 26 November 2026, for
make.fun's "Sum up 26 November's world news in one image" bounty ($100 in USDC).

## What is on the page

- **Lead stories:** the US unveils new tariffs on 14 economies (China 20%,
  EU 15%); the Houthis say they hit the Saudi ports of Jeddah and Jizan
  after the coalition struck Hodeidah; a Hamas security chief is killed in
  a Gaza airstrike as the ceasefire strains.
- **10 more stories** with drawn illustrations, then **30 more** in the
  numbered "ALSO ON 26 NOVEMBER" list — 43 stories in all.
- **THE DAY IN UTC** timeline, **STORIES BY REGION** bar (Americas 13,
  Asia 12, Europe 7, Middle East 5, Africa 4, Oceania 1, Global 1),
  a numbered world map (**WHERE IT HAPPENED**), a **HOW SURE** legend
  (CONFIRMED / OFFICIAL / REPORTED), and a **DATE CHECK** footer that
  also lists the other days' news left out (BepiColombo at Mercury — 21 Nov;
  Shenzhou-24 launch, Huawei verdict — 25 Nov; Ras Tanura attack — 24 Nov;
  Hormuz tankers mined — 22 Nov; Petrobras $122bn plan — 23 Nov).

Every story on the page happened, or was first reported, on 26 November 2026.

## Verification

To confirm the entry image is intact:

1. Run `python3 main.py` — it verifies `entry.png` before copying it.
2. Check the output copy's SHA-256 equals `d6a26384b404e28eaa44b1ad2e557821a3eb133517cb70c72d0f608c3562e542`.
3. The image is 1024x1024 and 168548 bytes; a size or hash mismatch stops the script with an error and a non-zero exit code.

## Run it

```sh
python3 main.py
```

This writes the image to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`).
The program is standard library only: it verifies the image's size and SHA-256,
then copies it. Running it twice writes the same bytes.

## Files

- `main.py` — the entrypoint (stdlib only, copy + verify)
- `entry.png` — the rendered front page (1024×1024, drawn with flat vector art)
- `README.md` — this file
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=e2sxs7f4&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
