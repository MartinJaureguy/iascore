---
name: Synthetic Intelligence Evaluator
colors:
  surface: '#131318'
  surface-dim: '#131318'
  surface-bright: '#39383e'
  surface-container-lowest: '#0e0e13'
  surface-container-low: '#1b1b20'
  surface-container: '#1f1f25'
  surface-container-high: '#2a292f'
  surface-container-highest: '#35343a'
  on-surface: '#e4e1e9'
  on-surface-variant: '#ccc3d8'
  inverse-surface: '#e4e1e9'
  inverse-on-surface: '#303036'
  outline: '#958da1'
  outline-variant: '#4a4455'
  surface-tint: '#d2bbff'
  primary: '#d2bbff'
  on-primary: '#3f008e'
  primary-container: '#7c3aed'
  on-primary-container: '#ede0ff'
  inverse-primary: '#732ee4'
  secondary: '#aeecff'
  on-secondary: '#003641'
  secondary-container: '#00d9ff'
  on-secondary-container: '#005b6c'
  tertiary: '#c6c6c8'
  on-tertiary: '#2f3132'
  tertiary-container: '#656769'
  on-tertiary-container: '#e6e6e8'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#eaddff'
  primary-fixed-dim: '#d2bbff'
  on-primary-fixed: '#25005a'
  on-primary-fixed-variant: '#5a00c6'
  secondary-fixed: '#aeecff'
  secondary-fixed-dim: '#00d9ff'
  on-secondary-fixed: '#001f26'
  on-secondary-fixed-variant: '#004e5d'
  tertiary-fixed: '#e2e2e4'
  tertiary-fixed-dim: '#c6c6c8'
  on-tertiary-fixed: '#1a1c1d'
  on-tertiary-fixed-variant: '#454749'
  background: '#131318'
  on-background: '#e4e1e9'
  surface-variant: '#35343a'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The design system is engineered for a high-performance Generative AI knowledge platform. The brand personality is precise, avant-garde, and authoritative, targeting technical leaders and AI researchers. 

The aesthetic draws from **Modern Minimalism** and **Glassmorphism**, characterized by a "dark-matter" workspace. The interface uses deep blacks to create infinite depth, punctuated by high-frequency accent colors that represent the "spark" of artificial intelligence. Visual weight is managed through luminosity rather than heavy fills, ensuring a lightweight, sophisticated user experience reminiscent of high-end developer tools.

## Colors
The palette is rooted in a "Deep Space" black (`#0A0A0F`) to maximize OLED contrast and reduce eye strain during long evaluation sessions. 

- **Primary (Electric Violet):** Used for primary actions and state indicators.
- **Secondary (Neon Cyan):** Used for data visualization, success states, and secondary highlights.
- **Surface Strategy:** Layers are defined by subtle increases in lightness. The background is pure black, while containers use a slightly elevated dark grey with low-opacity borders.
- **Gradients:** Use the violet-to-cyan gradient sparingly for high-impact areas like progress bars, active AI "thinking" states, and premium feature calls-to-action.

## Typography
The typographic system utilizes a dual-font strategy to balance character with utility.

- **Space Grotesk (Headings):** Provides a technical, geometric edge. Use bold weights for primary headings to establish a strong hierarchy.
- **Inter (Body/UI):** Chosen for its exceptional legibility in dark mode and technical contexts. Body text should maintain a "Light" or "Regular" weight (300-400) to keep the interface feeling airy.
- **Contrast:** Maintain a strict hierarchy where headings are `#F5F5F7` (High Contrast) and body/meta text is `#9CA3AF` (Medium Contrast).

## Layout & Spacing
This design system utilizes a **Fixed Grid** model for centralized content management and a **Fluid Flex** model for dashboard modules.

- **Desktop:** 12-column grid with 24px gutters. Content is centered in a 1200px max-width container.
- **Tablet:** 8-column grid with 20px gutters.
- **Mobile:** 4-column grid with 16px margins. 
- **Rhythm:** All spacing must be a multiple of 4px. Use generous vertical padding (`stack-lg`) between major sections to emphasize the minimalist, premium feel.

## Elevation & Depth
Depth is achieved through **Tonal Layering** and **Luminous Shadows** rather than traditional dropshadows.

- **Level 0 (Background):** `#0A0A0F`.
- **Level 1 (Cards/Sidebar):** `#12121A` with a 1px solid border of `#26262E`.
- **Level 2 (Popovers/Modals):** `#1A1A24` with a 1px solid border of `#3F3F46`.
- **Interactive Glow:** For hovered buttons or active cards, apply a soft, diffused outer glow using the primary color at 15% opacity (`box-shadow: 0 0 20px rgba(124, 58, 237, 0.15)`).
- **Backdrop Blur:** Modals and navigation overlays must use a 12px blur with a 60% opacity fill to maintain context of the underlying data.

## Shapes
The shape language is refined and consistent, utilizing a "Rounded" standard to soften the technical nature of the AI data.

- **Standard Elements:** Buttons, inputs, and small cards use `0.5rem` (8px) or `rounded-md`.
- **Main Containers:** Dashboard widgets and primary sections use `1rem` (16px) for a distinct, modern enclosure.
- **Interactive States:** Use a slight increase in border-color luminosity on hover rather than changing the shape or size.

## Components
- **Buttons:** 
  - *Primary:* Violet-to-Cyan gradient background, white text, no border, subtle violet glow on hover.
  - *Ghost:* Transparent background, 1px `#26262E` border, text turns white on hover.
- **Inputs:** 
  - Dark background (`#12121A`), 1px border. On focus, the border transitions to the primary violet and a 2px outer glow is applied.
- **Chips/Badges:** 
  - Small, capsules (fully rounded) with low-opacity fills of the accent colors (e.g., Violet at 10% opacity) and high-contrast text.
- **Cards:** 
  - Minimalist with a 1px border. Header and Body separated by a subtle 1px line. No heavy shadows; depth is indicated by the background color shift from the page floor.
- **Iconography:** 
  - Use 24px grid-aligned, 1.5pt stroke-width line icons. Icons should be monochrome (`#9CA3AF`) unless they represent an active state or a specific AI action.
- **Additional Elements:** 
  - *Code Blocks:* Use a custom monospaced font with `#12121A` background and subtle syntax highlighting using the cyan accent.
  - *Progress Indicators:* Thick, 8px rounded bars utilizing the brand gradient.