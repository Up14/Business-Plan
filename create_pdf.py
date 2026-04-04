from fpdf import FPDF

class BP(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=25)
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8); self.set_text_color(130,130,130)
            self.cell(0, 10, 'TalentLens - Business Plan', align='R', new_x="LMARGIN", new_y="NEXT")
            self.set_draw_color(0,51,102); self.line(10,17,200,17); self.ln(2)
    def footer(self):
        if self.page_no() > 1:
            self.set_y(-15); self.set_font('Helvetica','I',8); self.set_text_color(130,130,130)
            self.cell(0,10,f'Page {self.page_no()}',align='C')
    def ch(self,t):
        self.set_font('Helvetica','B',16); self.set_text_color(0,51,102)
        self.cell(0,12,t,new_x="LMARGIN",new_y="NEXT")
        self.set_draw_color(0,51,102); self.line(10,self.get_y(),200,self.get_y()); self.ln(6)
    def sec(self,t):
        self.set_font('Helvetica','B',13); self.set_text_color(0,70,130)
        self.cell(0,10,t,new_x="LMARGIN",new_y="NEXT"); self.ln(2)
    def p(self,t):
        self.set_font('Helvetica','',10.5); self.set_text_color(30,30,30)
        self.multi_cell(0,6,t); self.ln(3)
    def b(self,bold,normal=''):
        self.set_font('Helvetica','B',10.5); self.set_text_color(30,30,30); self.write(6,bold)
        if normal: self.set_font('Helvetica','',10.5); self.write(6,normal)
        self.ln(8)
    def bul(self,t):
        self.set_font('Helvetica','',10.5); self.set_text_color(30,30,30)
        self.cell(8,6,'-'); self.multi_cell(0,6,t); self.ln(1)
    def tbl(self,headers,rows,cw=None):
        if cw is None: cw=[180/len(headers)]*len(headers)
        # Header
        self.set_font('Helvetica','B',9); self.set_fill_color(0,51,102); self.set_text_color(255,255,255)
        for i,h in enumerate(headers):
            self.cell(cw[i],8,h,border=1,fill=True,align='C')
        self.ln()
        # Rows
        self.set_font('Helvetica','',9); self.set_text_color(30,30,30)
        alt=False
        for row in rows:
            if alt: self.set_fill_color(235,240,250)
            else: self.set_fill_color(255,255,255)
            for i,v in enumerate(row):
                self.cell(cw[i],8,str(v)[:90],border=1,fill=True)
            self.ln(); alt=not alt
        self.ln(4)
    def bmc_grid(self):
        """Proper 9-block BMC visual grid"""
        w = 36  # each column width
        # Row 1: Headers
        self.set_font('Helvetica','B',7); self.set_fill_color(0,51,102); self.set_text_color(255,255,255)
        for h in ['KEY PARTNERS','KEY ACTIVITIES','VALUE PROP.','CUSTOMER REL.','CUST. SEGMENTS']:
            self.cell(w,7,h,border=1,fill=True,align='C')
        self.ln()
        # Row 1: Content
        self.set_font('Helvetica','',6.5); self.set_text_color(30,30,30); self.set_fill_color(235,240,250)
        r1=['AWS, Razorpay,\nColleges, Incubators','AI interviews,\nScreening, Client mgmt','Verified talent fast,\n60-70% cost saving,\nAI removes bias','Account managers,\nFree pilots,\nWeekly reports','AI labs, Tech startups,\nGlobal companies']
        y_start = self.get_y()
        for i,c in enumerate(r1):
            self.set_xy(10+i*w, y_start)
            self.multi_cell(w, 4, c, border=1, fill=True)
        max_y = self.get_y()
        self.set_y(y_start + 20)

        # Row 2: Headers (KR and CH only)
        self.set_font('Helvetica','B',7); self.set_fill_color(0,51,102); self.set_text_color(255,255,255)
        y2 = self.get_y()
        # Empty
        self.set_fill_color(245,245,245); self.set_text_color(30,30,30)
        self.cell(w,7,'',border=1,fill=True)
        self.set_fill_color(0,51,102); self.set_text_color(255,255,255)
        self.cell(w,7,'KEY RESOURCES',border=1,fill=True,align='C')
        self.set_fill_color(245,245,245)
        self.cell(w,7,'',border=1,fill=True)
        self.set_fill_color(0,51,102); self.set_text_color(255,255,255)
        self.cell(w,7,'CHANNELS',border=1,fill=True,align='C')
        self.set_fill_color(245,245,245)
        self.cell(w,7,'',border=1,fill=True)
        self.ln()

        # Row 2: Content
        self.set_font('Helvetica','',6.5); self.set_text_color(30,30,30); self.set_fill_color(235,240,250)
        y2c = self.get_y()
        self.set_fill_color(245,245,245)
        self.cell(w,16,'',border=1,fill=True)
        self.set_fill_color(235,240,250)
        self.cell(w,16,'AI engine, Talent DB, Team, AWS',border=1,fill=True)
        self.set_fill_color(245,245,245)
        self.cell(w,16,'',border=1,fill=True)
        self.set_fill_color(235,240,250)
        self.cell(w,16,'LinkedIn, Conferences, Campus, Referrals',border=1,fill=True)
        self.set_fill_color(245,245,245)
        self.cell(w,16,'',border=1,fill=True)
        self.ln()

        # Row 3: Cost Structure + Revenue Streams
        self.set_font('Helvetica','B',7); self.set_fill_color(0,51,102); self.set_text_color(255,255,255)
        self.cell(90,7,'COST STRUCTURE',border=1,fill=True,align='C')
        self.cell(90,7,'REVENUE STREAMS',border=1,fill=True,align='C')
        self.ln()
        self.set_font('Helvetica','',6.5); self.set_text_color(30,30,30); self.set_fill_color(235,240,250)
        self.cell(90,12,'Salaries, Cloud hosting, Marketing, Office, Legal, Payment processing',border=1,fill=True)
        self.cell(90,12,'30-35% hourly commission | Data Services fees | Interview SaaS (Y2)',border=1,fill=True)
        self.ln(16)


