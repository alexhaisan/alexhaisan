from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_LINE_SPACING, WD_ALIGN_PARAGRAPH

C = {
 'decision':('Decision: ','In autumn 2026 I withdrew from final-round interviews at Marshall Wace, a fund accountant role worth £120,000 against £38,000 at PwC.'),
 'action':('Action: ','Accept, losing my placement, degree and ACA; or decline. A third existed: ask Marshall Wace to hold the role eight months. I never raised it, on the phone to them.'),
 'prefs':['Financial security','The ACA','Worthwhile work','A career not narrowed at twenty-one'],
 'ev':['Pay: headline only, £120,000 against £38,000.',
       'Tax: the real gap is £37,898; the £40,000 bonus is worth £15,600.',
       'Hours: sixty against forty; 3.2 times becomes 1.5 net hourly.',
       'Qualification: the ACA travels, the role is niche.',
       'Search: twenty minutes of arithmetic, not done.'],
 'fig1':'Figure 1: the gap I believed in against the gap that exists.',
 'expect':('Expectations: ','I expected an £80,000 advantage and sixty-hour weeks. The second was right, the first wrong by half. I never tested whether they would wait.'),
 'table':[['Preference','Marshall Wace','PwC'],
          ['Security','+£37,898 net','certain'],
          ['ACA','only likely','yes'],
          ['Worthwhile work','yes','no'],
          ['Career open','niche','portable']],
 'pred':('IRC Prediction: ','A rational agent with my preferences weighs £37,898 net against a portable qualification and twenty extra hours, and declines. But only after testing the deferral.'),
 'dev_h':'Why my decision deviated:',
 'dev_intro':'I withdrew. The outcome was probably right, the reasoning was not. Elster (2007, p. 191) asks that an action follow from the beliefs that justify it: doing right by accident is not reasoning well.',
 'dev':['Evidence to expectations: the search stopped at the headline, so my figure was wrong by £44,102.',
        'Expectations to action: that figure argued for accepting. I withdrew anyway.',
        'Outside the model: what moved me was tuition already paid, spent either way.',
        "The model's limit: it asks for the right amount of searching without saying what that is (Hargreaves Heap, 1992)."],
 'fig3':'Figure 3: my decision mapped onto the model.',
 'fig2':'Figure 2: my preferences against both options.',
}

def wc():
    n = 0
    n += len((C['decision'][0]+C['decision'][1]).split())
    n += len((C['action'][0]+C['action'][1]).split())
    n += len('Preferences:'.split()) + sum(len(x.split()) for x in C['prefs'])
    n += len('Evidence:'.split()) + sum(len(x.split()) for x in C['ev'])
    n += len(C['fig1'].split())
    n += len((C['expect'][0]+C['expect'][1]).split())
    n += len(C['fig2'].split())
    n += len((C['pred'][0]+C['pred'][1]).split())
    n += len(C['dev_h'].split()) + len(C['dev_intro'].split()) + sum(len(x.split()) for x in C['dev'])
    n += len(C['fig3'].split())
    return n
TOTAL = wc()

d = Document()
st = d.styles['Normal']
st.font.name = 'Verdana'; st.font.size = Pt(11)
st.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
st.paragraph_format.space_after = Pt(6)
for s in d.sections:
    s.top_margin = s.bottom_margin = s.left_margin = s.right_margin = Cm(2.5)

def para(label=None, text='', bullet=False, size=11, italic=False, align=None, space_before=0):
    p = d.add_paragraph(style='List Bullet' if bullet else None)
    p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.space_before = Pt(space_before)
    if align: p.alignment = align
    if label:
        r = p.add_run(label); r.bold = True; r.font.name='Verdana'; r.font.size=Pt(size)
    if text:
        r = p.add_run(text); r.italic = italic; r.font.name='Verdana'; r.font.size=Pt(size)
        if italic: r.font.color.rgb = RGBColor(0x59,0x59,0x59)
    return p

hdr = para(text='[your student ID]', size=10, align=WD_ALIGN_PARAGRAPH.RIGHT)
para(text='Instrumental Rational Choice application exercise', size=11, align=WD_ALIGN_PARAGRAPH.RIGHT)
para(text='Word count: %d' % TOTAL, size=10, align=WD_ALIGN_PARAGRAPH.RIGHT)

para(*C['decision'])
para(*C['action'])
para('Preferences:')
for b in C['prefs']: para(text=b, bullet=True)
para('Evidence:')
for b in C['ev']: para(text=b, bullet=True)

d.add_picture('../11-figures/fig1-money.png', width=Cm(15))
d.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
para(text=C['fig1'], size=9, italic=True)

para(*C['expect'])

d.add_picture('../11-figures/fig3-table.png', width=Cm(15))
d.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
para(text=C['fig2'], size=9, italic=True)
para(text='', size=6)

para(*C['pred'])
para(C['dev_h'])
para(text=C['dev_intro'])
for b in C['dev']: para(text=b, bullet=True)

d.add_picture('../11-figures/fig2-model.png', width=Cm(15))
d.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
para(text=C['fig3'], size=9, italic=True)

para('References', space_before=10)
for ref in ['Elster, J. (2007) Explaining Social Behavior: More Nuts and Bolts for the Social Sciences. Cambridge: Cambridge University Press.',
            'Hargreaves Heap, S., Hollis, M., Lyons, B., Sugden, R. and Weale, A. (1992) The Theory of Choice: A Critical Guide. Oxford: Blackwell.']:
    p = para(text=ref, size=10)
    p.paragraph_format.left_indent = Cm(1); p.paragraph_format.first_line_indent = Cm(-1)

d.save('IRC_application_exercise.docx')
print('word count (strictest: headings + bullets + captions):', TOTAL)
print('saved IRC_application_exercise.docx')
