---
name: HUMA
description: Clean open-hardware assembly docs for GitHub Pages
colors:
  bg: "#f4f6f8"
  surface: "#ffffff"
  ink: "#1a2332"
  muted: "#4a5568"
  line: "#d5dce6"
  accent: "#c45c26"
  accent-ink: "#9a3f12"
  accent-soft: "#fff3ea"
  warn-bg: "#fff1eb"
  warn-ink: "#8a2e0c"
  note-bg: "#eef3f8"
  note-ink: "#1e3a5f"
  code-bg: "#eef1f5"
  dark-bg: "#12171f"
  dark-surface: "#1a2230"
  dark-ink: "#e8edf4"
typography:
  body:
    fontFamily: "Gowun Dodum, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 400
    lineHeight: 1.7
  display:
    fontFamily: "Gowun Dodum, Apple SD Gothic Neo, Noto Sans KR, sans-serif"
    fontSize: "clamp(1.85rem, 3.2vw, 2.55rem)"
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  mono:
    fontFamily: "Source Code Pro, ui-monospace, Menlo, Consolas, monospace"
    fontSize: "0.9em"
rounded:
  sm: "4px"
  md: "8px"
  lg: "10px"
spacing:
  sm: "0.65rem"
  md: "1rem"
  lg: "1.75rem"
  xl: "2.5rem"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "#ffffff"
    rounded: "{rounded.md}"
    padding: "0.55rem 1rem"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "0.55rem 1rem"
  callout-warn:
    backgroundColor: "{colors.warn-bg}"
    textColor: "{colors.warn-ink}"
    rounded: "{rounded.lg}"
  callout-note:
    backgroundColor: "{colors.note-bg}"
    textColor: "{colors.note-ink}"
    rounded: "{rounded.lg}"
---

## Overview

HUMA docs use a category-standard clean tutorial layout (Adafruit Learn / SparkFun craft bar): sticky top nav, sticky sidebar TOC on desktop, calm reading column, photo figures as assembly checkpoints, and callouts for warnings and notes. Static HTML/CSS for GitHub Pages.

## Colors

Cool paper ground (`#f4f6f8`) with charcoal ink and one solder-amber accent (`#c45c26`) for CTAs, active TOC, and warning affinity. Notes use cool slate blue. Dark mode flips surfaces via `prefers-color-scheme` while keeping the same accent role.

## Typography

Self-hosted [Gowun Dodum](https://fonts.google.com/specimen/Gowun+Dodum) (Regular only) for UI and body. Hierarchy uses size and color, not bold weights (`font-synthesis: none`). Source Code Pro for `code` and numeric table cells. Body text and figures share the full content column width.

## Layout

Max content width ~1120px. Desktop: 220px TOC rail + fluid main. Mobile: single column with TOC as a compact panel above content. Hero is a 2-column split (copy + PCB photo) collapsing to one column under 900px. Nav height capped at 64px (56px mobile).

## Elevation & Depth

Flat system: borders and surface contrast only. No drop shadows on figures or tables.

## Shapes

Consistent soft radius: controls 8px, figures/callouts/tables 10px. No pills except as accidental full-round avoidance.

## Components

- **Nav:** brand left, page links + GitHub; current page uses accent-soft chip.
- **TOC:** sticky; active link via IntersectionObserver (`is-active`).
- **Buttons:** primary solid accent; secondary bordered surface.
- **Figures:** bordered surface plates with captions.
- **Callouts:** warn (safety) and note (tips) with labeled strong heading.
- **Tables:** hairline rows, muted header band, tabular nums for quantities.

## Do's and Don'ts

- Do keep Korean copy, step order, BOM data, and real `pics/` photos.
- Do keep contrast WCAG AA; muted text stays `#4a5568` or darker on light ground.
- Don't add marketing eyebrows, version stamps, or scroll cues.
- Don't invent kit prices beyond the documented ~15000원 note.
- Don't mix a second accent color or warm-cream craft palette.
