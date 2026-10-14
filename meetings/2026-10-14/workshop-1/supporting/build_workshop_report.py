"""Build the team-shareable Workshop 1 Murabaha report from reviewed source notes.

Run with the Codex bundled Python runtime. Source claims and timestamp references are
intentionally explicit; this script does not treat spoken proposals as approvals.
"""

from pathlib import Path
from xml.sax.saxutils import escape
import csv

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table,
    TableStyle, PageBreak, KeepTogether, HRFlowable,
)

ROOT = Path(__file__).resolve().parents[4]
WORKSHOP = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output/pdf/Bede_LMS_Workshop_1_Murabaha_Report_2026-10-14.pdf"
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold")

NAVY = colors.HexColor("#183153")
BLUE = colors.HexColor("#2459A8")
PALE = colors.HexColor("#EAF2FB")
ICE = colors.HexColor("#F4F7FA")
TEAL = colors.HexColor("#0C7C86")
AMBER = colors.HexColor("#A86512")
INK = colors.HexColor("#202C3B")
MUTED = colors.HexColor("#5B6879")
LINE = colors.HexColor("#D5DEE8")

styles = {
    "eyebrow": ParagraphStyle("eyebrow", fontName="Arial-Bold", fontSize=9, leading=12, textColor=TEAL, spaceAfter=12),
    "cover_title": ParagraphStyle("cover_title", fontName="Arial-Bold", fontSize=29, leading=34, textColor=NAVY, spaceAfter=16),
    "cover_sub": ParagraphStyle("cover_sub", fontName="Arial", fontSize=13, leading=18, textColor=MUTED, spaceAfter=25),
    "h1": ParagraphStyle("h1", fontName="Arial-Bold", fontSize=17, leading=21, textColor=NAVY, spaceAfter=13),
    "h2": ParagraphStyle("h2", fontName="Arial-Bold", fontSize=11, leading=14, textColor=BLUE, spaceBefore=11, spaceAfter=6),
    "body": ParagraphStyle("body", fontName="Arial", fontSize=9.1, leading=13.3, textColor=INK, spaceAfter=8),
    "small": ParagraphStyle("small", fontName="Arial", fontSize=8, leading=11.5, textColor=INK, spaceAfter=5),
    "tiny": ParagraphStyle("tiny", fontName="Arial", fontSize=7.35, leading=10, textColor=INK),
    "note": ParagraphStyle("note", fontName="Arial", fontSize=8.2, leading=12, textColor=MUTED, spaceAfter=8),
    "table_head": ParagraphStyle("table_head", fontName="Arial-Bold", fontSize=8, leading=10.5, textColor=colors.white),
    "table": ParagraphStyle("table", fontName="Arial", fontSize=7.65, leading=10.6, textColor=INK),
    "table_bold": ParagraphStyle("table_bold", fontName="Arial-Bold", fontSize=7.65, leading=10.6, textColor=NAVY),
    "callout": ParagraphStyle("callout", fontName="Arial-Bold", fontSize=10.2, leading=14.5, textColor=NAVY),
}

def p(text, style="body"):
    return Paragraph(text, styles[style])

def heading(text):
    return p(text, "h1")

def sub(text):
    return p(text, "h2")

def bullet(text, compact=False):
    return p("<font color='#2459A8'><b>•</b></font>  " + text, "small" if compact else "body")

def tag(text, bg=PALE):
    t = Table([[p(text, "callout")]], colWidths=[498])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    return t

def grid(headers, rows, widths, font="table", pad=7):
    data = [[p(escape(str(x)), "table_head") for x in headers]]
    for row in rows:
        data.append([p(str(x), "table_bold" if i == 0 else font) for i, x in enumerate(row)])
    t = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, ICE]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, 0), 0.7, BLUE),
        ("INNERGRID", (0, 1), (-1, -1), 0.3, LINE),
        ("BOX", (0, 0), (-1, -1), 0.5, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), pad),
        ("RIGHTPADDING", (0, 0), (-1, -1), pad),
        ("TOPPADDING", (0, 0), (-1, -1), pad),
        ("BOTTOMPADDING", (0, 0), (-1, -1), pad),
    ]))
    return t

def section_start(number, title, kicker):
    return [p(kicker.upper(), "eyebrow"), heading(f"{number}. {title}")]