pdf = BP()
pdf.set_margins(15,15,15)

# COVER
pdf.add_page(); pdf.ln(55)
pdf.set_font('Helvetica','B',32); pdf.set_text_color(0,51,102)
pdf.cell(0,15,'BUSINESS PLAN',align='C',new_x="LMARGIN",new_y="NEXT"); pdf.ln(5)
pdf.set_font('Helvetica','B',24)
pdf.cell(0,12,'TalentLens',align='C',new_x="LMARGIN",new_y="NEXT"); pdf.ln(3)
pdf.set_font('Helvetica','',14); pdf.set_text_color(100,100,100)
pdf.cell(0,10,'AI-Powered Talent and Data Services Platform',align='C',new_x="LMARGIN",new_y="NEXT"); pdf.ln(20)
for d in ['Prepared by: [Your Name]','Roll Number: [Your Roll Number]','College: [Your College Name]','Course: Entrepreneurship Essentials','Date: April 2026']:
    pdf.set_font('Helvetica','',12); pdf.set_text_color(80,80,80)
    pdf.cell(0,8,d,align='C',new_x="LMARGIN",new_y="NEXT")

# TOC
pdf.add_page(); pdf.ch('Table of Contents')
for item in ['Chapter 1: Executive Summary','Chapter 2: The Business','Chapter 3: Market Demand','Chapter 4: Competition','Chapter 5: Strategy','Chapter 6: Resources','Chapter 7: Financial Outlay, Financial Closer, and Projected Financials','Chapter 8: Risks, Opportunities, Rewards and Sensitivities','References']:
    pdf.set_font('Helvetica','',11); pdf.set_text_color(30,30,30)
    pdf.cell(8,8,'-'); pdf.cell(0,8,item,new_x="LMARGIN",new_y="NEXT")

