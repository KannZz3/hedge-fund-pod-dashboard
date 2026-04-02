# Strategy DNA Methodology

## The Core Problem with Factor-Based Models

Traditional quantitative finance assigns alpha from factor loadings: *"This stock scores high on Value, Momentum, and Quality — buy it."*

This ignores a fundamental institutional reality: **capital allocation is not unconstrained**. A portfolio manager at a market-neutral pod shop cannot simply hold a Value stock through a 20% drawdown. Their risk management system will terminate the book at -3%. Their thesis is correct; their mandate is incompatible.

## The Behavioral Constraint Approach

This framework maps how specific, named types of institutional capital **actually behave** under distress — not how they theoretically should behave.

The DNA profiles encode three categories of constraint:

### Category 1: Structural Limits (Quantitative)
Derived from 13F filing analysis and ADV disclosures:
- **Gross Capacity**: Maximum leverage relative to AUM (e.g., 300% for Stat-Arb, 100% for Activist)
- **VaR Window**: Evaluation horizon (5 days for Quant → 365 days for Activist)
- **Correlation Limit**: Maximum tolerable factor correlation before forced rebalancing

### Category 2: Philosophical Limits (Qualitative)
Extracted from investor letters and interviews via LLM parsing:
- **Holding Period**: Revealed by letter language ("we are long-term owners") and turnover ratios
- **Liquidation Trigger**: "Thesis invalidation only" (Fundie) vs. "Standard deviation breach" (Quant)
- **Instrument Preference**: Derived from 13F classification data

### Category 3: Historical Reaction Functions
Back-tested against known stress events (Q4 2018 Rate Hike, March 2020 COVID, Q3 2022 Inflation):
- Validates that the derived constraints produce the historically observed behavior
- Rejects any model that would have predicted behavior contrary to the archival record

## The Deafness Protocol

The central mechanism of the War Room simulation.

When agents with fundamentally incompatible time horizons evaluate the same market event:
- The Fundamental Tiger argues: *"MSFT is cheap on a 5-year FCF basis — buy it"*
- The Alpha Quant evaluates this argument against its 5-day VaR window
- Result: **DEAFNESS_PROTOCOL_ENGAGED** — the argument is discarded, not because it is wrong, but because it operates outside the Quant's evaluation horizon

This explains real market mispricing: fundamentally sound assets get sold mechanically because the capital that owns them is constrained by risk limits incompatible with the asset's resolution timeline.

## Evidence Chain

Every behavioral parameter in `agents/*.json` traces back to at least one of:
1. A specific 13F filing in `data/filings/`
2. A quoted passage from `data/investor_letters/` or `data/interviews/`
3. A historically validated analog in `data/historical_regimes/`

This evidentiary chain is what distinguishes this system from a simulation with arbitrary behavioral rules.