def draw_page(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(NAVY)
    canvas.rect(0, h-11, w, 11, fill=1, stroke=0)
    canvas.setFillColor(NAVY)
    canvas.setFont("Arial-Bold", 8)
    canvas.drawString(48, h-37, "BEDE LMS  /  WORKSHOP 1  /  MURABAHA")
    canvas.setStrokeColor(LINE)
    canvas.line(48, h-45, w-48, h-45)
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(48, 28, "Team discussion draft  |  14 October 2026  |  Source: Workshop1-a and Workshop1-b")
    canvas.drawRightString(w-48, 28, f"Page {doc.page}")
    canvas.restoreState()

class ReportDoc(BaseDocTemplate):
    pass

doc = ReportDoc(str(OUTPUT), pagesize=A4, rightMargin=48, leftMargin=48,
                topMargin=62, bottomMargin=51, title="Bede LMS Workshop 1 - Murabaha Report",
                author="Bede project review", subject="Workshop assessment and action report")
frame = Frame(48, 51, A4[0]-96, A4[1]-113, leftPadding=0, rightPadding=0,
              topPadding=0, bottomPadding=0, id="normal")
doc.addPageTemplates(PageTemplate(id="report", frames=[frame], onPage=draw_page))
story = []

# Cover
story += [Spacer(1, 38), p("WORKSHOP REPORT / 14 OCTOBER 2026", "eyebrow"),
          p("Murabaha: decisions, capability and delivery evidence", "cover_title"),
          p("Bede Loan Management System - Workshop 1", "cover_sub"),
          tag("Purpose: give the project team one shared record of what was discussed, what remains open, and what evidence is needed before a capability can be accepted."),
          Spacer(1, 20), sub("At a glance")]
story += [grid(["Source", "Review status", "Main conclusion"], [
    ["Two Voice Memos; about 117 minutes captured", "Draft for participant review", "The target Murabaha flow and current LMS capability have not yet been reconciled."],
], [139, 126, 233])]
story += [Spacer(1, 18), sub("Four decisions to resolve first"),
          bullet("Confirm first product, governing document version and exclusions."),
          bullet("Approve the event sequence from commodity purchase through sale, disbursement and receivable activation."),
          bullet("Assign sale confirmation and bank-disbursement orchestration across backend, LMS and bank."),
          bullet("Approve accounting, fixed-profit, deferment and Ibra rules with numerical examples."),
          Spacer(1, 18), p("Status rule: workshop statements, demonstrations and proposed enhancements are not executed acceptance tests or formal Sharia, finance or scope approvals.", "note"), PageBreak()]

# Page 2: provenance and executive assessment
story += section_start("1", "Executive assessment", "What the meeting established")
story += [p("Participants worked through Murabaha accounting and workflow questions. They described desired financial treatment, current system behavior and proposed changes, but repeatedly left detailed rules for later finance, Sharia, risk and integration review. The first recording focuses on accounting and Ibra; the second focuses on servicing, product scope, lifecycle and integration. [A 00:01-33:51; B 00:04-83:26]"),
          sub("The central delivery risk"),
          tag("A present-tense product claim must be connected to a named build, agreed product rule, observable transaction and executed test. A screen demonstration of partial Ibra or a verbal sale gate does not by itself verify the complete Murabaha process.", PALE),
          sub("Findings that materially affect the plan"),
          bullet("The group described commodity, offer and acceptance activities in a mobile/backend process outside LMS, while expecting lifecycle evidence to be available in LMS. The event owner and exact sequence remain open. [B 43:49-56:55]"),
          bullet("Current percentage-based pricing can produce a schedule, but participants also described a fixed contractual profit after sale. Days-based deferment and an older profit-adding scheme require explicit policy reconciliation. [B 29:43-42:02; 68:26-70:43]"),
          bullet("Gross receivable, deferred profit, suspense, charity, legal costs and reconciliation need signed journal examples and system ownership. [A 02:32-29:32; B 01:54-19:54]"),
          bullet("FOO-side participants reported existing partial Ibra, DPD buckets, installment deferment and full write-off. Bede-specific rules, configuration and tests remain open; partial write-off and configurable stage actions were described as enhancements. [A 30:17-33:51; B 04:19-07:15; 20:23-42:02]"),
          sub("Evidence level used in this report"),
          grid(["Level", "Meaning"], [
              ["Discussed", "A statement, question, example or proposal in the recording."],
              ["Demonstrated", "A participant walked through a screen; configuration and financial output were not independently checked."],
              ["Specified", "A written requirement or BRD describes target behavior."],
              ["Verified", "A versioned build produces the agreed result in an executed, retained test. No new verification was performed for this report."],
          ], [113, 385]), PageBreak()]

# Page 3: lifecycle
story += section_start("2", "Murabaha lifecycle and system handoffs", "The pivotal open design")
story += [p("The row order below is a <b>working test model drawn from the existing lifecycle BRD</b>, not a sequence approved in this workshop. Participants used 'activation' at different points. They did agree in principle that sale confirmation precedes disbursement, while the exact contract-signing, receivable and schedule timing remained inconsistent. [B 43:49-56:55]"),
          grid(["Stage", "Evidence or owner to define", "Gate to test"], [
              ["1. Approval", "Eligibility and approved application; identify where an undisbursed commitment is shown.", "Approval alone must not imply an active receivable."],
              ["2. Commodity purchase", "External trade platform/backend reference, date and amount.", "Purchase evidence is recorded before sale."],
              ["3. Ownership / possession", "Bede ownership, possession and supporting documents; LMS persistence and audit.", "Sale is blocked if either evidence item is absent."],
              ["4. Offer / acceptance", "Customer-facing offer, version, signature/acceptance and expiry.", "Customer acceptance matches the approved terms."],
              ["5. Sale execution", "Authoritative sale-complete event and caller; maker-checker where applicable.", "No premature sale; immutable contractual price/profit."],
              ["6. Disbursement", "Backend or LMS request to bank; bank response, retries and idempotency.", "No disbursement before sale; reconcile failures."],
              ["7. Receivable / schedule", "Who activates the account, schedule and GL, and on which confirmed event.", "State, schedule and GL agree with bank movement."],
          ], [103, 245, 150], pad=6),
          Spacer(1, 8), p("Current architecture described in the call: the backend triggers KFH/EFTS disbursement; the commodity workflow is outside LMS. LMS-led disbursement was explored as an alternative, not selected. Bank-success/LMS-failure and payment-success/LMS-failure incidents were cited as reasons for reconciliation and recovery design. [B 43:49-53:05]", "small"),
          sub("Decision package required"),
          bullet("One approved swimlane diagram with event names, API callers, success/failure callbacks and source of truth for each state.", True),
          bullet("A transaction evidence chain covering purchase, ownership, possession, offer, acceptance, sale, bank movement, LMS receivable and audit corrections.", True),
          bullet("Negative tests before each gate and one positive end-to-end case on a named build.", True), PageBreak()]

# Page 4: accounting
story += section_start("3", "Accounting and financial controls", "Rules requiring examples and sign-off")
story += [grid(["Area", "Workshop discussion", "Required output"], [
    ["Receivable / deferred profit", "Gross selling-price receivable and deferred profit were discussed; net presentation in GL was described. [A 02:32-05:13]", "Approved event-by-event journals and sample 10,000 cost / 750 profit reconciliation."],
    ["Subledger / ERP", "LMS subledger, Bede and Oracle ERP export roles, plus period close, were discussed. [A 05:16-11:36]", "Book-of-record and close-owner matrix; mapping, timing and closed-period controls."],
    ["Daily reconciliation", "Compare against independent bank/core movements, not only LMS posting logs. [A 11:38-14:48]", "Transaction and balance feeds; matching rules, exceptions and sample reconciled day."],
    ["Undisbursed approvals", "Visibility or off-balance commitments were raised; treatment not settled. [A 15:24-18:40]", "Rule for recognition, display, reversal and expiry before bank disbursement."],
    ["Non-performing profit", "Stop new accrual versus transfer unpaid recognized profit to suspense; cooling-off and recovery discussed. [A 18:51-29:32]", "Trigger thresholds, account-level suspense, journal and recovery examples."],
    ["Legal costs / charity", "Legal costs were described as recoverable amounts; late charges as charity, not income. [B 01:54-04:19; 16:08-19:54]", "Approved payment, recovery, charity payout and approval entries."],
    ["ECL", "Bede model was described as calculation owner with LMS data input; feedback route unclear. [B 26:34-27:36]", "Data dictionary, import/export contract and account-level tie-out."],
], [113, 211, 174], pad=6),
          Spacer(1, 10), tag("Finance gate: do not finalize ledger configuration from verbal examples. The project needs an approved journal matrix, example balances, posting dates, close rules and reconciliation tests.", ICE), PageBreak()]

# Page 5: servicing
story += section_start("4", "Servicing and product rules", "Current claims versus target behavior")
story += [grid(["Topic", "Reported or discussed", "Open acceptance rule"], [
    ["Ibra / settlement", "FOO walked through partial Ibra modes. Early settlement and cheque charges were discussed. [A 30:17-33:51; B 00:04-01:54]", "Eligible unearned profit, overdue unpaid profit, approvals, caps, GL, letters and tenor-vs-payment effect. [B 76:18-78:53]"],
    ["Fixed profit / deferment", "Contractual total was described as fixed post-sale; installment deferment exists; days-based deferment requested. [B 07:24-09:51; 29:43-42:02]", "No silent profit change; decide whether an old profit-adding deferment scheme applies, plus fee, consent and document rules."],
    ["Top-up", "Bede described a new Murabaha contract and commodity purchase, unlike a conventional LMS top-up. [B 09:51-15:37]", "New application/eligibility, old-contract treatment, API owner and accounting."],
    ["Write-off", "Full write-off reported available; partial write-off reported as requiring development. [B 04:19-07:15]", "Scope decision, estimate, authorization, journals and regression tests."],
    ["Delinquency / collections", "DPD buckets reported; amount/count thresholds and stage actions need detail. [B 20:23-27:36]", "Risk matrix, cooling-off, work queues, notifications and ECL handoff."],
    ["Notifications", "Product-configurable automated messages were described as needing development. [B 28:04-29:27]", "Trigger, channel, recipient, language, template and delivery evidence."],
    ["Offer / schedules", "Offer expiry, APR, net disbursement fees, step-up/down and skipped months raised. [B 64:58-75:49]", "Signed product examples; check variable installment amounts and Sharia treatment."],
], [99, 202, 197], pad=6),
          Spacer(1, 10), p("Scope warning: a participant verbally described Tawarruq as likely first product and set aside Wa'd, Hamish, Takaful and multi-currency 'for now'. This needs a versioned scope decision against the written requirements and BRDs. [B 42:35-43:49; 57:19-64:58]", "small"), PageBreak()]

# Page 6: crosswalk
story += section_start("5", "Requirements and capability crosswalk", "Use for change and test planning")
story += [p("Written requirement references below come from the Bede-Foo LMS scope extract. They indicate where to reconcile the workshop discussion; they do not establish agreed scope or implementation status."),
          grid(["Requirement", "Workshop impact", "Evidence / decision"], [
              ["FR-09, FR-10, FR-18", "Profit recognition, Ibra, early/partial settlement.", "Approved calculations, fixed-profit invariant, schedule, GL and output tests."],
              ["FR-11, FR-12, FR-13", "Subledger, ECL/staging, daily reconciliation.", "Journal matrix, ECL contract, bank/core feed and reconciliation cases."],
              ["FR-16; INT-03 to INT-05", "Commodity-to-sale gate, bank disbursement and payment/core integration.", "Owner/API swimlane, negative gates, callback recovery and end-to-end audit."],
              ["FR-20, FR-22, FR-24", "Murabaha top-up, deferment and write-off.", "New-contract flow, days-based deferment rules and partial write-off decision."],
              ["FR-26 to FR-30", "Delinquency, staging, notifications and collections.", "Risk/action matrix, templates, channels and queue tests."],
          ], [115, 188, 195]),
          sub("How to classify each item"),
          bullet("<b>Current, demonstrated:</b> retain the build/version and screen path, then verify calculations, journals, audit and edge cases."),
          bullet("<b>Proposed enhancement:</b> capture written behavior, estimate, delivery scope and acceptance scenarios."),
          bullet("<b>Policy decision:</b> obtain a named Bede finance, product, risk or Sharia reviewer decision for the exact scenario and version."),
          bullet("<b>Executed result:</b> record steps, data, expected/actual result, evidence and defect; do not copy a design-time PASS label into test status."),
          Spacer(1, 10), tag("The prior Murabaha review found conflicting present-tense FOO claims and BRD enhancement language. Its 71 Section 6 cases and 14 targeted lifecycle/Ibra checks had no executed result in the reviewed plan. This workshop did not close that evidence gap.", ICE), PageBreak()]

# Page 7: decisions
story += section_start("6", "Decision log for the next review", "Priority order")
decisions = [
    ("D1", "Product scope and document baseline", "Confirm Tawarruq versus direct Goods Murabaha, governing version and exclusions.", "B 42:35-43:49; 57:19-64:58"),
    ("D2", "Lifecycle sequence", "Approve purchase, ownership, possession, offer, acceptance, sale, disbursement and receivable event order.", "B 43:49-56:55"),
    ("D3", "System ownership", "Select sale-complete sender and backend/LMS bank-disbursement orchestration with failure recovery.", "B 45:39-53:05"),
    ("D4", "Fixed profit and deferment", "Decide days-based deferral, fees, consent and whether historical added-profit treatment is excluded.", "B 29:43-42:02"),
    ("D5", "Ibra rule", "Set eligible unearned profit, overdue treatment and partial-settlement schedule effect.", "A 30:17-33:51; B 76:51-78:53"),
    ("D6", "Suspense and recovery", "Choose threshold, suspense entries, cooling-off and restart behavior.", "A 18:51-29:32"),
    ("D7", "Partial write-off", "Include in first release or price as a separate enhancement.", "B 04:19-07:15"),
]
story += [grid(["ID", "Decision", "Output required", "Audio"], decisions, [36, 118, 259, 85], pad=6),
          Spacer(1, 10), p("<b>Status of D1-D7:</b> open in the reviewed recording. The suggested reviewers in the source action register are proposals, not assigned owners. Each decision should carry version, date, reviewer, rule example and affected test IDs.", "small"),
          sub("Three practical review sessions"),
          bullet("Product/Sharia: D1, D2, D4, D5 with annotated customer journey and sample contracts.", True),
          bullet("Finance/risk: D4-D7 with approved numerical schedule and journal examples.", True),
          bullet("Integration/QA: D2-D3 with API owners, bank callbacks and end-to-end evidence.", True), PageBreak()]

# Pages 8-9: action register in full
with (WORKSHOP / "reports/03-actions-and-decisions.tsv").open() as f:
    records = list(csv.DictReader(f, delimiter="\t"))
for page_index, selected in enumerate((records[:10], records[10:]), start=1):
    story += section_start("7", "Action and decision tracker" + (" (continued)" if page_index == 2 else ""), "Proposed follow-up, not accepted assignment")
    story += [p("This is a condensed view of the 20-item working register. 'Lead' is suggested for routing; the project leads must confirm ownership, dates and closure evidence. All items remain open as of the recording review.", "small")]
    rows = []
    for rec in selected:
        rows.append((rec["ID"], rec["Topic"], rec["Open point or proposed follow-up"], rec["Suggested lead (unconfirmed)"]))
    story += [grid(["ID", "Topic", "What to resolve or produce", "Suggested lead"], rows, [47, 101, 232, 118], pad=5),
              Spacer(1, 10), p("The full register includes recording timestamps, status language and closure evidence. See the source notes in section 8.", "note"), PageBreak()]

# Page 10: test plan and sources
story += section_start("8", "Evidence plan and delivery gates", "How to close the workshop gaps")
story += [grid(["Gate", "Minimum deliverable", "Result rule"], [
    ["0. Freeze target", "Build/config ID, environment, product variant, requirement/BRD versions and approved finance/Sharia examples.", "No unversioned 'supported' claim."],
    ["1. Lifecycle", "Negative sale/disbursement attempts at each missing evidence gate; one positive sale-to-bank-to-LMS chain.", "Capture state, API/UI response, receivable and audit."],
    ["2. Financial", "Ibra, fixed-profit deferment, suspense, charity, legal cost, write-off and reconciliation scenarios.", "Expected/actual schedule and GL; approved tolerances."],
    ["3. Operations", "Failed callbacks, bank-success/LMS-failure, retries, reconciliation and manual recovery.", "Independent bank/core source and exception closure."],
    ["4. Sign-off", "Completed test register, defect dispositions, scope exceptions and reviewer decisions.", "Pass only after observed output matches agreed rule."],
], [87, 272, 139], pad=6),
          sub("Source and method notes"),
          p("<b>Primary source:</b> Workshop1-a.m4a (33:52.6) and Workshop1-b.m4a (83:28.6), preserved byte-for-byte in <font color='#2459A8'>meetings/2026-10-14/workshop-1/recordings/</font>. A and B timestamps throughout this report refer to elapsed recording time. Embedded creation timestamps imply 14 October 2026 in Beirut and about a one-minute gap; they do not verify the exact meeting schedule or attendance.", "small"),
          p("<b>Working text:</b> local MacWhisper large-v3-turbo segment transcripts in <font color='#2459A8'>meetings/2026-10-14/workshop-1/supporting/</font>. These aid search but have no verified speaker labels and may mishear domain terms. The audio remains authoritative. Draft minutes, the full action register, and the scope crosswalk are in the workshop reports folder.", "small"),
          p("<b>Written context:</b> Bede-Foo LMS Scope and Requirements; Murabaha lifecycle and Ibra BRDs; prior capability reconciliation and test execution plan in <font color='#2459A8'>planning/sharia-murabaha-2026-10-07/</font>. Their claims are distinguished from this workshop's speech and from executed test evidence.", "small"),
          tag("Share as a discussion record. Before using it as a baseline, participants should correct any transcription or attribution error, confirm the document versions, and record formal scope, finance and Sharia decisions.", ICE)]

doc.build(story)
print(OUTPUT)
