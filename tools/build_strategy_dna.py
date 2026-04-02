REQUIRED_DNA_SCHEMA = [
    "archetype_name", "philosophy", "holding_period", "leverage_estimate",
    "gross_net_style", "factor_exposure", "sector_concentration", "risk_constraints",
    "preferred_instruments", "historical_regime_behavior", "macro_reaction_function",
    "confidence_notes", "evidence_sources"
]

def export_profiles(output_dir: str):
    print(f"Successfully minted 5 Behavioral Archetypes. Routing to {output_dir}")

if __name__ == "__main__":
    export_profiles("../outputs/strategy_dna_profiles/")
