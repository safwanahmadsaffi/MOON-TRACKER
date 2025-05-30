import streamlit as st
import pandas as pd

# Define the criteria and their weights
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

# UI Title
st.title("📊 Mood Transker – PSX Multibagger Score Calculator")
st.markdown("Evaluate any PSX stock based on key investment criteria to determine its multibagger potential.")

# Input section
st.subheader("🔍 Input Scores (0–10)")
scores = {}
for name, weight in criteria:
    scores[name] = st.slider(f"{name} (Weight: {weight})", 0, 10, 5)

# Calculate weighted score
weighted_scores = {name: score * weight for (name, weight), score in zip(criteria, scores.values())}
total_weighted_score = sum(weighted_scores.values())
normalized_score = total_weighted_score / 100

# Output Metrics
st.subheader("📈 Results")
st.metric("Total Weighted Score", f"{total_weighted_score:.0f} / 1000")
st.metric("Normalized Score", f"{normalized_score:.2f} / 10")

# Visual Investment Verdict
st.markdown("### 🎯 Final Investment Verdict")

if normalized_score >= 8.5:
    st.markdown("""
    <div style='padding: 20px; border-radius: 15px; background-color: #d4edda; border-left: 8px solid #28a745;'>
        <h3 style='color: #155724;'>💸 Multibagger Zone</h3>
        <p><strong>Score:</strong> {:.2f} / 10</p>
        <p>🚀 This stock shows exceptional potential with strong fundamentals. Long-term investment recommended.</p>
    </div>
    """.format(normalized_score), unsafe_allow_html=True)

elif normalized_score >= 7.1:
    st.markdown("""
    <div style='padding: 20px; border-radius: 15px; background-color: #d1ecf1; border-left: 8px solid #0c5460;'>
        <h3 style='color: #0c5460;'>👍 Strong Investment Call</h3>
        <p><strong>Score:</strong> {:.2f} / 10</p>
        <p>📈 Good signs across fundamentals. Worth researching deeper and tracking closely.</p>
    </div>
    """.format(normalized_score), unsafe_allow_html=True)

elif normalized_score >= 6.0:
    st.markdown("""
    <div style='padding: 20px; border-radius: 15px; background-color: #fff3cd; border-left: 8px solid #856404;'>
        <h3 style='color: #856404;'>🔍 Watchlist Zone</h3>
        <p><strong>Score:</strong> {:.2f} / 10</p>
        <p>🧐 Mixed signals. Add to watchlist, but do more due diligence before investing.</p>
    </div>
    """.format(normalized_score), unsafe_allow_html=True)

else:
    st.markdown("""
    <div style='padding: 20px; border-radius: 15px; background-color: #f8d7da; border-left: 8px solid #721c24;'>
        <h3 style='color: #721c24;'>❌ Do Not Invest</h3>
        <p><strong>Score:</strong> {:.2f} / 10</p>
        <p>📉 The stock fails to meet key investment standards. Better opportunities exist elsewhere.</p>
    </div>
    """.format(normalized_score), unsafe_allow_html=True)

# Breakdown table
st.subheader("📋 Criteria Breakdown")
df = pd.DataFrame({
    'Criterion': [name for name, _ in criteria],
    'Score (0-10)': list(scores.values()),
    'Weight': [weight for _, weight in criteria],
    'Weighted Score': list(weighted_scores.values())
})
st.dataframe(df)
