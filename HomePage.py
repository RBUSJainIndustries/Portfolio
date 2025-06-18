import streamlit as st

# Page setup
st.set_page_config(page_title="R. B. Umrao Singh Jain Industries", layout="centered")

# Flyer header
st.markdown("""
    <div style="text-align: center; font-family: sans-serif;">
        <h2 style="color: #5c3c4a;">R. B. Umrao Singh Jain Industries</h2>
        <p style="letter-spacing: 2px; color: #555;">PREMIUM METAL PERFORATED SHEETS</p>
        <img src="https://drive.google.com/uc?export=view&id=1JSMiGgrowOIhfY1Dbl-2FYG5H1L9koUs" alt="Flyer Banner" style="width: 100%; max-width: 600px; border-radius: 10px;">
    </div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("""
### 👋 Hi,

Looking for high-quality **perforated metal sheets** that combine durability, precision, and performance?

We’re **R. B. Umrao Singh Jain Industries**, trusted since **1992** by industries like **automobile**, **pharma**, **cement**, **construction**, and more for delivering engineered metal solutions that last.
""")

# What We Offer
st.markdown("""
### 🛠️ What We Offer:

✅ **Materials** – SS 202/304, Galvanized Steel, Mild Steel, Brass, Copper  
✅ **Hole Shapes** – Round • Square • Oblong • Triangle  
✅ **Custom Sizes** – Widths from 12” to 60” • Thickness 10–36 Gauge  
""")

# Why Choose Us
st.markdown("""
### 🌟 Why Choose Us?

✅ Over 30 years of **trust & expertise**  
✅ **Pan India delivery** with damage-proof packaging  
✅ **Quick response & customized orders**  
""")

# Call to Action
st.markdown("""
📎 **Check out our full product catalog** – attach PDF  
📞 **Call or WhatsApp** us at **+91 9416063658 / 9389030030**  
""")

# Google Form Embed
st.markdown("---")
st.markdown("### 📋 Fill Out Product Inquiry Form")
st.components.v1.iframe("https://forms.gle/frUcJBESz841e5Vq9")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 0.9em; color: #888;">
    Warm regards,<br>
    <strong>Sandeep Jain</strong><br>
    R. B. Umrao Singh Jain Industries<br><br>
    <em>Our team will contact you shortly!</em>
</div>
""", unsafe_allow_html=True)
