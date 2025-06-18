import streamlit as st

# Page configuration
st.set_page_config(page_title="R. B. Umrao Singh Jain Industries", layout="wide")

# Custom colors
BURGUNDY = "#6b3a51"
CREAM = "#e8e4da"
WHITE = "#ffffff"

# Global CSS styling
st.markdown(f"""
    <style>
        html, body, [class*="css"] {{
            background-color: {CREAM};
        }}
        .header-box {{
            background-color: {BURGUNDY};
            color: {WHITE};
            padding: 30px 20px;
            text-align: center;
            border-radius: 0;
        }}
        .header-box h2 {{
            margin-bottom: 5px;
            font-size: 2.2rem;
        }}
        .header-box p {{
            font-size: 1.1rem;
            letter-spacing: 1px;
        }}
        h3, h4 {{
            color: {BURGUNDY};
        }}
        .contact-box {{
            background-color: {BURGUNDY};
            color: {WHITE};
            padding: 15px;
            border-radius: 10px;
            margin-top: 10px;
        }}
        .footer {{
            text-align: center;
            color: #555;
            font-size: 0.9em;
            padding: 30px 0;
        }}
    </style>
""", unsafe_allow_html=True)

# Header section with background
st.markdown(f"""
<div class="header-box">
    <h2>R. B. Umrao Singh Jain Industries</h2>
    <p>Precision Engineered. Performance Delivered. Since 1992</p>
</div>
""", unsafe_allow_html=True)

# About Us
st.markdown("### 🏢 About Us")
st.write("""
Established in the year 1992, we “R. B. Umrao Singh Jain Industries,” based at Rewari, Haryana, India, are engaged in offering a wide range of Perforated Metal Sheets - S.S. vacuum filter screen, centrifugal filter screen for sugar industries, supporting liner (Dovex Type) for centrifugal machine and Rice Polishing Jali.

These products are known for their high tensile strength, durable finish and quality material. Fabricated using high quality basic material like Stainless or Carbon Steel, M.S/ G.I, Aluminum, Brass and Copper, these products find extensive applications in various Industries such as Food and Beverage Processing Units, Automobiles, Pharmaceuticals and Cement. Our Products are in different styles, while the perforations are offered in options of square, triangle, oblong, oval and round shapes also.

Leveraging on our modern infrastructure, excellent R&D facility and backed by proficient technical professionals, we cater to the need of various industries successfully. Quality products at cost effective prices is the prominent attribute of our organization.

Under the able guidance of our mentor Mr. Sandeep Jain, we have emerged as a leading player in this segment. His sharp business acumen and leadership qualities have helped us to establish a wide network of clients located across different parts of India.
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

# Contact Info
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
st.markdown("""
    <div style='height: 700px; overflow: auto; border: 1px solid #ccc; border-radius: 8px;'>
        <iframe src="https://forms.gle/frUcJBESz841e5Vq9" width="100%" height="100%" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"""
<div class="footer">
    © 1992–2025 R. B. Umrao Singh Jain Industries | Developed by Sandeep Jain<br>
    Engineered Sheet Metal Solutions | Precision • Strength • Customization
</div>
""", unsafe_allow_html=True)
