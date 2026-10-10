from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from pypdf import PdfReader
root=Path(__file__).resolve().parents[1]
out=root/'docs/assets/Huihui-Li-CV.pdf'
navy=HexColor('#043361'); gray=HexColor('#444444')
styles={
 'name':ParagraphStyle('name',fontName='Helvetica',fontSize=23,leading=29,textColor=navy,spaceAfter=7),
 'body':ParagraphStyle('body',fontName='Helvetica',fontSize=10,leading=14,textColor=gray,spaceAfter=5),
 'small':ParagraphStyle('small',fontName='Helvetica',fontSize=9,leading=13,textColor=gray,spaceAfter=5),
 'heading':ParagraphStyle('heading',fontName='Helvetica-Bold',fontSize=11,leading=15,textColor=navy,spaceBefore=16,spaceAfter=7),
 'paper':ParagraphStyle('paper',fontName='Helvetica',fontSize=9.5,leading=13.3,textColor=gray,spaceAfter=11)
}
story=[]
def add(text,style='body'):story.append(Paragraph(text,styles[style]))
add('Huihui Li','name')
add('Ph.D. Student | Evomics Lab<br/>Sun Yat-sen University Cancer Center, Guangzhou, China')
add('<link href="mailto:hhui.li@outlook.com" color="#1679a8">hhui.li@outlook.com</link> | <link href="https://github.com/hhuili" color="#1679a8">GitHub</link> | <link href="https://scholar.google.com/citations?user=L3DqZPoAAAAJ&amp;hl=zh-CN" color="#1679a8">Google Scholar</link> | <link href="https://www.researchgate.net/profile/Huihui-Li-6" color="#1679a8">ResearchGate</link>','small')
add('Education','heading')
add('<b>2023-present</b> &nbsp; Ph.D. studies, Sun Yat-sen University')
add('<b>Master\'s degree</b> &nbsp; Sun Yat-sen University')
add('<b>Bachelor\'s degree</b> &nbsp; Guizhou University')
add('Research interests','heading')
add('Telomere length variation, variant repeats, and DNA methylation; viral pangenomics and papillomavirus evolution; bioinformatics methods for long-read sequencing.')
add('Selected publications','heading')
add('First- and co-first-author work. Preprints are indicated explicitly.','small')
papers=[
 ('<b>Huihui Li</b>, Congying Chen, Ludong Yang, et al.','Multidimensional telomere diversity and inheritance at individual and population scales.','bioRxiv, 2026. Preprint.','10.64898/2026.08.19.745664'),
 ('<b>Huihui Li</b>, Jingtao Chen, Xinxin Zhang, et al.','Super-pangenome analysis of 3562 human and animal papillomavirus isolates illuminates their genome and pathogenicity evolution.','bioRxiv, 2025. Preprint.','10.1101/2025.07.20.664904'),
 ('<b>Huihui Li</b>, Mingzhe Xie, Yan Wang, Ludong Yang, Zhi Xie, Hongwei Wang.','riboCIRC: a comprehensive database of translatable circRNAs.','Genome Biology, 2021, 22:79.','10.1186/s13059-021-02300-7')]
for authors,title,venue,doi in papers:
 add(f'{authors}<br/>{title} <i>{venue}</i><br/><link href="https://doi.org/{doi}" color="#1679a8">doi:{doi}</link>','paper')
add('Open-source software','heading')
add('<b>TeloXplorer</b> - chromosome-end-resolved telomere analysis for long-read sequencing data. Profiles telomere length, variant repeats, and DNA methylation.')
add('<link href="https://github.com/hhuili/TeloXplorer" color="#1679a8">github.com/hhuili/TeloXplorer</link>','small')
def footer(c,doc):
 c.setFont('Helvetica',8);c.setFillColor(HexColor('#777777'));c.drawString(50,28,'Huihui Li | Curriculum vitae');c.drawRightString(545,28,'Updated 10 October 2026')
SimpleDocTemplate(str(out),pagesize=(595.28,841.89),leftMargin=50,rightMargin=50,topMargin=42,bottomMargin=44,title='Huihui Li - Curriculum Vitae',author='Huihui Li').build(story,onFirstPage=footer,onLaterPages=footer)
r=PdfReader(out);assert len(r.pages)==1,len(r.pages)
text='\n'.join(p.extract_text() for p in r.pages)
assert 'translational regulation' not in text and 'Nucleic Acids' not in text and 'National Academy' not in text
print('Created one-page CV; selectable text and content checks passed')
