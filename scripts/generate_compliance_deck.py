import os
import sys
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_enhanced_deck(output_pptx_path, assets_dir):
    prs = Presentation()
    # 16:9 widescreen layout: 13.333 x 7.5 inches
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # Palette
    DARK_BG = RGBColor(0x07, 0x0D, 0x18)      # Obsidian Midnight
    CARD_BG = RGBColor(0x0E, 0x1A, 0x2E)      # Deep Navy Slate
    ACCENT_GOLD = RGBColor(0xD4, 0xAF, 0x37)  # Imperial Gold
    ACCENT_BLUE = RGBColor(0x3B, 0x82, 0xF6)  # Electric Blue
    TEXT_WHITE = RGBColor(0xFF, 0xFF, 0xFF)   # Pure White
    TEXT_MUTED = RGBColor(0x94, 0xA3, 0xB8)   # Slate Light
    BORDER_COLOR = RGBColor(0x1E, 0x2E, 0x48) # Subtle Border
    
    img_terminal = os.path.join(assets_dir, "hero_terminal.jpg")
    img_network = os.path.join(assets_dir, "global_network.jpg")
    img_app = os.path.join(assets_dir, "multi_asset_app.jpg")
    img_solar = os.path.join(assets_dir, "energy_solar.jpg")
    img_board = os.path.join(assets_dir, "board_wealth.jpg")

    def add_bg(slide):
        shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = DARK_BG
        shape.line.fill.background()
        return shape

    def add_header(slide, title, category="12 CAPITAL INC. • INSTITUTIONAL DOSSIER", slide_num=None):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(10), Inches(0.35))
        p = cat_box.text_frame.paragraphs[0]
        p.text = category.upper()
        p.font.name = "Calibri"
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = ACCENT_GOLD
        
        t_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(10), Inches(0.65))
        p2 = t_box.text_frame.paragraphs[0]
        p2.text = title
        p2.font.name = "Calibri"
        p2.font.size = Pt(22)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        
        if slide_num:
            n_box = slide.shapes.add_textbox(Inches(11.8), Inches(0.4), Inches(1.0), Inches(0.4))
            pn = n_box.text_frame.paragraphs[0]
            pn.alignment = PP_ALIGN.RIGHT
            pn.text = f"{slide_num:02d} / 12"
            pn.font.name = "Calibri"
            pn.font.size = Pt(11)
            pn.font.bold = True
            pn.font.color.rgb = TEXT_MUTED

    def add_split_card(slide, left, top, width, height, title, bullets, card_bg=CARD_BG, title_color=ACCENT_GOLD):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = card_bg
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1)
        
        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.28)
        tf.margin_right = Inches(0.28)
        tf.margin_top = Inches(0.25)
        tf.margin_bottom = Inches(0.25)
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Calibri"
        p.font.size = Pt(13.5)
        p.font.bold = True
        p.font.color.rgb = title_color
        p.space_after = Pt(8)
        
        for b in bullets:
            pb = tf.add_paragraph()
            pb.text = f"• {b}"
            pb.font.name = "Calibri"
            pb.font.size = Pt(10)
            pb.font.color.rgb = TEXT_WHITE
            pb.space_after = Pt(4)

    # ─── SLIDE 1: COVER WITH CINEMATIC PHOTO ───
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1)
    if os.path.exists(img_terminal):
        pic = s1.shapes.add_picture(img_terminal, Inches(6.2), Inches(1.0), Inches(6.5), Inches(5.5))
    
    t_box = s1.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(5.2), Inches(5.0))
    tf = t_box.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = "12 GROUP HOLDING • COMPLIANCE DOSSIER"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = ACCENT_GOLD
    p.space_after = Pt(14)
    
    p2 = tf.add_paragraph()
    p2.text = "12 CAPITAL INC."
    p2.font.bold = True
    p2.font.size = Pt(40)
    p2.font.color.rgb = TEXT_WHITE
    p2.space_after = Pt(10)
    
    p3 = tf.add_paragraph()
    p3.text = "Global Multi-Asset Liquidity & Private Wealth Infrastructure\nInstitutional Onboarding Presentation for Banking & Risk Committee Review"
    p3.font.size = Pt(14)
    p3.font.color.rgb = TEXT_MUTED
    p3.space_after = Pt(24)
    
    p4 = tf.add_paragraph()
    p4.text = "• Jurisdiction: Saint Lucia (IBC Act, Cap. 12.14)\n• Execution Model: 100% STP / Non-Dealing Desk\n• Operational Partners: Luramic (LP) & Kenmore Design (CRM)\n• Live Platform: https://12capital.vercel.app"
    p4.font.size = Pt(10.5)
    p4.font.color.rgb = TEXT_WHITE

    # ─── SLIDE 2: OPERATIONAL REALITY & EXECUTIVE OVERVIEW ───
    s2 = prs.slides.add_slide(blank_layout)
    add_bg(s2)
    add_header(s2, "Active Operating Reality & Institutional Mandate", "01. EXECUTIVE SUMMARY", 2)
    
    if os.path.exists(img_terminal):
        s2.shapes.add_picture(img_terminal, Inches(7.5), Inches(1.5), Inches(5.0), Inches(5.4))
        
    add_split_card(s2, Inches(0.8), Inches(1.5), Inches(6.4), Inches(2.6), "Active Brokerage Operation", [
        "Live Market Facilitation: Real active client accounts already trading live currency & CFD markets.",
        "Corporate Domicile: International Business Company (IBC) in Saint Lucia with Caribbean Legal Opinion.",
        "Financial Engine of 12 Group: Backed by holding operating assets in clean energy and technology.",
        "Live Digital Infrastructure: Vercel production deployment active at https://12capital.vercel.app."
    ])
    add_split_card(s2, Inches(0.8), Inches(4.3), Inches(6.4), Inches(2.6), "Account Purpose & Strict Segregation", [
        "Corporate Working Capital & Shareholder Equity Injections from verified UBOs.",
        "Operational OPEX: Kenmore Design CRM, Luramic bridge fees, Vercel/Supabase cloud hosting.",
        "Liquidity Collateral: Transferring operational buffer to Luramic institutional clearing.",
        "100% Segregated: Zero commingling with client margin depositories or group projects."
    ])

    # ─── SLIDE 3: 12 GROUP ECOSYSTEM (DETRONIC ENERGIA & FACTORONE) ───
    s3 = prs.slides.add_slide(blank_layout)
    add_bg(s3)
    add_header(s3, "The 12 Group Ecosystem: Real Operating Assets", "02. CORPORATE BACKING", 3)
    
    if os.path.exists(img_solar):
        s3.shapes.add_picture(img_solar, Inches(7.5), Inches(1.5), Inches(5.0), Inches(5.4))
        
    add_split_card(s3, Inches(0.8), Inches(1.5), Inches(6.4), Inches(2.6), "Detronic Energia (Photovoltaic Energy)", [
        "Proven Real Assets: Operating solar energy generation with real commercial revenues in Brazil.",
        "Long-Term Infrastructure: Asset-backed stability providing corporate depth to 12 Group.",
        "Strategic Governance: Autonomous operating company with independent P&L and balance sheet.",
        "Sustainable Value Creation: Business as Mission (BAM) model uniting profits with real impact."
    ])
    add_split_card(s3, Inches(0.8), Inches(4.3), Inches(6.4), Inches(2.6), "FactorOne / FactorHub (Technology Track)", [
        "FinTech Development: Software backbone developed by Fayson Santos.",
        "Dual-Track Regulatory Segregation: FactorOne leads the domestic Brazilian BaaS path (BACEN).",
        "Zero Regulatory Contamination: 12 Capital (St. Lucia) and FactorOne operate as separate legal entities.",
        "Compliance Proof: 12 Capital does NOT solicit Brazilian residents or violate CVM boundaries."
    ])

    # ─── SLIDE 4: MULTI-ASSET & 12 TERMINAL AI ───
    s4 = prs.slides.add_slide(blank_layout)
    add_bg(s4)
    add_header(s4, "Multi-Asset Offering & 12 Intelligence Terminal", "03. PRODUCTS & AI", 4)
    
    if os.path.exists(img_app):
        s4.shapes.add_picture(img_app, Inches(7.5), Inches(1.5), Inches(5.0), Inches(5.4))
        
    add_split_card(s4, Inches(0.8), Inches(1.5), Inches(6.4), Inches(2.6), "Global Currency & Multi-Asset Execution", [
        "Câmbio Global / FX: 55+ Major, Minor & Exotic pairs with raw ECN spreads from 0.0 pips.",
        "Precious Metals & Energy: Gold (XAU/USD), Silver, Crude Oil, Natural Gas via STP.",
        "Global Indices: US30, S&P 500, Nasdaq 100, DAX 40 direct liquidity routing.",
        "De-Stigmatizing Forex: Repositioned as institutional multi-asset wealth connectivity."
    ])
    add_split_card(s4, Inches(0.8), Inches(4.3), Inches(6.4), Inches(2.6), "12 Intelligence Terminal (AI Analytics)", [
        "Automated DRE Upload: Clients upload company balance sheets for instant solvency scoring.",
        "Institutional Health Metrics: Real-time EBITDA margin, debt coverage & Altman Z-score.",
        "Macroeconomic Radar: Central bank yield curves, Treasury rates & DXY dollar index.",
        "High Retention Engine: Combines deep financial analytics with trading execution."
    ])

    # ─── SLIDE 5: STP EXECUTION & GLOBAL NETWORK ───
    s5 = prs.slides.add_slide(blank_layout)
    add_bg(s5)
    add_header(s5, "100% STP Execution & Global Network Architecture", "04. EXECUTION", 5)
    
    if os.path.exists(img_network):
        s5.shapes.add_picture(img_network, Inches(7.5), Inches(1.5), Inches(5.0), Inches(5.4))
        
    add_split_card(s5, Inches(0.8), Inches(1.5), Inches(6.4), Inches(2.6), "Straight-Through Processing (Luramic)", [
        "100% Non-Dealing Desk (NDD): Zero market making, zero proprietary trading desks.",
        "Back-to-Back Routing: Every client order is instantly mirrored into Luramic liquidity pool.",
        "Elimination of Market Risk: Currency swings affect liquidity provider, not broker balance sheet.",
        "Aligned Incentives: Revenues derived exclusively from transparent volume fees and spreads."
    ])
    add_split_card(s5, Inches(0.8), Inches(4.3), Inches(6.4), Inches(2.6), "Ultra-Low Latency Highways", [
        "Data Centers: High-speed cross-connects in London Equinix LD4 and New York NY4.",
        "Sub-Millisecond Execution: Orders filled at average latency under 1ms with minimal slippage.",
        "Daily Reconciliation: Automated end-of-day clearing statements from Luramic.",
        "Negative Balance Protection: Algorithmic stop-out limits preventing client debt."
    ])

    # ─── SLIDE 6: WEALTH STRUCTURING & GOVERNANCE ───
    s6 = prs.slides.add_slide(blank_layout)
    add_bg(s6)
    add_header(s6, "Offshore Wealth Structuring & Board Governance", "05. GOVERNANCE", 6)
    
    if os.path.exists(img_board):
        s6.shapes.add_picture(img_board, Inches(7.5), Inches(1.5), Inches(5.0), Inches(5.4))
        
    add_split_card(s6, Inches(0.8), Inches(1.5), Inches(6.4), Inches(2.6), "Executive Leadership Profiles", [
        "Cláudio (Chief Executive Officer): Leads corporate strategy, banking expansion & executive direction.",
        "André (Founding Partner & Board Director): Fiduciary architecture, group capital allocation & governance.",
        "Fayson Santos (Head of Technology & Operations): Systems deployment, Kenmore CRM & Luramic bridge.",
        "Certified MLRO: Dedicated compliance officer overseeing AML surveillance and FIU reporting."
    ])
    add_split_card(s6, Inches(0.8), Inches(4.3), Inches(6.4), Inches(2.6), "International Wealth Structuring", [
        "High-Net-Worth Advisory: Tailored corporate structures under Saint Lucia IBC common law.",
        "Capital Dollarization: Multi-currency treasury allocation (USD, EUR, GBP) for family offices.",
        "Strict KYC/AML Framing: Described strictly as asset protection & diversification, never as money movement.",
        "Third-Party Fund Distribution: Distributing verified UCITS and international investment funds."
    ])

    # ─── SLIDE 7: PARTNERS & TECH STACK ───
    s7 = prs.slides.add_slide(blank_layout)
    add_bg(s7)
    add_header(s7, "Proven Operational & Software Partners", "06. PARTNERS", 7)
    
    add_split_card(s7, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4), "Luramic (Prime Liquidity Provider)", [
        "Role: Prime counterparty clearing broker and institutional liquidity aggregator.",
        "Depth of Liquidity: Aggregating Tier-1 bank and non-bank pricing engines.",
        "Instruments: FX Majors/Minors, Gold, Silver, Oil, Global Equity Indices, Crypto CFDs.",
        "Audit & Reporting: Automated daily settlement journals, mark-to-market balances, and equity reports.",
        "Safety: Regulated institutional counterparty with multi-million dollar credit facilities."
    ])
    add_split_card(s7, Inches(6.8), Inches(1.5), Inches(5.6), Inches(5.4), "Kenmore Design (Enterprise CRM & PSP)", [
        "Role: Core Broker CRM, Trader's Room (Client Cabinet), KYC Pipeline & PSP Hub.",
        "Industry Standard: Renowned worldwide for turnkey institutional broker software.",
        "Client Cabinet: Multi-factor authenticated self-service portal for deposits and verification.",
        "PSP Gateway Hub: Connecting card acquirers, SEPA/SWIFT wire channels, and digital rails.",
        "Compliance Engine: Real-time user logs, IP tracking, and suspicious activity red flags."
    ])

    # ─── SLIDE 8: AML/CFT & KYC COMPLIANCE ───
    s8 = prs.slides.add_slide(blank_layout)
    add_bg(s8)
    add_header(s8, "Rigorous AML / CFT & KYC Compliance Program", "07. COMPLIANCE", 8)
    
    add_split_card(s8, Inches(0.8), Inches(1.5), Inches(3.6), Inches(5.4), "3-Tier Verification (KYC)", [
        "Tier 1 (Basic): Government-issued Passport/ID + 3D facial biometrics liveness test.",
        "Tier 2 (Full): Proof of residential address (utility bill/bank statement < 90 days).",
        "Tier 3 (Enhanced): Source of Wealth & Source of Funds documentation for accounts > $50k.",
        "Optical Character Recognition (OCR) ensures automated document tampering checks."
    ])
    add_split_card(s8, Inches(4.8), Inches(1.5), Inches(3.6), Inches(5.4), "Sanctions & PEP Screening", [
        "Dynamic Automated Screening: Every account screened against OFAC, UN, EU, UK sanctions.",
        "PEP Registries: Global Politically Exposed Persons and adverse media checks.",
        "Immediate Escalation: Instant account freeze upon match, escalated directly to MLRO.",
        "Re-screening: Continuous daily watchlist re-verification across entire active database."
    ])
    add_split_card(s8, Inches(8.8), Inches(1.5), Inches(3.6), Inches(5.4), "Anti-Third-Party Controls", [
        "Strict 1st-Party Rule: Sender name must match verified account name exactly.",
        "Zero Third-Party Payments: Intermediary and nominee deposits are systematically blocked.",
        "Return-to-Source: Withdrawals routed strictly back to originating verified deposit channel.",
        "Prohibited: US Persons, FATF blacklist nations (North Korea, Iran), St. Lucia residents."
    ])

    # ─── SLIDE 9: RISK CONTROLS & CAPITAL SAFETY ───
    s9 = prs.slides.add_slide(blank_layout)
    add_bg(s9)
    add_header(s9, "Capital Protection & Exposure Management", "08. RISK CONTROLS", 9)
    
    add_split_card(s9, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4), "Algorithmic Capital Preservation", [
        "Margin Call Alert (100%): Automated platform warning when account equity reaches 100% margin.",
        "Automated Stop-Out (50%): Instant liquidation of losing positions to prevent clearing deficit.",
        "Negative Balance Protection (NBP): Algorithmic guarantee ensuring clients never owe money.",
        "Risk Reserve Buffer: Internal corporate reserve funded to absorb rare black-swan market gaps.",
        "Zero Inventory Risk: STP pass-through eliminates overnight market exposure for 12 Capital."
    ])
    add_split_card(s9, Inches(6.8), Inches(1.5), Inches(5.6), Inches(5.4), "Treasury Segregation & Disaster Recovery", [
        "Full Segregation: Client margin deposits isolated completely from corporate operational funds.",
        "Dual-Signatory Controls: High-value corporate disbursements require dual executive sign-off.",
        "Cybersecurity: TLS 1.3 encryption, AES-256 at rest, mandatory 2FA, and SOC 2 cloud host.",
        "Business Continuity (BCP): Continuous database snapshot replication with RTO under 30 minutes.",
        "Independent Annual Audit: Financial records prepared for annual Caribbean audit."
    ])

    # ─── SLIDE 10: FINANCIAL MODEL (3 YEARS) ───
    s10 = prs.slides.add_slide(blank_layout)
    add_bg(s10)
    add_header(s10, "Three-Year Financial Projections & Solvency Model", "09. FINANCIAL MODEL", 10)
    
    add_split_card(s10, Inches(0.8), Inches(1.5), Inches(3.6), Inches(5.4), "Year 1 (Baseline)", [
        "Monthly Volume: $5,000,000",
        "Annual Volume: $60,000,000",
        "Active Accounts: 250",
        "Brokerage Revenue: $84,000",
        "Wealth & Advisory Fees: $101,000",
        "Total Gross Revenue: $185,000",
        "Total OPEX: ($131,100)",
        "Operating Profit: $17,900",
        "Operational Break-Even: Month 5",
        "Retained Buffer: $15,400"
    ])
    add_split_card(s10, Inches(4.8), Inches(1.5), Inches(3.6), Inches(5.4), "Year 2 (+100% Growth)", [
        "Monthly Volume: $10,000,000",
        "Annual Volume: $120,000,000",
        "Active Accounts: 650",
        "Brokerage Revenue: $168,000",
        "Wealth & Advisory Fees: $233,000",
        "Total Gross Revenue: $401,000",
        "Total OPEX: ($224,900)",
        "Operating Profit: $109,100",
        "Operating Margin: 27.2%",
        "Cumulative Buffer: $120,000"
    ])
    add_split_card(s10, Inches(8.8), Inches(1.5), Inches(3.6), Inches(5.4), "Year 3 (+100% Scale)", [
        "Monthly Volume: $20,000,000",
        "Annual Volume: $240,000,000",
        "Active Accounts: 1,500",
        "Brokerage Revenue: $336,000",
        "Wealth & Advisory Fees: $515,000",
        "Total Gross Revenue: $851,000",
        "Total OPEX: ($377,000)",
        "Operating Profit: $344,000",
        "Operating Margin: 40.4%",
        "Cumulative Buffer: $455,500"
    ])

    # ─── SLIDE 11: ROADMAP TO INTERNATIONAL DIGITAL BANK ───
    s11 = prs.slides.add_slide(blank_layout)
    add_bg(s11)
    add_header(s11, "Strategic Roadmap: Evolution to International Digital Bank", "10. FUTURE ROADMAP", 11)
    
    add_split_card(s11, Inches(0.8), Inches(1.5), Inches(11.6), Inches(5.4), "5-Stage Banking Transformation Blueprint", [
        "Phase 1 (Months 1–6): Operational Foundation & Bank Account Setup — $5M/mo volume; Luramic/Kenmore live; Corporate operational account active.",
        "Phase 2 (Months 6–18): Brokerage Scale & Capital Accumulation — $10M/mo volume; 12 Intelligence Terminal live; $350k+ retained in capitalization escrow.",
        "Phase 3 (Months 18–24): Regulatory Advisory & FSRA Filing — Retain Caribbean banking counsel; submit formal Class B/A application to Saint Lucia FSRA.",
        "Phase 4 (Months 24–30): Statutory Capitalization & Fit-and-Proper Vetting — Deposit $1.0M - $2.5M paid-up capital backed by 12 Group equity and earnings.",
        "Phase 5 (Months 30–36): Core Banking & SWIFT Direct Connectivity — Deploy Mambu/Skale cloud core; obtain SWIFT BIC; launch 12 International Digital Bank.",
        "LONG-TERM SYNERGY: Directly financing and clearing cross-border settlements for group entities (Detronic Energia, 12 Systems) with full regulatory ring-fencing."
    ])

    # ─── SLIDE 12: CONCLUSION & ATTESTATION ───
    s12 = prs.slides.add_slide(blank_layout)
    add_bg(s12)
    add_header(s12, "Corporate Attestation & Compliance Channel", "11. CONCLUSION", 12)
    
    add_split_card(s12, Inches(0.8), Inches(1.5), Inches(11.6), Inches(5.4), "Executive Attestation & Verification Data", [
        "Official Domicile: 12 Capital Inc., International Business Company (IBC), Laws of Saint Lucia (Cap. 12.14).",
        "Parent Holding: 12 Group Holding (Cláudio, CEO • André, Governance Director).",
        "Executive Leadership: Fayson Santos, Head of Technology & Operations.",
        "Operational Verification: Public web portal live at https://12capital.vercel.app (GitHub: 12capitalbank-cyber/12capital).",
        "Attestation: 12 Capital confirms that all capital derives from lawful commercial origins, operates on 100% STP without market risk, and enforces strict FATF AML/CFT compliance.",
        "Banking Compliance Liaison: compliance@12capital.com | Saint Lucia Registered Agent & Office"
    ])

    prs.save(output_pptx_path)
    print(f"Successfully generated PowerPoint with high-res images at {output_pptx_path}")

