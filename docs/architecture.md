# System Architecture

## Overview

The Hedge Fund Pod system operates as a 4-layer pipeline. Each layer has a discrete responsibility and passes structured data downstream to the next.

```
[ data/ ]  →  [ tools/build_strategy_dna.py ]  →  [ agents/*.json ]
                                                           ↓
[ data/macro_inputs/ ]  →  [ tools/run_war_room.py ]  ←─┘
                                    ↓
              [ tools/export_positioning_memos.py ]
                                    ↓
              [ outputs/latest_run_summary.json ]
                                    ↓
                         [ index.html (UI) ]
```

## Layer 1: Input (`data/`)

Raw, unstructured source materials:

| Directory | Contents | Used By |
|---|---|---|
| `data/filings/` | JSON-extracted 13F holdings | `build_strategy_dna.py` — quantitative constraint mapping |
| `data/investor_letters/` | Qualitative philosophy excerpts | `parse_letters.py` — LLM extraction of behavioral limits |
| `data/interviews/` | PM / founder transcript excerpts | `parse_letters.py` — supplementary behavioral signals |
| `data/historical_regimes/` | Stress analog datasets | `run_war_room.py` — back-test validation of reactions |
| `data/macro_inputs/` | Live catalyst packet | `run_war_room.py` — simulation trigger |

## Layer 2: DNA Synthesis (`tools/build_strategy_dna.py`)

Combines quantitative data from 13F extracts with qualitative signals from investor letters. Outputs structured behavioral constraint schemas to `agents/*.json`.

Key outputs per agent:
- `holding_period` — derived from turnover ratios in 13F data
- `risk_constraints` — extracted from letter disclosures and ADV filings
- `macro_reaction_function` — synthesized from historical regime behavior and interview evidence

## Layer 3: Simulation Engine (`tools/run_war_room.py`)

The core adversarial sequence. Six phases:

1. **Macro Ingestion** — Load `live_catalyst.json`
2. **Agent Loading** — Load all 5 `agents/*.json` profiles
3. **Independent Reactions** — Each agent generates its initial thesis independently
4. **Cross-Examination** — Agents evaluate each other's proposals; horizon mismatches trigger the Deafness Protocol
5. **Crowding Check** — Aggregator identifies where ≥3 agents are directionally aligned; applies EV drag penalty
6. **Output Generation** — Calls `export_positioning_memos.py` to produce final artifacts

## Layer 4: Output (`outputs/`)

| File | Description |
|---|---|
| `latest_run_summary.json` | Aggregated scenario summary — consumed by the UI |
| `positioning_memos/*.json` | Per-agent detailed position justification |
| `strategy_dna_profiles/*.json` | Compiled agent profiles (mirror of `agents/`) |

## Layer 5: UI (`index.html`)

Static front-end terminal dashboard. Visualizes the simulation state. Currently uses hardcoded simulation data. Future integration: fetch `outputs/latest_run_summary.json` via JavaScript to render live simulation results dynamically.

## Implementation Status

| Component | Status | Notes |
|---|---|---|
| `data/` — Source Materials | ✅ Seeded | Placeholder exemplars for all 5 archetypes |
| `agents/` — DNA Profiles | ✅ Complete | All 13 schema fields populated for each agent |
| `tools/build_strategy_dna.py` | 🔲 Scaffolded | LLM API integration pending |
| `tools/run_war_room.py` | ✅ Scaffolded | Full 6-phase logic stubbed |
| `tools/export_positioning_memos.py` | ✅ Complete | Generates valid output artifacts |
| `outputs/` | ✅ Seeded | Example run artifacts present |
| `index.html` (UI) | ✅ Complete | Dark terminal dashboard deployed |
