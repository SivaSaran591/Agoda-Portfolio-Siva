import streamlit as st
import time

# --- Page config ---
st.set_page_config(page_title="Demand Gen That Slaps — At Scale 🚀", page_icon=":tada:", layout="wide")

# --- Custom CSS ---
st.markdown(
    """
    <style>
    body {
        background-color: #f7f9fc;
        color: #222831;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    section[data-testid="stSidebar"] {
        background-color: #e0f2f1;
        border-right: 1px solid #d1d8e2;
    }
    h1, h2, h3 {
        color: #0078FF; /* Primary color */
        text-align: center; /* Center align all h1, h2, h3 */
    }
    .hero-banner {
        background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
        color: white;
        padding: 3rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .section-title {
        color: #005bb5; /* Darker primary color */
        border-bottom: 2px solid #00c6ff;
        padding-bottom: 0.5rem;
        margin-bottom: 1rem;
        text-align: center; /* Center align section titles */
    }
    .subsection {
        background-color: #f0f8ff; /* Light blue background */
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border-left: 4px solid #0078FF;
    }
    .toolkit-item {
        padding: 0.5rem 0;
        border-bottom: 1px dashed #d1d8e2;
    }
    .toolkit-item:last-child {
        border-bottom: none;
    }
    .connect-info {
        font-size: 1.1rem;
        margin-bottom: 0.8rem;
    }
    .blueprint-phase {
        background-color: #e6f7ff; /* Very light blue */
        padding: 1.2rem;
        border-radius: 10px;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        border-left: 5px solid #00b8d4; /* Accent color */
    }
    .blueprint-title {
        color: #0086b3;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .team-member {
        background-color: #f9fbe7; /* Light yellow */
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        border-left: 4px solid #aed581; /* Accent green */
    }
    .team-title {
        color: #689f38;
        font-weight: bold;
        margin-bottom: 0.3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Sidebar ---
st.sidebar.image("Agoda_logo.jpg", width=200)
st.sidebar.title("🧭 Explore My World")
sections = ["🏠 Home", "💖 We Go Together!", "🚀 Campaign Chronicles", "📅 30/60/90 Blueprint", "🤝 Dream Team", "🛠️ My Arsenal", "📬 Connect with Siva!"]
selection = st.sidebar.radio("Hop to a Section", sections)

# --- Home Section ---
if selection == "🏠 Home":
    with st.spinner("Igniting the Demand Gen Engine..."):
        time.sleep(1)

    st.markdown('<div class="hero-banner">', unsafe_allow_html=True)
    st.markdown(
        """
    <h1 style='text-align: center; font-size: 3em;'>🚀 Demand Gen That Breaks the Mold</h1>
    <p style='text-align: center; font-size: 1.5em;'>Where creativity fuels funnels, and pipelines aren’t just built — they're launched at warp speed. 🌠</p>
    """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<h2 class="section-title">Welcome Aboard 🎉</h2>', unsafe_allow_html=True)

    st.markdown(
        """
    👋 Hey there! Buckle up for a thrilling ride through my demand generation universe. I'm Siva, your future pipeline pilot 🚀, and I'm here to show you how I:
    """
    )
    st.markdown("📈 **Fuel Growth:** Implement data-driven, multi-channel strategies (email, SEO, social, webinars, content).")
    st.markdown("🎯 **Orchestrate Campaigns:** Manage end-to-end execution with a focus on compelling content and design.")
    st.markdown("🤝 **Collaborate Powerfully:** Work effectively with Sales, Product, BD, Design, and RevOps.")
    st.markdown("🎤 **Craft Impact:** Create marketing collateral that converts leads and empowers sales.")
    st.markdown("📣 **Build Audiences:** Execute digital campaigns to grow awareness and databases.")
    st.markdown("🚀 **Scale Social:** Drive growth on social media with engaged communities.")
    st.markdown("📊 **Optimize Relentlessly:** Monitor and refine performance using robust analytics.")

    st.markdown("<br>Ready to witness the magic? Let's make some serious KPI fireworks! 💥", unsafe_allow_html=True)

# --- We go together! Section ---
elif selection == "💖 We Go Together!":
    with st.spinner("Unveiling Our Story..."):
        time.sleep(1)

    st.markdown('<h2 class="section-title">The Story 🎬</h2>', unsafe_allow_html=True)

    st.markdown("### Why Agoda? 🛫", unsafe_allow_html=True)
    st.markdown(
        """
    For me, Agoda isn't just a company; it's a **high-octane rocketship** 🚀 in the travel galaxy! I'm drawn by:
    - 🔥 **Dynamic Energy:** A constant surge of innovation and progress.
    - 💡 **Bold Innovation:** They dare to disrupt and redefine the travel experience.
    - 📊 **Data-Driven Culture:** Where insights fuel every decision (my kind of language!).
    """
    )
    st.markdown(
        "I'm eager to join a league of **marketing superheroes** 🦸‍♂️, pushing the limits and shaping the future of travel. Being part of a company **scaling at warp speed** in this vibrant industry? That's my ultimate adventure! 🗺️",
        unsafe_allow_html=True,
    )

    st.markdown("### Why This Demand Gen Role? 🔥", unsafe_allow_html=True)
    st.markdown(
        """
    This Demand Gen role isn't just a job; it's my **personal quest** 🏹! I'm ready to bring:
    - 🔑 **Proven Expertise:** 5+ years of demand gen experience, ready to ignite growth.
    - 🧠 **Growth Hacker Mentality:** Turning leads into **customer tidal waves** 🌊.
    - 🤝 **Collaborative Power:** Building **marketing dream teams** that achieve the impossible.
    """
    )
    st.markdown(
        "I'm all about **driving impactful growth** through innovative, data-backed strategies, and I'm thrilled at the prospect of bringing my passion to Agoda. Let's create some legendary marketing moments! ✨",
        unsafe_allow_html=True,
    )

# --- Campaign Chronicles Section ---
elif selection == "🚀 Campaign Chronicles":
    with st.spinner("Loading Epic Campaign Tales..."):
        time.sleep(1)

    st.markdown('<h2 class="section-title">Data-Backed Victories 🏆</h2>', unsafe_allow_html=True)

    with st.expander("🎯 Mission: CFO Takeover"):
        st.markdown("**Objective:** Win the hearts (and wallets) of CFOs")
        st.markdown("**Tactic:** Precision-crafted outbound sequences plus laser-focused nurture flows.")
        st.markdown("**Victory:** Doubled the benchmark pipeline. My 'Golden Campaign' indeed! 🏆")
        st.markdown("*Fun Moment:* Our emails had a charm that was twice as effective as the industry average. 😉")

    with st.expander("🥇 Mission: PLM Cloud Launch Spectacle"):
        st.markdown("**Objective:** Launch a brand-new PLM cloud product with maximum impact.")
        st.markdown("**Tactic:** A full-stack GTM approach: electrifying webinars, insightful blogs, and compelling testimonials.")
        st.markdown("**Victory:** Smashed goals by 250%, generating a $10M+ pipeline in a single month! 🎉")
        st.markdown("*Fun Moment:* The Sales team joked they needed an extra pair of hands. 😎")

    with st.expander("🚀 Mission: Inbound Avengers Assemble"):
        st.markdown("**Objective:** Respond to inbound leads with superhero speed and efficiency.")
        st.markdown("**Tactic:** Assembled a crack team for inbound lead qualification.")
        st.markdown("**Victory:** Cut response time by 80%, leading to an explosive increase in pipeline velocity! ⚡")
        st.markdown("*Fun Moment:* We even implemented a 'Bat Signal' for ultra-hot leads. 🦇🔥")

    with st.expander("🚗 Mission: Rebrand Automotive's Ride to the Future"):
        st.markdown("**Objective:** Modernize HCL's Automotive positioning to align with CASE (Connected, Autonomous, Shared, Electric) innovation.")
        st.markdown("**Tactic:** Revamped web presence, launched engaging podcasts, and secured key analyst recognitions.")
        st.markdown("**Victory:** Achieved an 80% boost in organic form fills within a quarter! 📈")
        st.markdown("*Fun Moment:* Leadership showcased it as a global town hall success story. 🏆🏎️")

# --- 30/60/90 Blueprint Section ---
elif selection == "📅 30/60/90 Blueprint":
    with st.spinner("Crafting the Strategic Roadmap..."):
        time.sleep(1)

    st.markdown('<h2 class="section-title">Roadmap for Success 💡</h2>', unsafe_allow_html=True)

    st.markdown('<p class="blueprint-title">First 30 Days: Recon & Rally 🚀</p>', unsafe_allow_html=True)
    st.markdown("🗺️ **Understand the Terrain:** Deep dive into Agoda’s products, ICPs, and competitors.")
    st.markdown("📊 **Analyze the Data:** Audit current funnel metrics and campaign performance.")
    st.markdown("🤝 **Build Bridges:** Establish strong relationships with Sales, Product, and Content teams.")

    st.markdown('<p class="blueprint-title">Next 30 Days: Pilot & Perfect 🛠️</p>', unsafe_allow_html=True)
    st.markdown("🎯 **Activate Quick Wins:** Launch targeted pilot campaigns for rapid results.")
    st.markdown("🏗️ **Formalize Frameworks:** Develop scalable campaign blueprints for consistent success.")
    st.markdown("📈 **Establish Command Center:** Set up robust KPI tracking and reporting mechanisms.")

    st.markdown('<p class="blueprint-title">Final 30 Days: Scale & Conquer 🔥</p>', unsafe_allow_html=True)
    st.markdown("📣 **Amplify Success:** Expand high-performing strategies across all relevant channels.")
    st.markdown("⚡ **Optimize Velocity:** Streamline lead handoffs to accelerate pipeline flow.")
    st.markdown("👑 **Chart the Future:** Forecast demand gen goals and strategies for the next three quarters.")

# --- Dream Team Section ---
elif selection == "🤝 Dream Team":
    with st.spinner("Assembling the League of Extraordinary Marketers..."):
        time.sleep(1)

    st.markdown('<h2 class="section-title">My Agoda Approach ⚡</h2>', unsafe_allow_html=True)

    st.markdown('<p class="team-title">Sales BFFs 💬</p>', unsafe_allow_html=True)
    st.markdown("Co-create ICPs and feedback loops.")

    st.markdown('<p class="team-title">BD Stormers 🧠</p>', unsafe_allow_html=True)
    st.markdown("Capture real-time field intel to dynamically realign campaigns.")

    st.markdown('<p class="team-title">Product Whisperers 🚀</p>', unsafe_allow_html=True)
    st.markdown("Translate complex tech jargon into irresistible value propositions.")

    st.markdown('<p class="team-title">Creative Wizards 🎨</p>', unsafe_allow_html=True)
    st.markdown("Craft visually stunning and thumb-stopping content.")

    st.markdown('<p class="team-title">Content Ninjas 📚</p>', unsafe_allow_html=True)
    st.markdown("Build nurture flows so tight, leads won't know what hit 'em (in a good way!).")

    st.markdown("<br>Motto: 'Move fast. Collaborate faster.' ⚡", unsafe_allow_html=True)

# --- My Arsenal Section ---
elif selection == "🛠️ My Arsenal":
    with st.spinner("Loading My Supercharged Tools..."):
        time.sleep(1)

    st.markdown('<h2 class="section-title">Tools of the Trade 🛠️</h2>', unsafe_allow_html=True)

    st.markdown('<div class="toolkit-item">📤 Outbound: 🔗 Outreach, 💼 LinkedIn (Master of outbound sequences)</div>', unsafe_allow_html=True)
    st.markdown('<div class="toolkit-item">📊 Intelligence: 🏢 Crunchbase, 🔥 Bombora (Unlocking insights for targeted campaigns)</div>', unsafe_allow_html=True)
    st.markdown('<div class="toolkit-item">🎯 Lead Gen: 👤 Zoominfo (Your key to B2B connections)</div>', unsafe_allow_html=True)
    st.markdown('<div class="toolkit-item">🎬 Webinars & Video: 🌐 ON24, 🤖 HeyGen (Engaging audiences with dynamic content)</div>', unsafe_allow_html=True)
    st.markdown('<div class="toolkit-item">📈 Reporting & Analytics: 📊 PowerBI (Turning data into actionable strategies)</div>', unsafe_allow_html=True)
    st.markdown('<div class="toolkit-item">🔍 SEO: 🔭 (From keyword research to optimization mastery)</div>', unsafe_allow_html=True)

    st.markdown("<br>Motto: Equip. Engage. Elevate. 🚀", unsafe_allow_html=True)

# --- Let's Connect! Section ---
elif selection == "📬 Connect with Siva!":
    with st.spinner('Opening the hotline...'):
        time.sleep(1)

    st.markdown('<h2 class="section-title">Your Next Growth Partner 📬</h2>', unsafe_allow_html=True)
    
    st.markdown(f"""
    Ready to ignite some serious pipeline growth? Let's chat!

    📞 Call Me: <a href="tel:+916281495464">+91-6281495464</a>

    📧 Email Me: <a href="mailto:sivasaran591@gmail.com">sivasaran591@gmail.com</a>

    <br>P.S. I am a huge Arsenal fan. Let's chat Demand Gen, Collaboration, & Growth hacks 😎
    """, unsafe_allow_html=True)

    st.balloons()