def generate_interactive_gamma_style_html(output_html_path, assets_dir):
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>12 Capital Inc. — Dynamic Executive Presentation (Gamma Style)</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #070D18;
  --panel: #0E1A2E;
  --card: #13223A;
  --gold: #D4AF37;
  --gold-glow: rgba(212, 175, 55, 0.25);
  --blue: #3B82F6;
  --emerald: #10B981;
  --text: #F8FAFC;
  --muted: #94A3B8;
  --border: #1E2E48;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Plus Jakarta Sans', sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.6;
  overflow-x: hidden;
  height: 100vh;
  display: flex;
  flex-direction: column;
}

/* TOP STATUS BAR */
.top-bar {
  height: 54px;
  background: rgba(11, 21, 40, 0.95);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  z-index: 100;
  backdrop-filter: blur(10px);
}
.brand-badge {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: 'JetBrains Mono', monospace;
  font-weight: 800;
  font-size: 15px;
  letter-spacing: -0.02em;
}
.gold-tag {
  color: var(--gold);
}
.status-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(16, 185, 129, 0.1);
  border: 1px solid rgba(16, 185, 129, 0.2);
  color: var(--emerald);
  font-size: 11px;
  font-weight: 700;
  font-family: 'JetBrains Mono', monospace;
}
.live-pulse {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--emerald);
  box-shadow: 0 0 10px var(--emerald);
  animation: pulse 1.8s infinite;
}
@keyframes pulse {
  0% { transform: scale(0.9); opacity: 0.7; }
  50% { transform: scale(1.3); opacity: 1; }
  100% { transform: scale(0.9); opacity: 0.7; }
}

