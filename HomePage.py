import streamlit as st
import base64
import streamlit as st

def get_base64_of_local_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_of_local_image("about_bg.JPG")
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
st.markdown(f"""
    <style>
    .about-us {{
        background-image: url("data:image/jpg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        padding: 40px;
        border-radius: 10px;
        margin-bottom: 20px;
        position: relative;
        color: {BURGUNDY};
    }}
    .about-us::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(255, 255, 255, 0.75); 
        border-radius: 10px;
        z-index: 1;
    }}
    .about-us-content {{
        position: relative;
        z-index: 2;
        font-size: 1.05rem;
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="about-us">
<h2 class="about-us-content">About Us</h2>
    <div class="about-us-content">
        Established in the year 1992, we “R. B. Umrao Singh Jain Industries,” based at Rewari, Haryana, India, are engaged in offering a wide range of Perforated Metal Sheets - S.S. vacuum filter screen, centrifugal filter screen for sugar industries, supporting liner (Dovex Type) for centrifugal machine and Rice Polishing Jali.
        These products are known for their high tensile strength, durable finish and quality material. Fabricated using high quality basic material like Stainless or Carbon Steel, M.S/ G.I, Aluminum, Brass and Copper, these products find extensive applications in various Industries such as Food and Beverage Processing Units, Automobiles, Pharmaceuticals and Cement. Our Products are in different styles, while the perforations are offered in options of square, triangle, oblong, oval and round shapes also.
        Leveraging on our modern infrastructure, excellent R&D facility and backed by proficient technical professionals, we cater to the need of various industries successfully. Quality products at cost effective prices is the prominent attribute of our organization.<br><br>
        Under the able guidance of our mentor Mr. Sandeep Jain, we have emerged as a leading player in this segment. His sharp business acumen and leadership qualities have helped us to establish a wide network of clients located across different parts of India.
    </div>
</div>
""", unsafe_allow_html=True)
import streamlit as st


# Title
st.markdown(""" <h2 style="color: {BURGUNDY};" class="about-us-content">Our Product Range </h2>""", unsafe_allow_html=True )

# CSS for consistent card look
st.markdown("""
    <style>
    .product-card {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 12px;
        padding: 15px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .product-card:hover {
        transform: scale(1.03);
    }
    .product-title {
        margin-top: 0;
        margin-bottom: 8px;
        color: #6b3a51;
        font-size: 18px;
        font-weight: bold;
    }
    .product-desc {
        font-size: 0.95rem;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# Columns layout (responsive with 2 or more columns depending on screen)
cols = st.columns(2)

# Product 1
with cols[0]:
    st.image("Round PS.png", use_container_width=True)
    st.markdown("""
    <div class="product-card">
        <div class="product-title">🔘 Round Hole Perforated Sheet</div>
        <div class="product-desc">
        <b>Materials:</b> S.S. (202/304), Galvanized, CR, Copper & Brass<br>
        <b>Hole Size:</b> 0.5 – 25 mm<br>
        <b>Width:</b> 12 – 60 inches<br>
        <b>Thickness:</b> 10g – 36 gauge
        </div>
    </div>
    """, unsafe_allow_html=True)

# Product 2
with cols[1]:
    st.image("Square PS.png", use_container_width=True)
    st.markdown("""
    <div class="product-card">
        <div class="product-title">◻️ Square Hole Perforated Sheet</div>
        <div class="product-desc">
        <b>Materials:</b> S.S. (202/304), Galvanized, CR, Copper & Brass<br>
        <b>Hole Size:</b> 5, 8, 10, 12 & 25 mm<br>
        <b>Width:</b> 12 – 48 inches<br>
        <b>Thickness:</b> 16g – 26 gauge
        </div>
    </div>
    """, unsafe_allow_html=True)

# Next row of columns
cols = st.columns(2)

# Product 3
with cols[0]:
    st.image("Oblong PSS.jpg", use_container_width=True)
    st.markdown("""
    <div class="product-card">
        <div class="product-title">⭘ Oblong Hole Perforated Sheet</div>
        <div class="product-desc">
        <b>Materials:</b> S.S. (202/304), Galvanized, CR, Copper & Brass<br>
        <b>Hole Size:</b> 0.45 x 5 mm<br>
        <b>Width:</b> 12 – 50 inches<br>
        <b>Thickness:</b> 22 & 24 gauge
        </div>
    </div>
    """, unsafe_allow_html=True)

# Product 4
with cols[1]:
    st.image("Triangle PS.png" , use_container_width=True)
    st.markdown("""
    <div class="product-card">
        <div class="product-title">🔺 Triangle Hole Perforated Sheet</div>
        <div class="product-desc">
        <b>Materials:</b> S.S. (202/304), Galvanized, CR, Copper & Brass<br>
        <b>Hole Size:</b> 3 mm<br>
        <b>Width:</b> 36 & 48 inches<br>
        <b>Thickness:</b> 20 & 22 gauge
        </div>
    </div>
    """, unsafe_allow_html=True)



st.markdown("<hr>", unsafe_allow_html=True)

# Applications
st.markdown("### Applications")

# Create two columns
col1, col2 = st.columns([1, 1])  # Adjust width ratios as needed

with col1:
    st.write("""
We are engaged in offering a comprehensive range of Steel Perforated Sheets, and Woven Wire Mesh. Renowned for their reliable performance, durable finish, and high tensile strength, our products are widely used across multiple industries and sectors, including:

- Food & Food Processing Units  
- Paper & Board Mills  
- Sugar Mills  
- Automobile Industry  
- Pharmaceuticals  
- Power Projects  
- Fertilizer Plants  
- Cement Industries  
- Chemical Industries  
- Construction Sector  
- Petrochemical Industry  
- Textile Mills  
- Architectural Applications  
- Household Use  
    """)

with col2:
    st.image("Applications.png", use_container_width =True)

st.markdown("<hr>", unsafe_allow_html=True)
# Packaging & Quality
st.markdown("### 📦 Packaging & Quality")
st.write("""
At the heart of our operations lies a seamless, highly efficient manufacturing process designed to deliver metal perforated sheets that stand the test of time. With precision-engineered machinery and stringent quality controls at every stage, we ensure each sheet meets the highest standards of durability and performance.
What sets us apart is not just the strength of our products but also the care with which they are delivered. Our double-layered packaging system safeguards each sheet against damage during transit, ensuring it reaches our customers in flawless condition—ready to perform, right out of the packet.
""")
st.markdown("<hr>", unsafe_allow_html=True)

# Inquiry Form
st.markdown("### 📋 Product Inquiry Form")
st.markdown("""
    <div style='height: 700px; overflow: auto; border: 1px solid #ccc; border-radius: 8px;'>
        <iframe src="https://forms.gle/frUcJBESz841e5Vq9" width="100%" height="100%" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
    </div>
""", unsafe_allow_html=True)

# Contact Info
st.markdown(f"""
<div class="contact-box">
    📍 Uttam Nagar, Delhi Road, Rewari - 123401, Haryana, India<br>
    📱 +91 9416063658 | +91 8930030130<br>
    ✉️ rbusindustry@gmail.com
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