# CH1
pdf.add_page(); pdf.ch('Chapter 1: Executive Summary')
pdf.p('The hiring industry, both in India and globally, is going through a period of significant change. Companies are finding it harder and more expensive to hire skilled professionals. At the same time, millions of talented Indians are unable to access quality work opportunities because the systems that connect talent with employers are outdated, biased, and inefficient.')
pdf.p('TalentLens is a technology platform that solves this from both sides. We use AI-powered video interviews to assess candidates objectively, and connect them to companies that need their skills. The platform has three business lines: AI interviews and assessment, a talent marketplace, and managed AI data services for companies that need domain experts for data labeling and model evaluation.')
pdf.p('Revenue comes from a 30-35% commission on every hour a contractor works. Initial investment: Rs 18 lakhs. Break-even at ~30 contractors (Month 4). Year 1 target: 500 contractors, 15-20 clients, ~Rs 1.15 Cr net revenue. India is the ideal base: $14.3B AI market, 12M+ gig workers, 60-70% cost advantage over Western markets.')

# CH2
pdf.add_page(); pdf.ch('Chapter 2: The Business')
pdf.sec('2.1 Company Overview')
pdf.tbl(['Detail','Description'],
    [['Company Name','TalentLens Technologies Pvt Ltd'],['Legal Structure','Private Limited Company'],
     ['Office','[City, State]'],['Industry','HR Tech / AI Services'],['Year','2026']],cw=[50,130])

pdf.sec('2.2 Vision and Mission')
pdf.b('Vision: ','To become the most trusted bridge between India\'s skilled workforce and the world\'s leading technology companies.')
pdf.b('Mission: ','To use AI to evaluate talent fairly, connect professionals with meaningful work, and help companies build teams faster than traditional hiring.')

pdf.sec('2.3 The Problem')
pdf.b('For Companies:')
pdf.p('Hiring takes 45-60 days for technical roles. Agencies charge 15-25% of annual salary. Resumes are unreliable. AI companies specifically need thousands of domain experts (doctors, lawyers, coders) for data labeling and model evaluation at scale - a massive operational challenge.')
pdf.b('For Professionals:')
pdf.p('Talented people in tier-2/3 cities lack networks for global opportunities. Traditional hiring filters by college name, not skill. Freelancers face payment delays and disputes. No structured way to enter the high-paying AI data economy despite having the exact expertise AI companies need.')

pdf.sec('2.4 Our Solution')
pdf.b('Line 1 - AI Interview: ','20-min video interview. Scores: Technical (40%), Communication (20%), Problem-solving (25%), Professionalism (15%). TalentLens Score out of 100.')
pdf.b('Line 2 - Talent Marketplace: ','Verified candidates join talent pool. Companies search, hire, and manage contractors through us. We handle contracts, tracking, and payments.')
pdf.b('Line 3 - AI Data Services: ','Managed teams of domain experts for data labeling, model evaluation, rubric creation, and quality review for AI companies.')

pdf.sec('2.5 Revenue Model')
pdf.tbl(['Component','Example'],
    [['Contractor base rate','Rs 600/hour'],['Company pays us','Rs 790-810/hour'],['Our revenue/hour','Rs 190-210']],cw=[70,110])

pdf.sec('2.6 Business Model Canvas')
pdf.bmc_grid()

# CH3
pdf.add_page(); pdf.ch('Chapter 3: Market Demand')
pdf.sec('3.1 Industry Trends')
pdf.b('Trend 1 - AI needs humans: ','Better AI needs higher quality human training data. India AI market: $14.3B in 2026. Growing 25%+ per year.')
pdf.b('Trend 2 - Gig economy exploding: ','12M+ gig workers in 2025, projected 23.5M by 2030, 21% CAGR - fastest globally. 15M+ freelancers active.')
pdf.b('Trend 3 - Talent shortage paradox: ','82% of employers report difficulty filling roles (CXO Today, 2026). Not lack of talent - failure of matching systems.')

pdf.sec('3.2 Target Customers')
pdf.tbl(['Segment','Description','Need'],
    [['AI/ML Companies','Building LLMs, vision, AI products','Domain experts for labeling and evaluation'],
     ['Tech Startups','Need contract engineers/designers','Flexible 2-12 month hiring'],
     ['Global Companies','US/Europe/ME seeking Indian talent','60-70% cost saving']],cw=[40,60,80])

