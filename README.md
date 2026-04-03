# Hedge Fund Pod: Multi-Agent Behavioral Simulation

> A behavioral institutional modeling framework that replaces factor-based signal generation with a causal simulation of 5 hedge fund archetypes reacting under live macro conditions.

## Project Objective

This project explicitly rejects the assumption that capital markets can be alpha-generated purely through static factor sorting (Value, Momentum, Quality). The core insight: **real alpha requires modeling which specific pool of institutional capital will be forced to liquidate**, and which possesses the mandate latitude to absorb that liquidity vacuum.

We fine-tune 5 distinct Hedge Fund archetypes — each bounded by verifiable risk constraints — and run them through an adversarial multi-agent simulation to generate final positioning signals.

## Architecture

```
Macro Catalyst  ──▶  Agent DNA  ──▶  Constraint Engine  ──▶  War Room  ──▶  Positioning Output
```

The system comprises 4 execution layers:

| Layer | Location | Purpose |
|---|---|---|
| **Input** | `data/` | Raw 13F filings, investor letters, macro inputs |
| **DNA Profiles** | `agents/` | Behavioral constraint schemas for each archetype |
| **Simulation** | `tools/` | Pipeline scripts: DNA synthesis, War Room executor, memo exporter |
| **Output** | `outputs/` | Generated positioning memos and run summaries |
| **UI** | `index.html` | Dark terminal dashboard visualizing the simulation state |

## Folder Layout

```
hedge-fund-pod-dashboard/
├─ index.html                          # Main dashboard UI (GitHub Pages entry point)
├─ README.md                           # This file
├─ .nojekyll                           # GitHub Pages bypass (no Jekyll processing)
│
├─ agents/                             # Behavioral DNA constraint schemas
│  ├─ quant_agent_profile.json
│  ├─ macro_agent_profile.json
│  ├─ pod_agent_profile.json
│  ├─ fundie_agent_profile.json
│  └─ activist_agent_profile.json
│
├─ tools/                              # Execution pipeline scripts
│  ├─ build_strategy_dna.py            # DNA synthesis: 13F + letters → JSON profile
│  ├─ run_war_room.py                  # Core simulation engine
│  ├─ export_positioning_memos.py      # Output generator
│  ├─ fetch_13f.py                     # SEC EDGAR ingestion (placeholder)
│  ├─ fetch_newsapi.py                 # Live macro catalyst ingestion (placeholder)
│  └─ parse_letters.py                 # Investor letter LLM parser (placeholder)
│
├─ data/                               # Raw source materials
│  ├─ filings/                         # SEC 13F JSON extracts
│  ├─ investor_letters/                # Qualitative philosophy sources
│  ├─ interviews/                      # PM/founder transcript excerpts
│  ├─ historical_regimes/              # Analog regime reference data
│  └─ macro_inputs/                    # Live macro catalyst packet
│
├─ docs/                               # Project documentation
│  ├─ architecture.md
│  ├─ strategy_dna_methodology.md
│  └─ war_room_simulation.md
│
└─ outputs/                            # Generated simulation artifacts
   ├─ latest_run_summary.json          # Aggregated simulation output (feeds UI)
   ├─ strategy_dna_profiles/           # Compiled DNA outputs (mirror of agents/)
   └─ positioning_memos/               # Per-agent actionable position summaries
```

## Running the Simulation

```bash
# Step 1: Fetch the current macro regime
python tools/fetch_newsapi.py

# Step 2: Execute the multi-agent War Room
python tools/run_war_room.py

# Step 3: Export positioning memos and summary
python tools/export_positioning_memos.py
```

## Implementation Status

| Component | Status |
|---|---|
| Dashboard UI (`index.html`) | ✅ Complete |
| Agent DNA Profiles (5×) | ✅ Complete |
| War Room Simulation Logic | ✅ Scaffolded |
| SEC 13F Ingestion | 🔲 Placeholder (EDGAR API hook pending) |
| News API / Macro Feed | 🔲 Placeholder (API key required) |
| LLM Letter Parser | 🔲 Placeholder (LangChain integration pending) |
| Live JSON → UI Bridge | 🔲 Planned (fetch from `outputs/latest_run_summary.json`) |

## GitHub Pages

The dashboard is served directly from **`index.html`** at the repository root.

[Link URL: (https://kannzz3.github.io/short-alpha-pod/)]
