# War Room Simulation — Technical Specification

## Overview

The War Room is a causal, adversarial multi-agent simulation that takes a single macro catalyst and propagates it through 5 behaviorally distinct hedge fund archetypes to generate final positioning vectors.

Executed by: `tools/run_war_room.py`

## Six-Phase Execution Sequence

### Phase 1: Macro Catalyst Ingestion
```
Input:  data/macro_inputs/live_catalyst.json
Output: regime_state dict passed to all agents
```
The system reads the current macro environment. The catalyst is presented homogeneously to all agents — no agent receives information the others do not.

### Phase 2: Independent Reaction Functions
Each agent generates its initial thesis independently, applying only its own constraints:

| Agent | Key Constraint Applied | Typical Initial Reaction |
|---|---|---|
| Alpha Quant | VaR limit (5-day window) | Forced gross deleveraging |
| Macro Titan | Directional mandate | Amplify catalyst via rates short |
| Pod Shop | PM drawdown limit (3%) | Defensive factor neutralization |
| Fundamental Tiger | Thesis-based trigger (not price) | Buy into panic dislocation |
| Activist Alpha | Structural illiquidity | Pay tail hedge premium |

### Phase 3: Cross-Examination
Agents evaluate each other's Phase 2 theses. The Deafness Protocol governs this phase:

**Deafness Protocol Rule:**
> If Agent A's argument relies on a resolution timeline that exceeds Agent B's VaR evaluation window, Agent B's system rejects the argument entirely — not because it is logically invalid, but because it is computationally out of scope.

Example: Fundamental Tiger presents a 3-year FCF thesis to the Alpha Quant. The Quant evaluates all inputs against a 5-day window. The thesis horizon (1,095 days) exceeds the window (5 days) by a factor of 219x. Result: `DEAFNESS_PROTOCOL_ENGAGED`. Forced liquidation continues.

### Phase 4: Constraint-Based Overrides
Post-cross-examination, each agent finalizes its position strictly within its constraint boundaries. Arguments that survived cross-examination are incorporated; rejected arguments are discarded.

### Phase 5: Crowding Aggregation
The aggregator node maps all final positions:

**Crowding Rule:**
> If ≥3 of 5 agents are directionally aligned on the same asset/trade, a systemic EV drag penalty of -150bps is applied to that trade's expected value — reflecting exit liquidity risk when too many similar mandates attempt to unwind simultaneously.

### Phase 6: Final Output Generation
```
Output: outputs/latest_run_summary.json
Output: outputs/positioning_memos/*.json
```
The simulation state is serialized to JSON for UI consumption and archival.

## Scenario Reference: Bond Vigilante Duration Shock

**Catalyst:** 10yr UST +35bps (5.15%), VIX 26.5, Bear Steepener

| Agent | Final Position | Conviction |
|---|---|---|
| Alpha Quant | Short Basket (Broad Tech) | Mechanistic |
| Macro Titan | Short TLT / ZB Futures | Very High |
| Pod Shop | Short XLK, XLF (Factor Hedge) | Moderate |
| Fundamental Tiger | Long MSFT (Accumulate) | Extreme |
| Activist Alpha | Hold Core / VIX Calls | Forced |

**Crowded Trade:** Short Long-Duration Tech — 3/5 agents aligned → -150bps EV penalty applied.

**Highest Conviction:** Long MSFT via Fundamental Tiger — absorbing the artificial liquidity vacuum created by mechanistic Quant deleveraging.