pdf.sec('3.3 Market Size')
pdf.p('India: ~1.25M AI professionals by 2027, 16% of global AI talent. Even 0.04% capture (500 contractors) generates meaningful revenue. Global AI data services: several billion dollars TAM.')

# CH4
pdf.add_page(); pdf.ch('Chapter 4: Competition')
pdf.sec('4.1 Competitors')
pdf.tbl(['Competitor','Strengths','Weaknesses'],
    [['Upwork/Fiverr','Huge user base','No verification, price race'],
     ['Toptal','High quality','Expensive, slow, rejects 97%'],
     ['Scale AI','Major AI clients','Low-skill workers'],
     ['Appen','Global workforce','Quality issues, financial trouble'],
     ['Agencies','Deep relationships','Slow (45-60 days), 15-25% fees']],cw=[40,60,80])

pdf.sec('4.2 Our Position')
pdf.p('Gap between cheap-but-unreliable (Upwork) and elite-but-expensive (Toptal). We combine: AI assessment + managed marketplace + specialized AI data services with domain experts.')

pdf.sec('4.3 SWOT Analysis')
# SWOT as styled 2x2 grid
pdf.set_font('Helvetica','B',8)
pdf.set_fill_color(0,51,102); pdf.set_text_color(255,255,255)
pdf.cell(30,7,'',border=1,fill=True); pdf.cell(75,7,'HELPFUL',border=1,fill=True,align='C'); pdf.cell(75,7,'HARMFUL',border=1,fill=True,align='C'); pdf.ln()

pdf.set_fill_color(0,51,102); pdf.set_text_color(255,255,255)
pdf.cell(30,24,'INTERNAL',border=1,fill=True,align='C')
pdf.set_font('Helvetica','',7.5); pdf.set_text_color(30,30,30)
pdf.set_fill_color(232,245,233)
pdf.cell(75,24,'STRENGTHS: AI screening, Indian\ntalent focus, 3 revenue lines, low costs',border=1,fill=True)
pdf.set_fill_color(255,235,238)
pdf.cell(75,24,'WEAKNESSES: New brand, AI still\ndeveloping, small team, limited capital',border=1,fill=True)
pdf.ln()

pdf.set_font('Helvetica','B',8)
pdf.set_fill_color(0,51,102); pdf.set_text_color(255,255,255)
pdf.cell(30,24,'EXTERNAL',border=1,fill=True,align='C')
pdf.set_font('Helvetica','',7.5); pdf.set_text_color(30,30,30)
pdf.set_fill_color(227,242,253)
pdf.cell(75,24,'OPPORTUNITIES: AI boom, 21% gig\ngrowth, interview SaaS, govt support',border=1,fill=True)
pdf.set_fill_color(255,243,224)
pdf.cell(75,24,'THREATS: Big platforms, slowdowns,\nregulation, AI reducing labeling need',border=1,fill=True)
pdf.ln(8)

# CH5
pdf.add_page(); pdf.ch('Chapter 5: Strategy')
pdf.sec('5.1 Go-To-Market')
pdf.b('Demand Side:')
pdf.tbl(['Phase','Timeline','Activities'],
    [['Direct Outreach','Month 1-3','200-300 CTOs via LinkedIn/email. Free pilot.'],
     ['Content + Partners','Month 3-6','Case studies, LinkedIn articles, university AI labs.'],
     ['Inbound + Events','Month 6-12','Conferences, testimonials driving inbound.']],cw=[40,30,110])
pdf.b('Supply Side:')
pdf.bul('Campus drives (AI interview as free career assessment)')
pdf.bul('Instagram/LinkedIn ads for tech professionals')
pdf.bul('WhatsApp/Telegram domain communities')
pdf.bul('Rs 2,000 referral bonus per hire')

