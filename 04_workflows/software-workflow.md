# Software workflow

Status: Draft, 27 Nov 2026. Tags: B secondary, K general practice. Builds on `vishruth04/plinthscapes-os/office/skills/autocad-plan-to-sketchup-base` and `concept-to-render-workflow`.

## 1. Pipeline

```
AutoCAD (2D master)  ->  SketchUp (3D model)  ->  Enscape / D5 (renders, video)  ->  Photoshop (post)  ->  InDesign/Illustrator/Canva (sheets)  ->  PDF / PPT
        |                                                     |
        +-> DXF for laser-cut models                          +-> Blender (optional: light studies, animation)
```

## 2. Step notes

**AutoCAD (master drawings)**
- One master DWG at 1:1, model space, World UCS, everything at Z = 0. Clean copy for SketchUp import (walls, openings, levels only). Never edit the only copy. (from the plinthscapes skill, B/K)
- Layers by element (walls, glazing, furniture, exhibits, lighting, ceiling, text, dims) so RCP and lighting plans come from the same file.
- Plot styles (CTB) with line weights; sheets at 1:100, 1:50, 1:20, 1:10.

**SketchUp (3D)**
- Import the clean DWG, draw walls with Push/Pull, group/component everything, tags per zone.
- Model the light apertures (oculus, slots) accurately: renders will then show the real sun patches.
- Set geo-location to Kodaikanal (≈10.23° N, 77.46° E) for true shadows and sun studies.

**Rendering** (from [Chaos blog](https://blog.chaos.com/enscape-vs-d5-render-interior-design), [Novatr](https://www.novatr.com/blog/d5-render-vs-lumion-vs-enscape-which-visualization-tool-is-best-for-architects), [Coohom](https://www.coohom.com/article/lumion-vs-other-interior-rendering-software), B)

| Tool | Strength | Weakness | Use here |
|---|---|---|---|
| Enscape | Inside SketchUp, live updates, easiest workflow, OK on mid-range PCs | Images can look less polished; smaller library | Daily design checks, VR walk-through |
| D5 Render | Most cinematic; **emissive bloom**, decals, atmosphere; big library | Needs an RTX GPU (8 GB VRAM suggested); separate workspace | Final dark-room renders (glow, stars, light beams) |
| Lumion | Fast, atmospheric | GPU-heavy; needs tweaking for small rooms with complex artificial light | Exterior/site renders |
| Twinmotion | Easy to learn | Less precise interior light controls | Alternative |

Check student/education licences on each vendor's site (not confirmed here). The family PC already has SketchUp, Enscape and Lumion (plinthscapes skill notes); D5 has a free tier (verify).

**Rendering dark interiors (K):**
- Use emissive materials for star points, LED strips and screens; add bloom in post or in D5.
- Use volumetric fog to make light beams visible (Sun Gallery shafts).
- Set exposure for the dark room, not the bright one; render bright and dark zones separately.
- Show the sequence with the same camera height and lens across all zones.

**Blender (optional)**
- Good for: animated sun-path study through the oculus over a year, glowing star fields, stylised diagrams.
- `vishruth04/amara-bhoomi/skills/automate-blender-with-python` and `operate-blender-as-an-agent` cover safe scripting and file handling and can be reused.

**Photoshop:** add people silhouettes (helps scale in dark scenes), glow, sky replacement for exterior, colour grading for the light-to-dark series.

**Sheets:** InDesign (best for multi-sheet consistency), Illustrator, or Canva (already used for the topic review). Set the grid once as a template (see `presentation-sheets-and-ppt.md`).

**Video:** Enscape/D5 walkthrough, then edit in DaVinci Resolve (free) with captions and music.

## 3. File organisation

Local folder already exists: `D:\Blender\Ritu_Thesis\` (01_Brief ... 06_References). Keep big CAD, SKP and render files there (not in Git); keep text, small images and final PDFs here. Name files `YYYY-MM-DD_review-name_vNN`.