/* SLIDE PROGRESS BAR */
.progress-container {
  height: 3px;
  background: rgba(255,255,255,0.05);
  width: 100%;
}
.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, var(--gold) 0%, var(--blue) 100%);
  width: 8.33%;
  transition: width 0.4s ease;
}

/* MAIN SLIDES VIEWPORT */
.viewport {
  flex: 1;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 24px;
}
.slide {
  position: absolute;
  inset: 24px;
  display: flex;
  opacity: 0;
  transform: translateX(40px) scale(0.98);
  transition: all 0.45s cubic-bezier(0.16, 1, 0.3, 1);
  pointer-events: none;
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 25px 60px rgba(0,0,0,0.6);
}
.slide.active {
  opacity: 1;
  transform: translateX(0) scale(1);
  pointer-events: auto;
}

/* SPLIT LAYOUT */
.split-left {
  flex: 1.1;
  padding: 44px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow-y: auto;
}
.split-right {
  flex: 1.2;
  position: relative;
  background: #000;
  overflow: hidden;
  border-left: 1px solid var(--border);
}
.split-right img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 6s ease;
}
.slide.active .split-right img {
  transform: scale(1.05);
}
.img-overlay-card {
  position: absolute;
  bottom: 24px;
  left: 24px;
  right: 24px;
  padding: 16px 20px;
  background: rgba(7, 13, 24, 0.85);
  backdrop-filter: blur(14px);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* TYPOGRAPHY & CARDS */
.slide-cat {
  font-size: 11px;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: var(--gold);
  text-transform: uppercase;
  font-family: 'JetBrains Mono', monospace;
  margin-bottom: 8px;
}
.slide-title {
  font-size: 30px;
  font-weight: 800;
  color: #FFF;
  line-height: 1.2;
  margin-bottom: 20px;
  letter-spacing: -0.02em;
}
.card-stack {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.info-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 18px 20px;
  border-left: 4px solid var(--gold);
}
.info-card h4 {
  font-size: 14px;
  color: #FFF;
  font-weight: 700;
  margin-bottom: 6px;
}
.info-card p {
  font-size: 12.5px;
  color: var(--muted);
  line-height: 1.5;
}
.metrics-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-top: 14px;
}
.m-card {
  background: rgba(7, 13, 24, 0.7);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 12px;
  font-family: 'JetBrains Mono', monospace;
}
.m-label { font-size: 10px; color: var(--muted); text-transform: uppercase; }
.m-val { font-size: 16px; font-weight: 700; color: #FFF; margin-top: 4px; }
.m-sub { font-size: 9.5px; color: var(--emerald); margin-top: 2px; }

/* CONTROLS FOOTER */
.bottom-controls {
  height: 60px;
  background: rgba(11, 21, 40, 0.95);
  border-top: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 30px;
  z-index: 100;
}
.btn-group { display: flex; gap: 10px; align-items: center; }
.nav-btn {
  background: rgba(255,255,255,0.06);
  border: 1px solid var(--border);
  color: #FFF;
  padding: 8px 18px;
  border-radius: 8px;
  font-size: 12.5px;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s ease;
}
.nav-btn:hover { background: rgba(255,255,255,0.12); border-color: var(--gold); }
.nav-btn.primary {
  background: linear-gradient(135deg, var(--gold) 0%, #B8860B 100%);
  color: #070D18;
  border: none;
}
.slide-indicator {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: var(--muted);
  font-weight: 600;
}
.slide-indicator strong { color: #FFF; }
.kbd-hint {
  font-size: 11px;
  color: var(--muted);
  font-family: 'JetBrains Mono', monospace;
}
.kbd {
  background: rgba(255,255,255,0.1);
  padding: 2px 6px;
  border-radius: 4px;
  border: 1px solid rgba(255,255,255,0.15);
  color: #FFF;
}
</style>
</head>
<body>

<!-- TOP STATUS BAR -->
<header class="top-bar">
  <div class="brand-badge">
    <span>12<span class="gold-tag">CAPITAL</span></span>
    <span style="color:var(--border);">|</span>
    <span style="font-size:11px; color:var(--muted);">IBC SAINT LUCIA</span>
  </div>
  <div class="status-pill">
    <span class="live-pulse"></span>
    <span>LIVE OPERATIONAL BROKERAGE</span>
  </div>
  <div class="kbd-hint">
    Use <span class="kbd">←</span> <span class="kbd">→</span> or <span class="kbd">Space</span> to navigate
  </div>
</header>

<!-- PROGRESS BAR -->
<div class="progress-container">
  <div class="progress-bar" id="progressBar"></div>
</div>

<!-- VIEWPORT FOR SLIDES -->
<main class="viewport">

  <!-- SLIDE 1: COVER -->
  <div class="slide active">
    <div class="split-left">
      <div>
        <div class="slide-cat">12 GROUP HOLDING • COMPLIANCE DOSSIER</div>
        <h1 class="slide-title" style="font-size:42px; margin-bottom:14px;">12 CAPITAL INC.</h1>
        <p style="font-size:15px; color:var(--muted); margin-bottom:28px;">
          Global Multi-Asset Liquidity, Straight-Through Processing (STP) & Private Wealth Infrastructure.
          Institutional Onboarding Presentation for Banking & Risk Committee Review.
        </p>
        <div class="card-stack">
          <div class="info-card">
            <h4>Corporate Standing</h4>
            <p>Incorporated under the International Business Companies Act, Cap. 12.14 of Saint Lucia with Caribbean Legal Opinion.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--blue);">
            <h4>Active Operations</h4>
            <p>Real ongoing trading volume and active clients. Publicly verifiable live platform at <strong style="color:#FFF;">https://12capital.vercel.app</strong>.</p>
          </div>
        </div>
      </div>
      <div style="font-size:11.5px; color:var(--muted); font-family:'JetBrains Mono',monospace;">
        Holding: 12 Group • Partners: Luramic (LP) & Kenmore Design (CRM)
      </div>
    </div>
    <div class="split-right">
      <img src="assets/hero_terminal.jpg" alt="Institutional Trading Floor">
      <div class="img-overlay-card">
        <div>
          <div style="font-size:12px; font-weight:700; color:#FFF;">Institutional Trading Hub</div>
          <div style="font-size:11px; color:var(--muted);">Multi-Bank Liquidity Aggregation • Zero Dealing Desk</div>
        </div>
        <div class="status-pill" style="background:rgba(212,175,55,0.15); border-color:var(--gold); color:var(--gold);">
          STP / DMA
        </div>
      </div>
    </div>
  </div>

  <!-- SLIDE 2: OPERATIONAL REALITY -->
  <div class="slide">
    <div class="split-left">
      <div>
        <div class="slide-cat">01. EXECUTIVE SUMMARY</div>
        <h2 class="slide-title">Active Operating Reality & Banking Purpose</h2>
        <div class="card-stack">
          <div class="info-card">
            <h4>Live Operating Track Record</h4>
            <p>12 Capital is not an idea on paper; the company is an active broker already facilitating real FX/CFD volume for live traders under formal Caribbean legal backing.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--emerald);">
            <h4>Exclusive Purpose of Corporate Account</h4>
            <p>Receiving verified shareholder equity injections, settling software licensing (Kenmore) and LP bridge fees (Luramic), and transferring margin collateral buffers.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--blue);">
            <h4>Strict Fund Segregation</h4>
            <p>Zero commingling between client margin deposits and corporate operating cash. Client deposits are held in dedicated segregated pathways.</p>
          </div>
        </div>
      </div>
      <div class="metrics-grid">
        <div class="m-card">
          <div class="m-label">Execution</div>
          <div class="m-val">100% STP</div>
          <div class="m-sub">No Market Risk</div>
        </div>
        <div class="m-card">
          <div class="m-label">Clearing</div>
          <div class="m-val">Luramic</div>
          <div class="m-sub">Tier-1 Aggregator</div>
        </div>
        <div class="m-card">
          <div class="m-label">CRM Engine</div>
          <div class="m-val">Kenmore</div>
          <div class="m-sub">SOC 2 Compliant</div>
        </div>
      </div>
    </div>
    <div class="split-right">
      <img src="assets/hero_terminal.jpg" alt="Active Trading Floor">
      <div class="img-overlay-card">
        <div>
          <div style="font-size:12px; font-weight:700; color:#FFF;">Corporate Operational Flow</div>
          <div style="font-size:11px; color:var(--muted);">OPEX & Capitalization Account (Separate from Client Margin)</div>
        </div>
        <div class="status-pill">VERIFIED UBOs</div>
      </div>
    </div>
  </div>

  <!-- SLIDE 3: 12 GROUP ECOSYSTEM (DETRONIC ENERGIA & FACTORONE) -->
  <div class="slide">
    <div class="split-left">
      <div>
        <div class="slide-cat">02. CORPORATE BACKING</div>
        <h2 class="slide-title">12 Group: Real Operating Assets</h2>
        <div class="card-stack">
          <div class="info-card">
            <h4>Detronic Energia (Photovoltaic Infrastructure)</h4>
            <p>Active solar power generation utility in Brazil, generating real commercial revenue and providing capital depth and tangible infrastructure to 12 Group.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--blue);">
            <h4>FactorOne / FactorHub (Systems & Domestic FinTech)</h4>
            <p>Technology division headed by Fayson Santos. Operates on a separate domestic BaaS track targeting future Central Bank of Brazil (BACEN) licensing.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--emerald);">
            <h4>Dual-Track Regulatory Ring-Fencing</h4>
            <p>12 Capital (St. Lucia offshore) and FactorOne (Brazil domestic) maintain strict corporate separation with no balance-sheet commingling.</p>
          </div>
        </div>
      </div>
      <div style="font-size:11.5px; color:var(--muted); font-family:'JetBrains Mono',monospace;">
        Holding: 12 Group • Clean Energy • Financial Software • Offshore Brokerage
      </div>
    </div>
    <div class="split-right">
      <img src="assets/energy_solar.jpg" alt="Detronic Energia Solar Plant">
      <div class="img-overlay-card">
        <div>
          <div style="font-size:12px; font-weight:700; color:#FFF;">Detronic Energia • 12 Group Asset</div>
          <div style="font-size:11px; color:var(--muted);">Commercial Solar Photovoltaic Generation Infrastructure</div>
        </div>
        <div class="status-pill" style="background:rgba(212,175,55,0.15); border-color:var(--gold); color:var(--gold);">REAL ASSET</div>
      </div>
    </div>
  </div>

  <!-- SLIDE 4: MULTI-ASSET & 12 TERMINAL AI -->
  <div class="slide">
    <div class="split-left">
      <div>
        <div class="slide-cat">03. PRODUCTS & AI TECHNOLOGY</div>
        <h2 class="slide-title">Multi-Asset Matrix & 12 Terminal AI</h2>
        <div class="card-stack">
          <div class="info-card">
            <h4>Câmbio Global & Multi-Asset Markets</h4>
            <p>55+ FX pairs, Spot Gold (XAU/USD), Silver, Crude Oil, S&P 500, Nasdaq 100, and US Equities with raw ECN spreads from 0.0 pips via Luramic.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--gold);">
            <h4>12 Intelligence Terminal (AI DRE Analyzer)</h4>
            <p>Proprietary financial analysis dashboard allowing corporate clients to upload audited DRE/balance sheets for automated solvency scoring and debt coverage.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--blue);">
            <h4>De-Stigmatizing Forex</h4>
            <p>Positioned as an institutional multi-asset wealth platform, serving both active traders and conservative wealth builders.</p>
          </div>
        </div>
      </div>
      <div class="metrics-grid">
        <div class="m-card">
          <div class="m-label">Gold (XAU/USD)</div>
          <div class="m-val">$2,684.50</div>
          <div class="m-sub">Raw Spreads</div>
        </div>
        <div class="m-card">
          <div class="m-label">AI DRE Audit</div>
          <div class="m-val">Real-time</div>
          <div class="m-sub">Solvency Benchmark</div>
        </div>
        <div class="m-card">
          <div class="m-label">FX Spreads</div>
          <div class="m-val">From 0.0</div>
          <div class="m-sub">EUR/USD, USD/JPY</div>
        </div>
      </div>
    </div>
    <div class="split-right">
      <img src="assets/multi_asset_app.jpg" alt="12 Capital Terminal and App">
      <div class="img-overlay-card">
        <div>
          <div style="font-size:12px; font-weight:700; color:#FFF;">12 Intelligence Terminal</div>
          <div style="font-size:11px; color:var(--muted);">AI Financial Statement Analysis • Luramic STP Connectivity</div>
        </div>
        <div class="status-pill">AI POWERED</div>
      </div>
    </div>
  </div>

  <!-- SLIDE 5: STP EXECUTION ARCHITECTURE -->
  <div class="slide">
    <div class="split-left">
      <div>
        <div class="slide-cat">04. ORDER EXECUTION</div>
        <h2 class="slide-title">100% STP Execution & Global Highways</h2>
        <div class="card-stack">
          <div class="info-card">
            <h4>Zero Dealing Desk Conflict (A-Book Only)</h4>
            <p>12 Capital does not make markets or bet against clients. Every order is matched back-to-back to Luramic institutional pools, eliminating market risk.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--emerald);">
            <h4>Sub-Millisecond Execution Latency</h4>
            <p>Direct low-latency fiber routes connecting client terminals to financial hubs in London Equinix LD4, New York NY4, and Frankfurt.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--blue);">
            <h4>Automated Stop-Out & Negative Balance Protection</h4>
            <p>Automated margin calls at 100% and algorithmic stop-outs at 50% prevent accounts from falling into clearing deficits.</p>
          </div>
        </div>
      </div>
      <div style="font-size:11.5px; color:var(--muted); font-family:'JetBrains Mono',monospace;">
        Latency: 0.89ms (LD4) • Primary Clearing: Luramic • Broker Risk: Zero
      </div>
    </div>
    <div class="split-right">
      <img src="assets/global_network.jpg" alt="Global Financial Routes">
      <div class="img-overlay-card">
        <div>
          <div style="font-size:12px; font-weight:700; color:#FFF;">Global STP Execution Highways</div>
          <div style="font-size:11px; color:var(--muted);">Saint Lucia ➔ London LD4 ➔ New York NY4 ➔ Frankfurt</div>
        </div>
        <div class="status-pill" style="background:rgba(59,130,246,0.15); border-color:var(--blue); color:var(--blue);">0.89ms LATENCY</div>
      </div>
    </div>
  </div>

  <!-- SLIDE 6: WEALTH STRUCTURING & BOARD -->
  <div class="slide">
    <div class="split-left">
      <div>
        <div class="slide-cat">05. GOVERNANCE & WEALTH</div>
        <h2 class="slide-title">Offshore Wealth Structuring & Board</h2>
        <div class="card-stack">
          <div class="info-card">
            <h4>Cláudio (Chief Executive Officer)</h4>
            <p>Leads group strategy, banking expansion, international partnerships, and high-level institutional alliances.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--blue);">
            <h4>André (Founding Partner & Governance Director)</h4>
            <p>Directs holding capital allocation, fiduciary standards, and long-term asset preservation architecture.</p>
          </div>
          <div class="info-card" style="border-left-color:var(--emerald);">
            <h4>Fayson Santos (Head of Technology & Operations)</h4>
            <p>Senior architect directing the broker bridge, Kenmore Design CRM, FactorHub systems, and compliance coordination.</p>
          </div>
        </div>
      </div>
      <div class="metrics-grid">
        <div class="m-card">
          <div class="m-label">Structuring</div>
          <div class="m-val">St. Lucia IBC</div>
          <div class="m-sub">Tax Neutral</div>
        </div>
        <div class="m-card">
          <div class="m-label">Compliance</div>
          <div class="m-val">FATF / GAFI</div>
          <div class="m-sub">3-Tier KYC</div>
        </div>
        <div class="m-card">
          <div class="m-label">Client Segregation</div>
          <div class="m-val">100%</div>
          <div class="m-sub">Ring-Fenced</div>
        </div>
      </div>
    </div>
    <div class="split-right">
      <img src="assets/board_wealth.jpg" alt="Boardroom and Wealth Advisory">
      <div class="img-overlay-card">
        <div>
          <div style="font-size:12px; font-weight:700; color:#FFF;">Executive Board & Governance</div>
          <div style="font-size:11px; color:var(--muted);">Cláudio (CEO) • André (Governance) • Fayson (Tech/Ops)</div>
        </div>
        <div class="status-pill">BOARD DIRECTORS</div>
      </div>
    </div>
  </div>

  <!-- SLIDE 7: FINANCIAL PROJECTIONS -->
  <div class="slide">
    <div class="split-left" style="flex:1;">
      <div class="slide-cat">06. FINANCIAL MODEL</div>
      <h2 class="slide-title">Three-Year Financial Projections & Solvency</h2>
      <div class="card-stack">
        <div class="info-card">
          <h4>Conservative Baseline Assumptions</h4>
          <p>Initial Year 1 baseline of USD 5,000,000 monthly volume (USD 60M/yr), scaling 100% YoY to USD 10M/mo (USD 120M/yr) in Year 2 and USD 20M/mo (USD 240M/yr) in Year 3.</p>
        </div>
      </div>
      <div class="metrics-grid" style="grid-template-columns:repeat(3,1fr); margin-top:20px;">
        <div class="m-card">
          <div class="m-label">Year 1 (Baseline)</div>
          <div class="m-val">$5M / mo</div>
          <div class="m-sub">Gross Rev: $185k • Break-even M5</div>
        </div>
        <div class="m-card">
          <div class="m-label">Year 2 (+100%)</div>
          <div class="m-val">$10M / mo</div>
          <div class="m-sub">Gross Rev: $401k • EBITDA: $109k</div>
        </div>
        <div class="m-card">
          <div class="m-label">Year 3 (+100%)</div>
          <div class="m-val">$20M / mo</div>
          <div class="m-sub">Gross Rev: $851k • Buffer: $455k</div>
        </div>
      </div>
      <div style="margin-top:20px; font-size:12px; color:var(--muted);">
        The Company retains 30% of net profits in an unencumbered Solvency Capital Reserve, accumulating $455,500+ by Year 3 to fund future international banking capitalization.
      </div>
    </div>
  </div>

  <!-- SLIDE 8: ROADMAP TO BANK -->
  <div class="slide">
    <div class="split-left" style="flex:1;">
      <div class="slide-cat">07. STRATEGIC HORIZON</div>
      <h2 class="slide-title">Transition Blueprint: Towards a Licensed Bank</h2>
      <div class="card-stack">
        <div class="info-card">
          <h4>Phase 1 (Months 1–6): Operational Brokerage & Banking Integration</h4>
          <p>$5M/month volume baseline; Luramic and Kenmore live; Corporate operational bank account activated.</p>
        </div>
        <div class="info-card" style="border-left-color:var(--blue);">
          <h4>Phase 2 (Months 6–18): Scale Brokerage & Accumulate Capital Reserve</h4>
          <p>$10M/month volume; 12 Intelligence Terminal deployed; $350k+ accumulated in capital escrow.</p>
        </div>
        <div class="info-card" style="border-left-color:var(--emerald);">
          <h4>Phase 3 & 4 (Months 18–30): Caribbean Regulatory Advisory & $1M-$2.5M Capitalization</h4>
          <p>Retain Caribbean banking counsel; submit formal Class B/A application to Saint Lucia FSRA backed by 12 Group capital.</p>
        </div>
        <div class="info-card" style="border-left-color:var(--gold);">
          <h4>Phase 5 (Months 30–36): Cloud Core Banking & SWIFT Direct Connectivity</h4>
          <p>Deploy Mambu/Skale core banking platform; acquire SWIFT BIC; transition clients to 12 International Digital Bank.</p>
        </div>
      </div>
    </div>
  </div>