pdf.sec('5.2 Pricing')
pdf.tbl(['Service','Model','Range'],
    [['Marketplace','30-35% markup','Rs 700 base = Rs 910-945 to client'],
     ['Data (Basic)','Per hour/worker','Rs 300-500/hour'],
     ['Data (Expert)','Per hour/expert','Rs 800-2,000/hour'],
     ['Interview SaaS','Per interview (Y2)','Rs 200-500']],cw=[45,45,90])

pdf.sec('5.3 Growth')
pdf.b('Year 1: ','500 contractors, 15-20 clients, break-even Month 4-5')
pdf.b('Year 2: ','2,000 contractors, new domains, interview tool as product')
pdf.b('Year 3: ','Series A, 50+ team, 10,000 contractors, US/Europe')

pdf.sec('5.4 Quality Control')
pdf.bul('AI scores calibrated against human expert evaluations')
pdf.bul('Client rates every contractor; below 3.0/5 = removed')
pdf.bul('10-15% audit on data labeling; max 5% error rate')

# CH6
pdf.add_page(); pdf.ch('Chapter 6: Resources')
pdf.sec('6.1 Team')
pdf.tbl(['Role','Count','Monthly (Rs)'],
    [['Full-stack Developer','1','60,000'],['Sales/BD','1','35,000'],
     ['Talent Ops','1','25,000'],['Data PM','1','40,000'],
     ['Marketing','1','20,000'],['Total','5','1,80,000']],cw=[70,30,80])
pdf.sec('6.2 Technology')
pdf.tbl(['Resource','Cost/Month (Rs)'],
    [['AWS Cloud','50,000'],['AI/NLP APIs','20,000'],['Payments','30,000'],
     ['Comm tools','5,000'],['Analytics','5,000']],cw=[100,80])
pdf.sec('6.3 Other')
pdf.bul('Co-working in [City]: Rs 40,000/month')
pdf.bul('Advisory board: recruitment, AI/tech, finance experts')
pdf.bul('Partnerships: colleges, NASSCOM/T-Hub, AWS Activate')
pdf.bul('IP: AI scoring algorithm, talent DB, QA workflow')

# CH7
pdf.add_page(); pdf.ch('Chapter 7: Financial Outlay, Closer, and Projections')
pdf.p('Note: All figures are estimates based on stated assumptions.')
pdf.sec('7.1 Startup Costs')
pdf.tbl(['Item','Amount (Rs)'],
    [['Registration/legal','50,000'],['Platform MVP','3,00,000'],['AI engine','2,00,000'],
     ['Office setup','80,000'],['Marketing launch','1,50,000'],['Working capital','10,00,000'],
     ['Misc','20,000'],['Total','18,00,000']],cw=[110,70])

pdf.sec('7.2 Funding')
pdf.tbl(['Source','Amount (Rs)','Type'],
    [['Founders','5,00,000','Equity'],['Family/friends','5,00,000','Convertible/equity'],
     ['Angel/incubator','8,00,000','Equity (10-15%)'],['Total','18,00,000','']],cw=[55,55,70])

pdf.sec('7.3 Revenue (Year 1)')
pdf.p('Assumptions: Rs 192 markup/contractor/hour, 80 hrs/month avg.')
pdf.tbl(['Month','Contractors','Gross Billing','Our Revenue'],
    [['M1-2','0','0','0 (setup)'],['M3','20','12,67,200','3,07,200'],
     ['M6','100','63,36,000','15,36,000'],['M9','270','1,71,07,200','41,47,200'],
     ['M12','500','3,16,80,000','76,80,000'],['Year 1','-','~Rs 13.4 Cr','~Rs 3.25 Cr']],cw=[25,35,60,60])

pdf.sec('7.4 Expenses (at 200 contractors)')
pdf.tbl(['Category','Amount (Rs)'],
    [['Salaries','1,80,000'],['Office','40,000'],['Cloud','50,000'],['Marketing','1,00,000'],
     ['Payments','30,000'],['Legal','20,000'],['Tools+misc','30,000'],['Total','4,50,000']],cw=[110,70])

