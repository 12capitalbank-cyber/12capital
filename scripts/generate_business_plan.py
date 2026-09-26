import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_callout_box(doc, title, text, bg_hex="F0F4F8", border_hex="1E3A8A"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, bg_hex)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border only
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:left w:val="single" w:sz="24" w:space="0" w:color="{border_hex}"/><w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/></w:tcBorders>')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(4)
    run_title = p.add_run(f"■ {title}\n")
    run_title.bold = True
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(10.5)
    run_title.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    
    run_text = p.add_run(text)
    run_text.font.name = "Calibri"
    run_text.font.size = Pt(9.5)
    run_text.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
    
    # Empty space after table
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(6)

def generate_docx(output_path):
    doc = docx.Document()
    
    # Page setup - 1 inch margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
    
    NAVY = RGBColor(0x0F, 0x2A, 0x4A)
    SLATE = RGBColor(0x47, 0x55, 0x69)
    GOLD = RGBColor(0x9A, 0x7B, 0x2F)
    BODY_TEXT = RGBColor(0x1E, 0x29, 0x3B)
    
    # ─── COVER PAGE ───
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(36)
    title_p.paragraph_format.space_after = Pt(6)
    r_sub = title_p.add_run("12 GROUP HOLDING • INSTITUTIONAL BANKING ONBOARDING DOSSIER\n")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11)
    r_sub.font.bold = True
    r_sub.font.color.rgb = GOLD
    
    r_title = title_p.add_run("12 CAPITAL INC.")
    r_title.font.name = "Calibri"
    r_title.font.size = Pt(32)
    r_title.font.bold = True
    r_title.font.color.rgb = NAVY
    
    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(4)
    sub_p.paragraph_format.space_after = Pt(28)
    r_desc = sub_p.add_run("INSTITUTIONAL BUSINESS PLAN & COMPLIANCE OVERVIEW\nMulti-Asset Brokerage, Straight-Through Execution (STP), and Risk Management Framework")
    r_desc.font.name = "Calibri"
    r_desc.font.size = Pt(13)
    r_desc.font.color.rgb = SLATE
    
    # Metadata Table
    meta_table = doc.add_table(rows=6, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Legal Entity Name:", "12 Capital Inc."),
        ("Jurisdiction of Formation:", "Saint Lucia (IBC Act, Cap. 12.14)"),
        ("Primary Operating Partners:", "Luramic (Prime Liquidity) • Kenmore Design (CRM & Portal)"),
        ("Parent Holding Entity:", "12 Group Holding"),
        ("Target Document Audience:", "Bank Compliance Officers, Risk Committee & MLRO"),
        ("Classification:", "Strictly Confidential — Commercial & Regulatory Due Diligence")
    ]
    for idx, (label, val) in enumerate(meta_data):
        row = meta_table.rows[idx]
        cell_lbl, cell_val = row.cells[0], row.cells[1]
        set_cell_background(cell_lbl, "F8FAFC")
        set_cell_background(cell_val, "FFFFFF")
        set_cell_margins(cell_lbl, top=80, bottom=80, left=120, right=120)
        set_cell_margins(cell_val, top=80, bottom=80, left=120, right=120)
        
        p0 = cell_lbl.paragraphs[0]
        p0.paragraph_format.space_after = Pt(2)
        r0 = p0.add_run(label)
        r0.font.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = NAVY
        
        p1 = cell_val.paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1 = p1.add_run(val)
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = BODY_TEXT
        
    doc.add_page_break()
    
    # ─── SECTION 1: EXECUTIVE SUMMARY ───
    h1 = doc.add_heading("1. Executive Summary & Purpose of Corporate Account", level=1)
    h1.paragraph_format.space_before = Pt(16)
    h1.paragraph_format.space_after = Pt(8)
    
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(6)
    p.add_run("12 Capital Inc. (\"12 Capital\" or the \"Company\") is an internationally structured multi-asset brokerage, market connectivity, and financial technology firm incorporated as an International Business Company (IBC) in Saint Lucia. The Company operates as the premier international financial services arm of 12 Group Holding, a diversified corporate conglomerate with proven operating assets in renewable energy (Detronic Energia, generating real commercial revenues in Brazil's photovoltaic sector) and financial software (FactorHub / FactorOne).\n\n"
              "Crucially, 12 Capital is already an active, operational brokerage facilitating live foreign exchange and CFD market transactions for an established base of international traders. The Company provides eligible international retail, professional, and corporate clients with seamless, low-latency access to global financial markets—including Foreign Exchange / Global Currencies (FX), Contracts for Difference (CFDs) on Global Indices, Commodities (Gold, Silver, Energy), Digital Assets, and Cross-Border Wealth Advisory.\n\n"
              "Operating strictly on a Straight-Through Processing (STP) / Direct Market Access (DMA) non-dealing desk model, 12 Capital does not engage in proprietary directional market making. All client order flow is routed directly to Tier-1 institutional liquidity providers, spearheaded by Luramic, thereby eliminating broker-client market conflict and market risk from the Company's balance sheet. Client management, regulatory onboarding, and payment processing orchestration are managed through enterprise-grade financial software provided by Kenmore Design.\n\n"
              "The Company's live web platform is deployed and publicly accessible for regulatory inspection at https://12capital.vercel.app (backed by institutional GitHub repository 12capitalbank-cyber/12capital).")
    
    create_callout_box(doc, "SPECIFIC PURPOSE OF THE CORPORATE BANK ACCOUNT",
                       "The requested corporate operational bank account will be strictly segregated from client margin depositories and utilized exclusively for:\n"
                       "1. Initial Shareholder Capitalization & Equity Injections from 12 Group Holding and verified UBOs.\n"
                       "2. Corporate Operating Expenditures (OPEX): Vendor invoices (Kenmore Design CRM, trading infrastructure), institutional liquidity clearing fees (Luramic), cloud hosting (Vercel, Supabase, AWS), external legal retainers, and executive salaries.\n"
                       "3. Liquidity Collateral Funding: Institutional margin deposits transferred to Luramic clearing accounts.\n"
                       "4. Retained Earnings & Dividends: Net broker revenues (spread markups and commissions) and lawful distributions.")

    # ─── SECTION 2: CORPORATE STRUCTURE & GOVERNANCE ───
    h2 = doc.add_heading("2. Corporate Structure, Jurisdiction & Ultimate Beneficial Ownership (UBO)", level=1)
    h2.paragraph_format.space_before = Pt(18)
    h2.paragraph_format.space_after = Pt(8)
    
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(6)
    p.add_run("12 Capital Inc. is incorporated pursuant to the International Business Companies Act, Cap. 12.14 of Saint Lucia. Saint Lucia was deliberately selected as the corporate domicile due to its established English Common Law legal tradition, adherence to OECD and FATF 40 Recommendations on AML/CFT, and commercial flexibility for cross-border capital facilitation.\n\n"
              "The Company's international operations are supported by a formal Legal Letter of Opinion issued by Caribbean legal counsel, affirming corporate good standing, capacity, and full legality of international financial facilitation services outside of Saint Lucia.\n\n"
              "Dual-Track Regulatory Architecture:\n"
              "12 Group Holding maintains a strict legal and operational separation between its offshore and domestic tracks:\n"
              "• Offshore International Track (12 Capital Inc. - Saint Lucia): Global currency markets, multi-asset brokerage, and cross-border wealth structuring for international non-resident clients.\n"
              "• Domestic Brazilian FinTech Track (FactorOne / FactorHub - Brazil): Independent domestic financial technology under Brazilian BaaS partnerships, preparing for future Central Bank (BACEN) licensing.\n"
              "The two entities do not commingle balances or operations, ensuring complete regulatory compliance across all jurisdictions.")
    
    doc.add_heading("Key Principals & Management", level=2)
    p_gov = doc.add_paragraph()
    p_gov.add_run("• Cláudio (Chief Executive Officer & Board Director): Leads corporate strategy, high-level banking expansion, commercial partnerships, and executive decision-making across 12 Group.\n"
                  "• André (Founding Partner & Board Director): Oversees group-wide capital allocation, fiduciary architecture, holding governance, and long-term asset preservation.\n"
                  "• Fayson Santos (Head of Technology & Broker Operations): Senior financial systems architect directing the operational bridge, Kenmore Design CRM deployment, Luramic liquidity connectivity, and banking compliance coordination.")

    create_callout_box(doc, "RING-FENCING & SEGREGATION PRINCIPLE (12 GROUP HOLDING)",
                       "As formally enacted in 12 Group Holding bylaws: 12 Capital operates as an independent, ring-fenced operational subsidiary with its own dedicated balance sheet. Under no circumstances are 12 Capital funds or client margin balances commingled with the cash flows of other group subsidiaries (Detronic Energia, FactorOne, 12 Systems) or used to fund external commercial projects.")


    # ─── SECTION 3: BUSINESS MODEL & MULTI-ASSET MATRIX ───
    doc.add_heading("3. Business Model & Multi-Asset Offering", level=1)
    p = doc.add_paragraph()
    p.add_run("To establish long-term institutional credibility and avoid the reputational stigma of pure speculative retail forex, 12 Capital operates a Multi-Asset Wealth & Trading Platform catering to two distinct client tiers: active algorithmic/retail traders and long-term corporate/wealth clients seeking capital dollarization, global ETFs, and US equities.\n\n"
              "Additionally, 12 Capital deploys the proprietary 12 Intelligence Terminal—an AI-driven financial intelligence interface where corporate and private clients can upload audited financial statements (DRE) for automated solvency benchmarking, fundamental analysis, and real-time macroeconomic radar monitoring.")

    # Product Table
    prod_table = doc.add_table(rows=7, cols=4)
    prod_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Asset Class", "Tradable Instruments", "Execution Model", "Primary Partner"]
    for c_idx, h_text in enumerate(headers):
        cell = prod_table.cell(0, c_idx)
        set_cell_background(cell, "0F2A4A")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        r = p.add_run(h_text)
        r.font.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    rows_data = [
        ("Foreign Exchange (FX)", "55+ Major, Minor & Exotic Currency Pairs", "STP / DMA (No Dealing Desk)", "Luramic Institutional"),
        ("Precious Metals", "XAU/USD (Gold), XAG/USD (Silver), Platinum", "STP / Raw Interbank Spreads", "Luramic Institutional"),
        ("Commodities & Energy", "WTI Crude Oil, Brent Crude, Natural Gas", "STP / Cash CFD", "Luramic Institutional"),
        ("Global Equity Indices", "US30, SPX500, NAS100, GER40, UK100", "STP / Direct Market Routing", "Luramic Institutional"),
        ("Global Equities & ETFs", "US Blue Chips (Apple, Microsoft), S&P 500 ETFs", "Direct Sub-Broker / Custody", "Institutional Clearing Rail"),
        ("Offshore Advisory", "International Holding Setup, Dollarization", "Fee-for-Service Advisory", "12 Capital Fiduciary Network")
    ]
    for r_idx, row_values in enumerate(rows_data):
        for c_idx, val in enumerate(row_values):
            cell = prod_table.cell(r_idx + 1, c_idx)
            bg = "F8FAFC" if r_idx % 2 == 0 else "FFFFFF"
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            r.font.color.rgb = BODY_TEXT

    # ─── SECTION 4: STP ORDER EXECUTION & LURAMIC ───
    doc.add_heading("4. Order Execution Architecture (STP / Non-Dealing Desk)", level=1)
    p = doc.add_paragraph()
    p.add_run("A critical pillar for banking risk mitigation is the elimination of market risk from the Company's balance sheet. 12 Capital strictly operates a 100% Non-Dealing Desk (NDD) Straight-Through Processing (STP) architecture.\n\n"
              "• Zero Proprietary Market Making: 12 Capital never trades against its clients or holds speculative open positions.\n"
              "• Back-to-Back Matching: Every trade is mirrored instantaneously into the institutional liquidity pool of Luramic.\n"
              "• Alignment of Interests: The Company derives its revenues entirely from transparent volume commissions and spread markups, meaning client trading longevity directly correlates with Company health.")

    # ─── SECTION 5: OPERATIONAL PARTNERS ───
    doc.add_heading("5. Operational Partners & Technology Infrastructure", level=1)
    p = doc.add_paragraph()
    p.add_run("12 Capital partners with top-tier, globally recognized software and liquidity counterparties:\n"
              "• Luramic: Institutional prime liquidity provider providing deep multi-bank liquidity feeds, raw ECN spreads, and daily automated settlement statements.\n"
              "• Kenmore Design: Recognized industry standard provider of broker CRM, Trader's Room (Client Cabinet), compliance document onboarding, and Payment Service Provider (PSP) orchestration.\n"
              "• Next.js 16, Supabase & Vercel Edge: Enterprise-grade web architecture with SOC 2 Type II certified physical datacenters, end-to-end tokenized sessions, and 99.99% operational uptime.")

    # ─── SECTION 6: AML/CFT & KYC FRAMEWORK ───
    doc.add_heading("6. Comprehensive AML/CFT & KYC Compliance Framework", level=1)
    p = doc.add_paragraph()
    p.add_run("12 Capital operates a robust compliance policy adhering strictly to the Financial Action Task Force (FATF) 40 Recommendations on Anti-Money Laundering and Counter-Financing of Terrorism:\n\n"
              "1. Three-Tier Customer Due Diligence (CDD):\n"
              "   - Tier 1 (Basic): Government-issued Passport/ID verification + automated 3D facial liveness biometrics.\n"
              "   - Tier 2 (Full): Proof of Residential Address (utility bill/bank statement under 90 days old).\n"
              "   - Tier 3 (Enhanced Due Diligence): Source of Wealth and Source of Funds declarations with supporting tax/bank documentation for accounts funding > $50,000.\n"
              "2. Sanctions & PEP Screening: Dynamic automated screening against OFAC, UN, EU, UK HM Treasury sanctions lists, and global Politically Exposed Persons (PEP) registries.\n"
              "3. Strict Anti-Third-Party Transaction Rule: Deposits and withdrawals are accepted solely from bank accounts, credit cards, or verified wallets bearing the exact legal name of the registered account holder.\n"
              "4. Prohibited Jurisdictions: The Company enforces geographic IP geofencing and KYC rejection for residents of the United States of America (US Persons), FATF Blacklist/Greylist nations (North Korea, Iran, Myanmar, Syria), and Saint Lucia domestic residents.")

    # ─── SECTION 7: RISK MANAGEMENT ───
    doc.add_heading("7. Risk Management & Capital Protection", level=1)
    p = doc.add_paragraph()
    p.add_run("• Negative Balance Protection (NBP): Algorithmic risk limits prevent client balances from dropping below zero during black-swan gap events.\n"
              "• Automated Margin Calls & Stop-Out: Real-time automated liquidation triggers at 50% margin level to protect client equity and prevent clearing deficit.\n"
              "• Treasury Segregation: Operational corporate funds are completely segregated from client margin pools.\n"
              "• Business Continuity Planning (BCP): Automated real-time database replication, sub-30 minute Recovery Time Objective (RTO), and continuous disaster recovery protocols.")

    # ─── SECTION 8: 3-YEAR FINANCIAL PROJECTIONS ───
    doc.add_heading("8. Three-Year Financial Forecast & Solvency Model", level=1)
    p = doc.add_paragraph()
    p.add_run("The financial forecast is constructed on conservative, audited assumptions based on an initial baseline of USD 5,000,000 monthly trading volume in Year 1, expanding by 100% year-over-year to USD 10,000,000/month in Year 2 and USD 20,000,000/month in Year 3.")

    # Financial Table
    fin_table = doc.add_table(rows=10, cols=4)
    fin_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    fin_headers = ["Financial Metric (USD)", "Year 1 (Baseline)", "Year 2 (+100%)", "Year 3 (+100%)"]
    for c_idx, h_text in enumerate(fin_headers):
        cell = fin_table.cell(0, c_idx)
        set_cell_background(cell, "0F2A4A")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        r = p.add_run(h_text)
        r.font.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    fin_data = [
        ("Active Client Accounts (Year End)", "250", "650", "1,500"),
        ("Monthly Average Trading Volume", "$5,000,000", "$10,000,000", "$20,000,000"),
        ("Annual Gross Trading Volume", "$60,000,000", "$120,000,000", "$240,000,000"),
        ("Gross Brokerage Revenue (Spreads/Comm.)", "$84,000", "$168,000", "$336,000"),
        ("Auxiliary Wealth, Advisory & Fund Fees", "$101,000", "$233,000", "$515,000"),
        ("TOTAL GROSS REVENUE", "$185,000", "$401,000", "$851,000"),
        ("Direct Liquidity & Bridge Costs (Luramic/PSP)", "($36,000)", "($67,000)", "($130,000)"),
        ("Total Operating Expenses (OPEX)", "($131,100)", "($224,900)", "($377,000)"),
        ("NET OPERATING PROFIT (EBITDA)", "$17,900", "$109,100", "$344,000"),
    ]
    for r_idx, row_values in enumerate(fin_data):
        for c_idx, val in enumerate(row_values):
            cell = fin_table.cell(r_idx + 1, c_idx)
            bg = "F1F5F9" if r_idx % 2 == 0 else "FFFFFF"
            if r_idx in [5, 8]:  # Highlight totals
                bg = "E2E8F0"
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            if r_idx in [5, 8]:
                r.font.bold = True
            r.font.color.rgb = BODY_TEXT

    p_break = doc.add_paragraph()
    p_break.paragraph_format.space_before = Pt(8)
    p_break.add_run("• Operational Break-Even: Month 5 of Year 1.\n"
                    "• Capital Solvency Buffer: The Company retains 30% of net profits in an unencumbered treasury reserve, accumulating $455,500+ by Year 3 to support future Class A/B International Banking capitalization.")

    # ─── SECTION 9: STATUTORY DECLARATION ───
    doc.add_heading("9. Statutory Declarations & Sign-Off", level=1)
    p = doc.add_paragraph()
    p.add_run("12 Capital Inc. affirms that all corporate equity contributions derive from legitimate commercial activities, that the Company maintains strict adherence to international regulatory standards, and commits to providing complete operational and financial transparency to its banking counterparties.\n\n"
              "For and on behalf of 12 Capital Inc.:\n\n\n"
              "_____________________________________________________\n"
              "Fayson Santos\n"
              "Managing Director & Authorized Signatory\n"
              "12 Capital Inc. (Saint Lucia IBC)\n"
              "Date: September 26, 2026")

    doc.save(output_path)
    print(f"Successfully generated DOCX at {output_path}")

