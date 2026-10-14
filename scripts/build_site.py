"""Render two static pages using only the Python standard library."""
from pathlib import Path
import html
import json

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def read(path):
    return (ROOT / path).read_text()


def render(source, values):
    for key, value in values.items():
        source = source.replace("{{" + key + "}}", value)
    return source


def news_html():
    items = json.loads(read("content/news.json"))
    result = '<h2>News</h2>\n<ul class="dated-list news-list">\n'
    for item in items[:4]:
        result += f'<li><strong>{html.escape(item["date"])}</strong> {item["html"]}</li>\n'
    if len(items) > 4:
        result += '<li class="news-toggle"><button type="button" aria-expanded="false" aria-controls="older-news">Show more</button></li>\n</ul>\n<ul class="dated-list news-list" id="older-news" hidden>\n'
        for item in items[4:]:
            result += f'<li><strong>{html.escape(item["date"])}</strong> {item["html"]}</li>\n'
    return result + '</ul>\n'


def publication_item(p):
    esc = lambda text: html.escape(str(text), quote=True)
    image = '../assets/publications/' + p['image']
    badge = '<abbr class="badge" data-venue="' + esc(p['badge']) + '" title="' + ('Preprint' if p['preprint'] else 'Genome Biology') + '">' + esc(p['badge']) + '</abbr>'
    links = ' '.join('<a class="btn" href="' + esc(link['url']) + '" target="_blank" rel="noopener">' + esc(link['label']) + '</a>' for link in p['links'])
    return f'''<li><div class="pub-row">
<div class="col-sm-3 abbr publication-art"><a href="{image}" target="_blank" rel="noopener" aria-label="View full figure: {esc(p['image_alt'])}"><img src="{image}" class="teaser" alt="{esc(p['image_alt'])}"></a>{badge}</div>
<div class="col-sm-9 publication-text"><div class="title"><a href="{esc(p['url'])}">{esc(p['title'])}</a></div>
<div class="author">{p['authors_html']}</div><div class="periodical">{p['venue_html']}</div><div class="links">{links}</div></div>
</div></li>\n'''


def publications_html():
    pubs = json.loads(read('content/publications.json'))
    result = '<h2 class="pub-section-title">Publications <span class="pub-ext-links"><a href="https://scholar.google.com/citations?user=L3DqZPoAAAAJ&amp;hl=zh-CN">Google Scholar</a></span></h2>\n'
    preprints = [p for p in pubs if p['preprint']]
    if preprints:
        result += '<h3 class="pub-subsection">Preprints</h3><div class="publications"><ol class="bibliography">\n'
        result += ''.join(publication_item(p) for p in sorted(preprints, key=lambda p: p['year'], reverse=True))
        result += '</ol></div>\n'
    published = [p for p in pubs if not p['preprint']]
    if published:
        result += '<h3 class="pub-subsection">Published Papers</h3><div class="publications">\n'
        for year in sorted({p['year'] for p in published}, reverse=True):
            result += f'<h2 class="year">{year}</h2><ol class="bibliography">\n'
            result += ''.join(publication_item(p) for p in published if p['year'] == year)
            result += '</ol>\n'
        result += '</div>\n'
    return result + '<p class="publication-note">† Equal contribution.</p>\n'


def build_page(page, body, title, output):
    values = {
        'prefix': './' if page == 'home' else '../',
        'title': title,
        'canonical': 'https://hhuili.github.io/' + ('' if page == 'home' else 'publications/'),
        'home_active': 'active' if page == 'home' else '',
        'publications_active': 'active' if page == 'publications' else '',
        'home_current': 'aria-current="page"' if page == 'home' else '',
        'publications_current': 'aria-current="page"' if page == 'publications' else '',
    }
    values['header'] = render(read('templates/header.html'), values)
    values['hero'] = render(read('templates/hero.html'), values)
    values['body'] = body
    result = render(read('templates/base.html'), values)
    assert '{{' not in result, 'Unresolved template token'
    path = DOCS / output
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(result)


if __name__ == '__main__':
    home = render(read('content/home.html'), {'news': news_html()})
    build_page('home', home, 'Huihui Li | Sun Yat-sen University', 'index.html')
    build_page('publications', publications_html(), 'Publications | Huihui Li', 'publications/index.html')
    print('Rendered Home and Publications.')
