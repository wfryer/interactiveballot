# Interactive Ballot

The homepage for [interactiveballot.com](https://interactiveballot.com).

Interactive Ballot helps voters build their own nonpartisan, clickable voter guide from their official sample ballot. Every candidate and ballot question links to good information, so people can learn about everyone before they vote.

## Part of Heal Our Culture

Interactive Ballot is a [Heal Our Culture](https://healourculture.org) project. The goals:

- Reduce political polarization.
- Help voters arrive at the polls better informed.
- Encourage candidates to use their websites to explain their ideas, experience and background. When a candidate has no website, the guide says so plainly.

## How to use the prompt

1. Find your official sample ballot. The homepage has a state finder to help.
2. Download it as a PDF.
3. Copy the prompt from [interactiveballot.com](https://interactiveballot.com).
4. Open a new chat in an AI tool with web search (Claude Pro is what built these), attach your PDF and paste the prompt.
5. Click through every link and check it against your official ballot before you rely on it.
6. Share your ballot with #InteractiveBallot.

## What's here

- `index.html`: the homepage. One self-contained file, no frameworks.
- `stallings-2025/`: the archived Town of Stallings, NC ballot for November 4, 2025, with its sample ballot PDF.
- `tools/build_ballot.py`: generates the Union County, NC 2026 ballot page. Run `python3 -I tools/build_ballot.py out.html`. The live Union page is at [wfryer/interactive-ballot-union-nc-2026](https://github.com/wfryer/interactive-ballot-union-nc-2026).

## Nonpartisan disclaimer

Interactive Ballot is nonpartisan and experimental. It is not affiliated with any candidate, campaign, party or election office. It does not endorse anyone or tell anyone how to vote. Links can change, so always confirm against your official ballot and your election office.

## Credit and license

Created by Wes Fryer ([ai.wesfryer.com](https://ai.wesfryer.com)). Released under the MIT License. See `LICENSE`.
