# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

static HTML/CSS (GitHub Pages). Framework optional if it still ships as static files; prettier result preferred over preserving pandoc markup.

## Users

Primary: makers at a soldering workbench assembling a HUMA board (check parts → solder → burn bootloader → use). Secondary: people evaluating the project before they build.

## Product Purpose

HUMA (HUman Madeable Arduino) is an open-source, Arduino-compatible board designed so builders can solder it themselves, like a radio kit. The site’s job is to make that assembly path clear and safe.

Success: a builder can follow the Korean guide and BOM without getting lost, and finish a working board.

## Positioning

Solder-it-yourself Arduino-compatible hardware (Freeduino lineage), not a preassembled commercial board. The differentiator is human-buildable assembly with documented steps and parts.

## Operating Context

Workbench with soldering iron, parts from the BOM, PCB photos as visual checkpoints, Arduino IDE / ISP for bootloader. Docs live under `site/` and are meant to publish on GitHub Pages.

## Capabilities and Constraints

- Korean assembly guide (`site/index.html`) and parts list / price table (`site/huma_bom.html`).
- Real step photos in `site/pics/` must remain the visual evidence.
- Preserve Korean copy meaning, step order, BOM data, and technical claims; redesign structure, typography, and layout only.
- Must remain static for GitHub Pages hosting.
- Open hardware; circuit/docs under CC BY-SA; no liability for damage from building or use.

## Brand Commitments

- Name: HUMA (HUman Madeable Arduino / Freeduino-based).
- Voice: practical workshop Korean; warnings and notes stay plain and safety-first.
- Assets: existing PCB and assembly photos; do not invent marketing claims, customers, or specs.
- Visual preference (user-chosen): category-standard clean technical documentation, craft bar set by Adafruit Learn and SparkFun tutorials. No experimental/quirky art direction.

## Evidence on Hand

- Assembly photos and PCB shot: `site/pics/`
- Source docs: `doc/instruction.md`, `doc/partlist.md`
- Eagle / gerber / project files in repo; GitHub: https://github.com/suapapa/HUMA
- External references already linked (Freeduino, soldering tutorials, bootloader notes)

Do not fabricate testimonials, kit sales numbers, or unsupported specs.

## Product Principles

1. Workbench clarity over marketing polish: steps and photos lead.
2. Safety and notes stay visible without drama.
3. Parts truth is sacred: BOM values and quantities are not restyled into fiction.
4. Static, fast, readable on phone at the bench and on desktop.
5. Open-hardware honesty: license and disclaimer stay present.

## Accessibility & Inclusion

Readable contrast for long reading; images need meaningful alt text; works on narrow phone viewports at the bench.
