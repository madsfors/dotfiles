# Accessibility & Contrast

Contrast is always measured between a **foreground color** (text, icon, or UI element) and the **background color** it sits on. When checking contrast, identify the background the element will be rendered against, typically the nearest parent's background color.

**Report, don't repaint.** When a check fails, report the failing foreground/background pair, its measured WCAG ratio, and the requirement it misses, then leave the colors unchanged. A project's colors are a design decision; only apply the fix below when the user asks for one. If APCA is also reported, label it advisory and name the calculator and version used.

## WCAG 2.2 thresholds (normative for WCAG 2.x conformance)

WCAG 2.2 uses a relative-luminance ratio. Use these thresholds when evaluating or claiming WCAG 2.2 conformance.

| Content Type | AA | AAA |
| --- | --- | --- |
| Normal text (<24px / <18.5px bold) | 4.5:1 | 7:1 |
| Large text (>=24px / >=18.5px bold) | 3:1 | 4.5:1 |
| UI components & graphical objects | 3:1 | n/a |

WCAG defines "large text" in points: 18pt ≈ `24px`, or 14pt bold ≈ `18.5px`.

## APCA (advisory only)

APCA is an evolving perceptual contrast model, not the normative algorithm for WCAG 2.2 conformance. It may provide useful design evidence, but do not use simplified universal Lc thresholds or present APCA as a WCAG pass/fail result. Use a named, versioned calculator and its full font-size/weight guidance. Report the implementation and result separately from WCAG.

APCA's Lc value is signed: positive means dark text on a light background, negative means light text on a dark background. Preserve the sign in reports even when a tool also shows the absolute magnitude.

## Fixing contrast with oklch (on request)

In hex/rgb, fixing contrast means trial and error across three channels. In oklch, lightness (L) is the clearest first lever: adjust the L distance between the foreground and its background while preserving C and H when possible:

```css
/* Candidate pair: measure this rendered foreground/background combination */
color: oklch(0.65 0.08 250);      /* foreground */
background: oklch(0.95 0.02 250); /* background */

/* Candidate fix: darken the text, then recalculate WCAG contrast */
color: oklch(0.3 0.08 250);       /* foreground: more L distance */
background: oklch(0.95 0.02 250); /* background: unchanged */
```

Mid-lightness backgrounds can limit the achievable contrast, but OKLCH lightness alone does not establish a pass or failure. Calculate the converted, rendered pair.

Adjust L first, then remeasure the rendered foreground/background pair. Chroma and hue can still affect the converted color, gamut mapping, and measured contrast; reduce C when needed to keep the adjusted color in gamut.

## Lightness is a starting heuristic, not a measurement

Use a larger OKLCH lightness gap as a first adjustment, then calculate the actual WCAG ratio for the rendered pair. Do not invent a ratio or APCA Lc value from L alone.

## Light vs dark color detection

Do not use a fixed OKLCH-lightness cutoff to choose foreground text. Measure both candidate foreground/background pairs with the required WCAG algorithm, then inspect the result in context.

## Hue drift detection

To detect hue drift in an existing HSL palette:

1. Convert each step to oklch
2. Compare the H values across steps
3. If the hue spread is greater than 10°, the palette has visible drift

```css
/* HSL blue ramp: hue shifts toward purple */
hsl(240, 80%, 20%)  →  oklch H ≈ 269
hsl(240, 80%, 50%)  →  oklch H ≈ 267
hsl(240, 80%, 90%)  →  oklch H ≈ 285  /* shifted 18° */
```
