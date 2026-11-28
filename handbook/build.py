import re, html, json, sys, markdown, os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/'
OUT = sys.argv[1]
GROUPS = [
 ("Start here", [
  ("brief", "00_project/brief-and-topic-review.md", "The brief and the topic review", "What she proposed, what the reviewers said, and what to change"),
  ("roadmap", "02_roadmap/review-roadmap.md", "Review roadmap", "Every review from topic to final jury, with deliverables"),
  ("checklists", "02_roadmap/review-checklists.md", "Review checklists", "Tick-lists and likely questions for each review"),
  ("norms", "01_research/thesis-norms-sathyabama-and-india.md", "What the college expects", "Sathyabama courses, thesis norms, questions for the guide"),
 ]),
 ("Site", [
  ("site", "01_research/site/kodaikanal-site-and-context.md", "Kodaikanal site and the observatory", "KSO history, climate, height rules, access"),
 ]),
 ("Design", [
  ("lighting", "01_research/design/lighting-and-darkness.md", "Lighting and darkness", "The light ladder, eye adaptation and lux targets"),
  ("zoning", "01_research/design/zoning-programme-and-circulation.md", "Zoning, programme and circulation", "Area table, zones, circulation rules"),
  ("rooms", "01_research/design/room-by-room-guide.md", "Room-by-room design guide", "Each space: purpose, light, feel, exhibits, drawings"),
  ("exhibits", "01_research/design/exhibits-and-interactivity.md", "Exhibits and interactivity", "Exhibit ideas by zone and furniture sizes"),
  ("dome", "01_research/design/dome-theatre.md", "Dome theatre", "Dome size, seats, tilt, projection, drawings"),
  ("materials", "01_research/design/materials-and-finishes.md", "Materials and finishes", "Palette by zone, humidity and fire choices"),
  ("services", "01_research/design/services-hvac-acoustics-fire.md", "Services and innovation", "Lighting control, fire, HVAC, acoustics, dark sky"),
  ("codes", "01_research/standards/codes-and-accessibility.md", "Codes and accessibility", "NBC 2016 and the Harmonised Guidelines in numbers"),
 ]),
 ("Science", [
  ("astronomy", "01_research/astronomy-primer.md", "Astronomy primer", "The science behind each gallery, ready for labels"),
  ("glossary", "00_project/glossary.md", "Glossary", "Astronomy, lighting, dome and code terms explained"),
 ]),
 ("Case studies", [
  ("cases", "01_research/case-studies/case-studies.md", "Case studies", "Shanghai, Rose Center, Greenwich, Birla, Pilikula and more"),
  ("template", "05_templates/case-study-template.md", "Case-study template", "The headings to fill in for every case"),
 ]),
 ("Making the work", [
  ("software", "04_workflows/software-workflow.md", "Software workflow", "AutoCAD to SketchUp to renders to sheets"),
  ("sheets", "04_workflows/presentation-sheets-and-ppt.md", "Sheets and PPTs", "Layout, hierarchy and the final sheet set"),
  ("models", "04_workflows/physical-models.md", "Physical models", "Which models, materials, lighting, budget"),
  ("skills", "03_skills/skills-checklist.md", "Skills checklist", "What to learn, from research to models"),
  ("report", "00_project/report-outline.md", "Report outline", "Chapter-by-chapter plan for the written report"),
  ("viva", "00_project/viva-questions.md", "Viva questions", "Likely jury questions with answer outlines"),
 ]),
 ("Sources", [
  ("sources", "sources/SOURCES.md", "All sources", "Every link used, with confidence tags, and gaps"),
 ]),
]
path2id = {p: i for g, ts in GROUPS for (i, p, *_ ) in ts}
path2id['02_roadmap/review-log.md'] = 'roadmap'
def slug(s):
    s = re.sub(r'<[^>]+>', '', s); s = html.unescape(s).lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:50] or 'section'
def find_id(target):
    t = target.split('#')[0].lstrip('./')
    for p, i in path2id.items():
        if t == p or p.endswith('/' + t) or p.endswith(t) or os.path.basename(p) == os.path.basename(t):
            return i
    return None
def linkify(h):
    def a(m):
        href = m.group(1)
        if href.endswith('.md') or '.md#' in href:
            i = find_id(href)
            if i: return f'<a href="#{i}" data-topic-link'
        if href.startswith('http'):
            return f'<a href="{href}" target="_blank" rel="noopener"'
        return m.group(0)
    h = re.sub(r'<a href="([^"]+)"', a, h)
    def c(m):
        t = m.group(1)
        if re.search(r'\.md$', t) or t.rstrip('/').endswith(('01_research/standards','04_workflows')):
            i = find_id(t) if t.endswith('.md') else ('codes' if 'standards' in t else 'software')
            if i:
                title = TITLES[i]
                return f'<a href="#{i}" data-topic-link>{html.escape(title)}</a>'
        return m.group(0)
    h = re.sub(r'<code>([^<]+)</code>', c, h)
    return h