def generate_html(output_path):
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>12 Capital Inc. — Institutional Business Plan & Compliance Dossier</title>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root {
  --navy: #0F2A4A;
  --dark: #0A192F;
  --slate: #475569;
  --light: #F8FAFC;
  --border: #E2E8F0;
  --gold: #9A7B2F;
  --gold-bg: #FAF5E8;
  --green: #0D7A53;
  --green-bg: #EDFDF5;
  --blue-bg: #EFF6FF;
  --blue-border: #BFDBFE;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Plus Jakarta Sans', sans-serif;
  color: #1E293B;
  background: #F1F5F9;
  line-height: 1.7;
  font-size: 14.5px;
  padding: 40px 20px;
}
.page-container {
  max-width: 960px;
  margin: 0 auto;
  background: #FFFFFF;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid var(--border);
}
.cover-header {
  background: linear-gradient(135deg, var(--dark) 0%, var(--navy) 100%);
  color: #FFFFFF;
  padding: 60px 50px;
  border-bottom: 4px solid var(--gold);
}
.cover-tag {
  display: inline-block;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #E2B96F;
  margin-bottom: 12px;
}
.cover-title {
  font-size: 34px;
  font-weight: 800;
  letter-spacing: -0.02em;
  margin-bottom: 12px;
}
.cover-subtitle {
  font-size: 16px;
  color: #94A3B8;
  max-width: 760px;
  font-weight: 400;
}
.meta-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  padding: 30px 50px;
  background: #F8FAFC;
  border-bottom: 1px solid var(--border);
}
.meta-item { font-size: 12.5px; }
.meta-label { color: var(--slate); font-weight: 600; text-transform: uppercase; font-size: 10.5px; letter-spacing: 0.05em; margin-bottom: 4px; }
.meta-value { color: var(--dark); font-weight: 700; }