</main>

<!-- BOTTOM CONTROLS -->
<footer class="bottom-controls">
  <div class="slide-indicator">
    SLIDE <strong id="slideNum">1</strong> OF <strong id="slideTotal">8</strong>
  </div>

  <div class="btn-group">
    <button class="nav-btn" id="prevBtn">← Previous</button>
    <button class="nav-btn primary" id="nextBtn">Next →</button>
    <button class="nav-btn" id="fullBtn">⛶ Fullscreen</button>
  </div>
</footer>

<script>
  let currentSlide = 0;
  const slides = document.querySelectorAll('.slide');
  const totalSlides = slides.length;
  const progressBar = document.getElementById('progressBar');
  const slideNum = document.getElementById('slideNum');
  const slideTotal = document.getElementById('slideTotal');
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const fullBtn = document.getElementById('fullBtn');

  slideTotal.textContent = totalSlides;

  function updateSlide(idx) {
    slides.forEach((s, i) => {
      s.classList.toggle('active', i === idx);
    });
    slideNum.textContent = idx + 1;
    progressBar.style.width = ((idx + 1) / totalSlides * 100) + '%';
    prevBtn.disabled = idx === 0;
    nextBtn.textContent = (idx === totalSlides - 1) ? 'Finish ↺' : 'Next →';
  }

  function next() {
    currentSlide = (currentSlide + 1) % totalSlides;
    updateSlide(currentSlide);
  }

  function prev() {
    if (currentSlide > 0) {
      currentSlide--;
      updateSlide(currentSlide);
    }
  }

  nextBtn.addEventListener('click', next);
  prevBtn.addEventListener('click', prev);

  fullBtn.addEventListener('click', () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => console.log(err));
      fullBtn.textContent = '✕ Exit';
    } else {
      document.exitFullscreen();
      fullBtn.textContent = '⛶ Fullscreen';
    }
  });

  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'Space') {
      e.preventDefault();
      next();
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      prev();
    }
  });

  updateSlide(0);
</script>

</body>
</html>"""
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Successfully generated Gamma-style Interactive Presentation at {output_html_path}")

if __name__ == "__main__":
    pres_dir = r"c:\Users\Home\12-capital\docs\presentation"
    assets_dir = os.path.join(pres_dir, "assets")
    os.makedirs(pres_dir, exist_ok=True)
    pptx_path = os.path.join(pres_dir, "12_Capital_Compliance_Deck.pptx")
    html_path = os.path.join(pres_dir, "12_Capital_Presentation.html")
    
    create_enhanced_deck(pptx_path, assets_dir)
    generate_interactive_gamma_style_html(html_path, assets_dir)
