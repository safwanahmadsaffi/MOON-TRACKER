import streamlit as st
import pandas as pd

# Define the criteria, weights, and helper descriptions
criteria = [
    ("Revenue Growth Consistency", 14),
    ("Profit-Margin Expansion", 10),
    ("Leverage (Debt/Equity)", 5),
    ("Return on Equity (ROE)", 9),
    ("Management & Insider Ownership", 10),
    ("Total Addressable Market (TAM) Growth", 7),
    ("Long-Term Industry Tailwinds", 4),
    ("Margin of Safety (Valuation)", 10),
    ("Customer Concentration", 4),
    ("Global Expansion Potential", 4),
    ("Sustainable Competitive Advantage", 10),
    ("Valuation Ratios (P/E & PEG)", 8),
    ("Free Cash Flow Positivity", 4),
    ("Institutional Investor Interest", 4),
    ("Price Momentum", 7)
]

# UI: Title
st.title("📊 Mood Transker – PSX Multibagger Score Calculator")
st.markdown("Evaluate any PSX stock based on key investment criteria to determine its multibagger potential.")

# Input scores for each criterion
scores = {}
st.subheader("🔍 Input Scores (0–10)")
for name, weight in criteria:
    scores[name] = st.slider(f"{name} (Weight: {weight})", 0, 10, 5)

# Calculate weighted score
weighted_scores = {name: score * weight for (name, weight), score in zip(criteria, scores.values())}
total_weighted_score = sum(weighted_scores.values())
normalized_score = total_weighted_score / 100

# Determine Investment Zone
if normalized_score >= 8.5:
    zone = "✅ Multibagger"
elif normalized_score >= 7.1:
    zone = "👍 Strong Investment Call"
elif normalized_score >= 6.0:
    zone = "🔍 Watchlist (Further due diligence needed)"
else:
    zone = "❌ Do Not Invest"

# Show Breakdown Table
st.subheader("📋 Criteria Breakdown")
st.dataframe(pd.DataFrame({
    'Criterion': [name for name, _ in criteria],
    'Score (0-10)': list(scores.values()),
    'Weight': [weight for _, weight in criteria],
    'Weighted Score': list(weighted_scores.values())
}))
# Output
st.subheader("📈 Results")
st.metric("Total Weighted Score", f"{total_weighted_score:.0f} / 1000")
st.metric("Normalized Score", f"{normalized_score:.2f} / 10")
st.success(f"**Investment Zone:** {zone}")