pdf.sec('7.5 P&L (Year 1)')
pdf.tbl(['Item','Amount (Rs)'],
    [['Revenue','~3,25,00,000'],['Expenses','~54,00,000'],['Profit before tax','~2,71,00,000'],
     ['Tax (25%)','~67,75,000'],['Net profit','~2,03,25,000']],cw=[110,70])

pdf.sec('7.6 Break-Even')
pdf.p('Fixed costs: Rs 4,50,000/month. Revenue/contractor: Rs 15,360/month. Break-even: ~30 contractors (Month 4). Investment recovery: Month 7-8.')

pdf.sec('7.7 Key Ratios')
pdf.tbl(['Metric','Value'],
    [['Gross Margin','32%'],['Net Margin','~15%'],['CAC','Rs 25-40K/client'],
     ['LTV','Rs 5L+ (12 months)'],['LTV:CAC','12:1 to 20:1'],['Payback','7-8 months']],cw=[90,90])

# CH8
pdf.add_page(); pdf.ch('Chapter 8: Risks, Opportunities, Rewards and Sensitivities')
pdf.sec('8.1 Risks')
pdf.tbl(['Risk','Mitigation'],
    [['AI accuracy early on','Hybrid: AI + human review. Improve with feedback.'],
     ['Slow client acquisition','Free pilots, start with startups, build case studies.'],
     ['Talent supply','Campus drives, social media, referrals, communities.'],
     ['Cash flow gaps','Advance deposits, 6-month reserve, net-15 terms.'],
     ['Large platform competition','Specialize in AI data niche. High switching costs.'],
     ['Regulatory changes','Legal advisor day 1. Flexible contracts. Budget for compliance.']],cw=[55,125])

pdf.sec('8.2 Opportunities')
pdf.bul('AI boom: growing need for human labeling for years')
pdf.bul('India: 56.35% employability, 16% global AI talent')
pdf.bul('Interview tool as standalone SaaS in Year 2')
pdf.bul('Startup India tax benefits and incubation')
pdf.bul('Data network effects compound over time')

pdf.sec('8.3 Rewards')
pdf.b('Founders: ','Scalable business, significant valuation potential in 3 years.')
pdf.b('Contractors: ','Higher pay, structured work. Experts earn Rs 1,500-2,000/hr.')
pdf.b('Clients: ','Verified talent in days, not months. Lower cost.')
pdf.b('Economy: ','Formal channel for Indian talent in global AI economy.')

pdf.sec('8.4 Sensitivity')
pdf.tbl(['Scenario','Change','Impact'],
    [['Conservative','300 contractors','Rev ~Rs 1.9 Cr. Still profitable.'],
     ['Aggressive','800 contractors','Rev ~Rs 5.2 Cr. Much higher profit.'],
     ['Pricing drop','22% markup','Rev -30%. Break-even at 43. Viable.'],
     ['Client loss','Top client exits','Target 15-20 clients to limit risk.']],cw=[35,45,100])

# REFERENCES
pdf.add_page(); pdf.ch('References')
for i,ref in enumerate(['Market Research Future (2026). India AI Recruitment Market. MRFR.','CXO Today (2026). Talent Shortages 82% in India. CXO Today.','India Skills Report (2026). 56.35% Employability. Wheebox/CII.','Naukri JobSpeak (2026). IT Hiring 12% YoY Growth. Info Edge.','DemandSage (2026). Gig Economy Statistics 2026.','VynZ Research (2025). India AI Market Size Report.','Down to Earth (2026). Economic Survey: Gig Economy. CSE.','Adecco India (2026). 12-15% Tech Hiring Growth.','HireRight (2024). Global Background Screening Report.','NASSCOM (2025). Indian Tech Sector Strategic Review.','CII/Wheebox (2026). India Skills Report 2026.','Ken Research (2025). India Staffing Market Forecast to 2030.'],1):
    pdf.set_font('Helvetica','',10); pdf.set_text_color(30,30,30)
    pdf.multi_cell(0,6,f'{i}. {ref}'); pdf.ln(2)

pdf.output('/home/raethteam/upanshu/b/Business_Plan_TalentLens.pdf')
print('PDF saved.')