TITLES = {i: t for g, ts in GROUPS for (i, p, t, d) in ts}
def tagify(h):
    # confidence tags like (K) (A) (A/B) -> badges
    return re.sub(r'\((A/B|A|B|C|K)\)', lambda m: f'<span class="ctag ctag-{m.group(1)[0]}" title="{ {"A":"Official or primary source","B":"Reputable secondary source","C":"Aggregator source","K":"General knowledge: verify before using"}[m.group(1)[0]] }">{m.group(1)}</span>', h)
articles = []; nav = []; order = []
for g, ts in GROUPS:
    nav.append((g, [(i, t) for (i, p, t, d) in ts]))
    for (i, p, t, d) in ts:
        src = open(R + p, encoding='utf-8').read()
        if i == 'roadmap':
            src += '\n\n' + re.sub(r'^# ', '## ', open(R + '02_roadmap/review-log.md').read(), flags=re.M).replace('\n## Review 0', '\n### Review 0')
        src = re.sub(r'^# .*\n', '', src, count=1)
        src = re.sub(r'\n- \[ \] ', '\n- ☐ ', src)
        lines = src.split('\n'); fixed = []
        kind = lambda l: 'li' if re.match(r'\s*([-*]|\d+\.) ', l) else ('tb' if l.startswith('|') else ('blank' if not l.strip() else 'p'))
        for ln in lines:
            if fixed and kind(ln) in ('li','tb') and kind(fixed[-1]) not in (kind(ln), 'blank') and not (kind(ln)=='li' and fixed[-1].startswith('  ')):
                fixed.append('')
            fixed.append(ln)
        src = '\n'.join(fixed)
        md = markdown.markdown(src, extensions=['tables', 'fenced_code', 'sane_lists'])
        md = linkify(md); md = tagify(md)
        md = re.sub(r'<table>', '<div class="tw"><table>', md); md = md.replace('</table>', '</table></div>')
        parts = re.split(r'(?=<h2>)', md)
        body = ''
        used = set()
        for k, part in enumerate(parts):
            m = re.match(r'<h2>(.*?)</h2>', part, re.S)
            if m:
                s = slug(m.group(1)); 
                while s in used: s += '-2'
                used.add(s)
                rest = part[m.end():]
                body += (f'<section class="sec" id="{i}--{s}"><div class="sh"><h2>{m.group(1)}</h2>'
                         f'<button class="copy" type="button" data-copy="{i}--{s}" aria-label="Copy this section">Copy</button></div>{rest}</section>')
            elif part.strip():
                body += f'<section class="sec intro" id="{i}--intro">{part}</section>'
        toc = ''.join(f'<li><a href="#{i}--{slug(h)}" data-sec>{re.sub("<[^>]+>","",h)}</a></li>' for h in re.findall(r'<h2>(.*?)</h2>', md, re.S))
        articles.append(f'<article class="topic" id="{i}" data-title="{html.escape(t)}" hidden><p class="kicker">{html.escape(g)}</p><h1>{html.escape(t)}</h1><p class="dek">{html.escape(d)}</p>'
            f'<div class="tbar"><button class="copy big" type="button" data-copy="{i}" aria-label="Copy this whole topic">Copy whole topic</button></div>'
            + (f'<nav class="toc" aria-label="On this page"><p>On this page</p><ul>{toc}</ul></nav>' if toc else '') +
            f'<div class="content">{body}</div><nav class="pn" aria-label="Previous and next topic"></nav></article>')
        order.append((i, t, d, g))
tpl = open(os.path.join(os.path.dirname(__file__), 'template.html'), encoding='utf-8').read()
navhtml = ''.join(f'<p class="ng">{html.escape(g)}</p><ul>' + ''.join(f'<li><a href="#{i}" data-nav="{i}">{html.escape(t)}</a></li>' for i, t in ts) + '</ul>' for g, ts in nav)
cards = ''
for g, ts in GROUPS:
    cards += f'<h3 class="cg">{html.escape(g)}</h3><div class="cards">' + ''.join(f'<a class="card" href="#{i}"><span class="ct">{html.escape(t)}</span><span class="cd">{html.escape(d)}</span></a>' for (i, p, t, d) in ts) + '</div>'
out = tpl.replace('{{NAV}}', navhtml).replace('{{ARTICLES}}', '\n'.join(articles)).replace('{{CARDS}}', cards).replace('{{ORDER}}', json.dumps([[i, t] for i, t, d, g in order]))
open(OUT, 'w', encoding='utf-8').write(out)
print(len(out))
