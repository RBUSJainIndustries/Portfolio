import streamlit as st

# Page configuration
st.set_page_config(page_title="R. B. Umrao Singh Jain Industries", layout="centered")

BURGUNDY = "#6b3a51"
WHITE = "#ffffff"

# Custom CSS styling
st.markdown(f"""
    <style>
        body {{ background-color: {WHITE}; }}
        h1, h2, h3, h4 {{ color: {BURGUNDY}; }}
        .contact-box {{
            background-color: {BURGUNDY};
            color: {WHITE};
            padding: 15px;
            border-radius: 10px;
        }}
        .footer {{
            text-align: center;
            color: #999;
            font-size: 0.9em;
            padding: 20px 0;
        }}
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"<h2 style='text-align: center;'>R. B. Umrao Singh Jain Industries</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #555;'>Precision Engineered. Performance Delivered. Since 1992</p>", unsafe_allow_html=True)

# About Us
st.markdown("### 🏢 About Us")
st.write("""
Established in **1992**, we are a trusted manufacturer of **Perforated Metal Sheets** including vacuum filter screens, centrifugal filter screens, supporting liners (Dovex Type), and Rice Polishing Jali.

Our products are made from high-grade materials such as Stainless Steel, Carbon Steel, M.S/G.I, Brass, Copper, and Aluminum. With modern infrastructure, an R&D-backed process, and an expert team, we serve industries like:

- Food & Beverage Processing
- Sugar, Cement & Power Plants
- Automobile, Pharmaceuticals, Fertilizer, and more
""")

# What We Offer
st.markdown("### 🛠️ Product Range")

with st.expander("🔘 Round Hole Sheets"):
    st.write("""
- **Materials**: SS (202/304), Galvanized, CR, Copper & Brass
- **Hole Size**: 0.5 – 25 mm
- **Width**: 12 – 60 inches
- **Thickness**: 10g – 36 gauge
""")

with st.expander("◻️ Square Hole Sheets"):
    st.write("""
- **Hole Size**: 0.45 x 5 mm
- **Width**: 12 – 50 inches
- **Thickness**: 22g – 24g
""")

with st.expander("⭘ Oblong Hole Sheets"):
    st.write("""
- **Hole Size**: 3 mm
- **Width**: 36 – 48 inches
- **Thickness**: 20g – 22g
""")

with st.expander("🔺 Triangle Hole & Other Custom Shapes"):
    st.write("Available on request for industrial and architectural needs.")

# Applications
st.markdown("### 🧩 Applications")
st.write("""
Our sheets are used across:
- Food Processing
- Sugar Mills
- Chemical & Cement Industries
- Petrochemical, Construction & Architecture
- Automobile, Pharmaceuticals, Paper, Textile, Power Projects
""")

# Packaging & Quality
st.markdown("### 📦 Packaging & Quality")
st.write("""
We use **double-layered packaging** to prevent transit damage and maintain sheet integrity. Our manufacturing process is ISO-grade with strict quality control at every stage.
""")

# Contact Info Box
st.markdown("### 📞 Contact Us")
st.markdown(f"""
<div class="contact-box">
    📍 Uttam Nagar, Delhi Road, Rewari - 123401, Haryana, India<br>
    📱 +91 9416063658 | +91 8930030130<br>
    ✉️ rbusindustry@gmail.com
</div>
""", unsafe_allow_html=True)

# Inquiry Form
st.markdown("### 📋 Product Inquiry Form")
st.components.v1.iframe("https://forms.gle/frUcJBESz841e5Vq9", height=700)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<div class="footer">
    © 1992–2025 R. B. Umrao Singh Jain Industries | Developed by Sandeep Jain<br>
    Engineered Sheet Metal Solutions | Precision • Strength • Customization
</div>
""", unsafe_allow_html=True)