.content-body { padding: 50px; }
h2 {
  font-size: 22px;
  color: var(--navy);
  font-weight: 800;
  margin-top: 40px;
  margin-bottom: 16px;
  padding-bottom: 8px;
  border-bottom: 2px solid #E2E8F0;
  display: flex;
  align-items: center;
  gap: 10px;
}
h2:first-of-type { margin-top: 0; }
h3 {
  font-size: 16px;
  color: var(--dark);
  font-weight: 700;
  margin-top: 24px;
  margin-bottom: 10px;
}
p { margin-bottom: 16px; color: #334155; }
ul, ol { margin-left: 20px; margin-bottom: 20px; color: #334155; }
li { margin-bottom: 8px; }

.callout {
  background: var(--blue-bg);
  border-left: 4px solid #2563EB;
  padding: 20px 24px;
  border-radius: 0 8px 8px 0;
  margin: 24px 0;
}
.callout-title {
  font-weight: 800;
  color: #1E3A8A;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 8px;
}
.callout-text { font-size: 13.5px; color: #1E293B; line-height: 1.6; }

.table-wrapper {
  overflow-x: auto;
  margin: 24px 0;
  border: 1px solid var(--border);
  border-radius: 8px;
}
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  text-align: left;
}
th {
  background: var(--navy);
  color: #FFFFFF;
  padding: 12px 16px;
  font-weight: 700;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
td {
  padding: 12px 16px;
  border-bottom: 1px solid var(--border);
  color: #334155;
}
tr:nth-child(even) td { background: #F8FAFC; }
tr:last-child td { border-bottom: none; }
.highlight-row td { background: #F1F5F9; font-weight: 700; color: var(--navy); }

.badge {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 999px;
  font-size: 11px;
  font-weight: 700;
}
.badge-green { background: var(--green-bg); color: var(--green); border: 1px solid #A7F3D0; }
.badge-gold { background: var(--gold-bg); color: var(--gold); border: 1px solid #FDE68A; }

.sign-box {
  margin-top: 50px;
  padding: 30px;
  background: #F8FAFC;
  border: 1px dashed #CBD5E1;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}

@media print {
  body { background: #FFF; padding: 0; font-size: 12px; }
  .page-container { box-shadow: none; border: none; }
  .cover-header { padding: 40px; }
  .content-body { padding: 30px; }
  h2 { page-break-before: auto; }
}
</style>
</head>
<body>

<div class="page-container">
  <div class="cover-header">
    <div class="cover-tag">12 GROUP HOLDING • STRICTLY CONFIDENTIAL</div>
    <div class="cover-title">12 CAPITAL INC.</div>
    <div class="cover-subtitle">Institutional Business Plan & Compliance Onboarding Dossier — Prepared for Corporate Banking & Risk Committee Review</div>
  </div>

  <div class="meta-grid">
    <div class="meta-item">
      <div class="meta-label">Jurisdiction</div>
      <div class="meta-value">Saint Lucia (IBC Act, Cap. 12.14)</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Execution Architecture</div>
      <div class="meta-value">100% STP / Non-Dealing Desk</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Core Partners</div>
      <div class="meta-value">Luramic (LP) • Kenmore (CRM)</div>
    </div>
    <div class="meta-item">
      <div class="meta-label">Document Date</div>
      <div class="meta-value">September 26, 2026</div>
    </div>
  </div>

  <div class="content-body">
    <h2>1. Executive Summary & Corporate Purpose</h2>
    <p><strong>12 Capital Inc.</strong> ("12 Capital" or the "Company") is an internationally structured multi-asset brokerage and financial technology firm incorporated as an International Business Company (IBC) in Saint Lucia. Operating as the flagship financial arm of <strong>12 Group Holding</strong> (which includes operational renewable solar assets under <strong>Detronic Energia</strong> and financial technology systems under <strong>FactorHub / FactorOne</strong>), the Company provides eligible international retail, professional, and corporate clients with institutional access to Foreign Exchange (FX), CFDs on Precious Metals, Commodities, Global Indices, and Cross-Border Wealth Solutions.</p>
    <p>Crucially, <strong>12 Capital is already an active, operational brokerage</strong> with live trading accounts, real transaction volume, and operational infrastructure. Operating exclusively on a <strong>Straight-Through Processing (STP) / Direct Market Access (DMA)</strong> model, 12 Capital does not hold speculative market risk or trade against its clients. Orders are routed directly to institutional liquidity providers, spearheaded by <strong>Luramic</strong>, while client relationship management and compliance verification are powered by <strong>Kenmore Design</strong>.</p>
    <p>The Company's live web platform is deployed and publicly accessible for regulatory inspection at <strong><a href="https://12capital.vercel.app" style="color:#2563EB;">https://12capital.vercel.app</a></strong>.</p>

    <div class="callout">
      <div class="callout-title">Exclusive Purpose of the Corporate Bank Account</div>
      <div class="callout-text">
        The requested corporate operational account will be held strictly separate from client depositories and used solely for:
        <br>• Initial Shareholder Capitalization & Equity Contributions from 12 Group Holding and verified UBOs.
        <br>• Corporate Operating Expenses (OPEX): Technology licensing (Kenmore Design), liquidity clearing (Luramic), cloud servers (Vercel/Supabase), legal retainers, and executive salaries.
        <br>• Institutional Liquidity Margin: Buffer collateral transferred to Luramic clearing accounts.
        <br>• Corporate Retained Earnings & Lawful Dividend Distributions.
      </div>
    </div>

    <h2>2. Corporate Structure & Dual-Track Governance</h2>
    <p>12 Capital Inc. is incorporated under the <em>International Business Companies Act, Cap. 12.14</em> of Saint Lucia, supported by a formal Caribbean Legal Letter of Opinion confirming capacity, good standing, and legality of cross-border financial facilitation services. 12 Group operates a clear <strong>Dual-Track Regulatory Architecture</strong>:</p>
    <ul>
      <li><strong>Offshore Track (12 Capital Inc. - Saint Lucia):</strong> Global currency markets and multi-asset execution for non-resident clients under international common law.</li>
      <li><strong>Domestic Track (FactorOne / FactorHub - Brazil):</strong> Separate domestic Brazilian banking-as-a-service (BaaS) and technology operations preparing for Central Bank (BACEN) licensing.</li>
    </ul>
    <p>Under 12 Group Holding bylaws, 12 Capital operates as an independent ring-fenced entity with zero commingling of customer balances or external group liabilities:</p>
    <ul>
      <li><strong>Cláudio (Chief Executive Officer & Board Director):</strong> Directs corporate strategy, institutional banking relations, commercial alliances, and executive leadership.</li>
      <li><strong>André (Founding Partner & Board Director):</strong> Oversees group capital allocation, corporate governance, and fiduciary oversight.</li>
      <li><strong>Fayson Santos (Head of Technology & Broker Operations):</strong> Leads technical architecture, trading bridges, Kenmore Design CRM integrations, and operational compliance.</li>
    </ul>

    <h2>3. Multi-Asset Portfolio & Products</h2>
    <p>To establish institutional credibility, 12 Capital combines active market execution with conservative wealth dollarization and corporate analytics tools:</p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Asset Class</th>
            <th>Instruments Offered</th>
            <th>Execution Model</th>
            <th>Primary Partner</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Foreign Exchange (FX)</strong></td>
            <td>55+ Major, Minor & Exotic Currency Pairs</td>
            <td><span class="badge badge-green">STP / DMA</span></td>
            <td>Luramic Institutional</td>
          </tr>
          <tr>
            <td><strong>Precious Metals</strong></td>
            <td>Gold (XAU/USD), Silver (XAG/USD), Platinum</td>
            <td><span class="badge badge-green">STP / DMA</span></td>
            <td>Luramic Institutional</td>
          </tr>
          <tr>
            <td><strong>Commodities & Energy</strong></td>
            <td>WTI Crude Oil, Brent, Natural Gas</td>
            <td><span class="badge badge-green">STP / Cash CFD</span></td>
            <td>Luramic Institutional</td>
          </tr>
          <tr>
            <td><strong>Global Indices</strong></td>
            <td>US30, SPX500, NAS100, GER40, UK100</td>
            <td><span class="badge badge-green">Direct STP Routing</span></td>
            <td>Luramic Institutional</td>
          </tr>
          <tr>
            <td><strong>Equities & ETFs</strong></td>
            <td>US Blue Chips, S&P 500 ETFs, Thematic Funds</td>
            <td><span class="badge badge-gold">Custody Rail</span></td>
            <td>Sub-Broker / Custody</td>
          </tr>
          <tr>
            <td><strong>Wealth & Advisory</strong></td>
            <td>Offshore Structuring, Capital Dollarization</td>
            <td><span class="badge badge-gold">Fee-for-Service</span></td>
            <td>12 Capital Fiduciary Network</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2>4. Technology Stack & Operational Partners</h2>
    <p>• <strong>Luramic:</strong> Institutional counterparty providing multi-bank liquidity aggregation, raw ECN pricing, and daily automated reconciliation statements.<br>
    • <strong>Kenmore Design:</strong> Core broker CRM, secure Client Cabinet (Trader's Room), KYC document capture, and multi-gateway PSP orchestration hub.<br>
    • <strong>Next.js 16, Supabase & Vercel Edge:</strong> Cloud infrastructure deployed across SOC 2 Type II certified datacenters, with AES-256 data-at-rest encryption, TLS 1.3, and mandatory 2FA.</p>

    <h2>5. Compliance, AML/CFT & KYC Framework</h2>
    <p>The Company enforces a rigorous AML/CFT framework structured around FATF 40 Recommendations:</p>
    <ul>
      <li><strong>Tiered Onboarding:</strong> Tier 1 (Passport/ID + 3D facial liveness biometrics); Tier 2 (Proof of address < 90 days); Tier 3 (Source of Wealth/Funds for accounts > $50,000).</li>
      <li><strong>Sanctions & PEP Screening:</strong> Automated screening against OFAC, UN, EU, UK sanctions lists, and global Politically Exposed Persons (PEP) registers.</li>
      <li><strong>Strict First-Party Rule:</strong> Deposits and withdrawals must match the client's verified legal name exactly. Third-party transfers and anonymous instruments are blocked.</li>
      <li><strong>Geographic Exclusions:</strong> Zero onboarding of US Persons (CFTC/SEC compliance), FATF Blacklist/Greylist nations, or domestic Saint Lucia residents.</li>
    </ul>

    <h2>6. Three-Year Financial Forecast & Solvency Analysis</h2>
    <p>Financial projections reflect a conservative baseline starting at <strong>USD 5,000,000 monthly volume</strong> in Year 1, expanding 100% YoY to <strong>USD 10,000,000/month</strong> in Year 2 and <strong>USD 20,000,000/month</strong> in Year 3:</p>

    <div class="table-wrapper">
      <table>
        <thead>
          <tr>
            <th>Financial Metric (USD)</th>
            <th>Year 1 (Baseline)</th>
            <th>Year 2 (+100%)</th>
            <th>Year 3 (+100%)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Active Trading Accounts</td>
            <td>250</td>
            <td>650</td>
            <td>1,500</td>
          </tr>
          <tr>
            <td>Monthly Average Volume</td>
            <td>$5,000,000</td>
            <td>$10,000,000</td>
            <td>$20,000,000</td>
          </tr>
          <tr>
            <td>Annual Gross Volume</td>
            <td>$60,000,000</td>
            <td>$120,000,000</td>
            <td>$240,000,000</td>
          </tr>
          <tr>
            <td>Gross Brokerage Revenues (Spreads/Comm.)</td>
            <td>$84,000</td>
            <td>$168,000</td>
            <td>$336,000</td>
          </tr>
          <tr>
            <td>Auxiliary Wealth & Advisory Fees</td>
            <td>$101,000</td>
            <td>$233,000</td>
            <td>$515,000</td>
          </tr>
          <tr class="highlight-row">
            <td>TOTAL GROSS REVENUES</td>
            <td>$185,000</td>
            <td>$401,000</td>
            <td>$851,000</td>
          </tr>
          <tr>
            <td>Direct Clearing Costs (Luramic/PSP)</td>
            <td>($36,000)</td>
            <td>($67,000)</td>
            <td>($130,000)</td>
          </tr>
          <tr>
            <td>Operating Expenses (OPEX)</td>
            <td>($131,100)</td>
            <td>($224,900)</td>
            <td>($377,000)</td>
          </tr>
          <tr class="highlight-row">
            <td>NET OPERATING PROFIT (EBITDA)</td>
            <td>$17,900</td>
            <td>$109,100</td>
            <td>$344,000</td>
          </tr>
          <tr>
            <td><strong>Retained Solvency Buffer (Cumulative)</strong></td>
            <td><strong>$15,400</strong></td>
            <td><strong>$120,000</strong></td>
            <td><strong>$455,500</strong></td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="sign-box">
      <div>
        <p style="font-weight:700; color:var(--navy); margin-bottom:4px;">12 CAPITAL INC. — EXECUTIVE ATTESTATION</p>
        <p style="font-size:12px; color:var(--slate); margin-bottom:0;">Submitted to Banking Compliance & Risk Committee</p>
      </div>
      <div style="text-align:right;">
        <p style="font-weight:800; color:var(--dark); margin-bottom:2px;">Fayson Santos</p>
        <p style="font-size:12px; color:var(--slate); margin-bottom:0;">Managing Director & Authorized Signatory</p>
      </div>
    </div>
  </div>
</div>

</body>
</html>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Successfully generated HTML at {output_path}")

if __name__ == "__main__":
    docs_dir = r"c:\Users\Home\12-capital\docs\business_plan"
    os.makedirs(docs_dir, exist_ok=True)
    docx_path = os.path.join(docs_dir, "12_Capital_Institutional_Business_Plan.docx")
    html_path = os.path.join(docs_dir, "12_Capital_Institutional_Business_Plan.html")
    
    generate_docx(docx_path)
    generate_html(html_path)
