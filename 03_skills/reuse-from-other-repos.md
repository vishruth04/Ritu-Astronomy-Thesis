# What we can reuse from vishruth04's other repositories

Reviewed 27 Nov 2026 (read-only): `Plinthscapes`, `plinthscapes-os`, `plinthscapes-os-app`, `project-loom`, `amara-bhoomi`.

| Repo | What is there | Reuse for the thesis |
|---|---|---|
| **plinthscapes-os** `office/skills/` (25 Markdown skills) | `interior-detailing-and-specs` (BIS plywood/MDF/laminate/gypsum/tile/paint standards, joinery, ergonomics, BOQ), `concept-to-render-workflow` (sketch → massing → render stages; SketchUp + Enscape + Lumion on the family PC), `autocad-plan-to-sketchup-base` (clean DWG → SketchUp), `client-proposal-and-presentation-pack` (presentation structure), `green-energy-and-sustainability-rules` (rainwater, solar, ECBC-type rules), `structural-and-mep-review-basics`, `tn-building-approval-process`, `tn-site-options-advisor` | **High.** Material specs, render pipeline, CAD-to-3D workflow and TN rules apply directly. These skills are also available to Claude in this project, so ask for them by name. They are written for Chennai residences; adapt for a public museum and hill-station rules. |
| **plinthscapes-os** repo pattern | `AGENTS.md`, `INDEX.md`, `HANDOFF.md`, `TASKS.md`, dated approval records, Draft/Approved status labels | **High.** Copied here as `AGENTS.md` + `HANDOFF.md` so any AI or device can resume. |
| **amara-bhoomi** `skills/` | `operate-blender-as-an-agent`, `automate-blender-with-python`, `build-procedural-blender-game-assets`, `validate-blender-game-asset-exports`; research source logs; `tools/workboard` (HTML project board generator) | **Medium.** Blender scripting for light/sun-path animations and stylised renders; source-log habit (cite every fact); the workboard could become a visual thesis tracker. Game-specific parts not needed. |
| **project-loom** | Factory IT and a Python production web app; `chat-history/` and `SOURCES.md` pattern | **Low.** Only the habit of keeping the owner's requests in their own words and listing files that live only on a laptop. |
| **plinthscapes-os-app** | Flutter construction-ops app | **None** for the thesis. |
| **Plinthscapes** | Older version of plinthscapes-os (merged) | None beyond the above. |

## Claude-side tools that help (no install needed by Ritu)

- SketchUp connector (Trimble) can block out massing models from a description (untested here).
- Slides and document tools for review PPTs and the report.
- Blender on `D:\Blender` via the connected computer, for scripted light studies.
