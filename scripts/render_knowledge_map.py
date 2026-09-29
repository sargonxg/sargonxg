"""Render the profile's deterministic SVG architecture illustration (stdlib only).

The topology is illustrative, not telemetry or extracted research findings.
The nine layer names follow the public TACITUS capsule reference architecture.
"""
from html import escape
from pathlib import Path
import math
import random

OUT = Path(__file__).resolve().parents[1] / 'assets' / 'policy-knowledge-map.svg'
rng = random.Random(29)
parts = []
def add(s):
    parts.append(s)
def text(x, y, value, size=20, color='#d7e3ef', weight=400, anchor='start', family='Inter,Segoe UI,Arial,sans-serif', extra=''):
    add(f'<text x="{x}" y="{y}" fill="{color}" font-family="{family}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" {extra}>{escape(value)}</text>')
def rect(x,y,w,h,fill='#0e1c2a',stroke='#233749',rx=8,extra=''):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" {extra}/>')
def line(x1,y1,x2,y2,color='#496278',opacity=.3,width=1,extra=''):
    add(f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" fill="none" stroke="{color}" stroke-opacity="{opacity}" stroke-width="{width}" {extra}/>')
def circle(x,y,r,color,opacity=1,extra=''):
    add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}" opacity="{opacity}" {extra}/>')

add('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1060" role="img" aria-labelledby="title desc">')
add('<title id="title">TACITUS / PRAXIS — from contested evidence to reviewable judgment</title>')
add('<desc id="desc">An illustrative dense knowledge graph links sources, actors, claims, commitments, events, methods and alternatives to reviewed context. Nine architecture layers distinguish evidence, claims, situation, time, ontology, reasoning, memory, governance and runtime. A fictional Nordalia example ends in a caveated conclusion, a verification question and a proposed next step. This is a conceptual architecture map, not a live product screenshot.</desc>')
add('<defs><radialGradient id="halo"><stop stop-color="#16b8ab" stop-opacity=".09"/><stop offset="1" stop-color="#16b8ab" stop-opacity="0"/></radialGradient><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#809bb1" opacity=".14"/></pattern></defs>')
rect(0,0,1600,1060,'#08131f','#2a4154',16)
rect(1,1,1598,1058,'url(#grid)','none',16)
text(48,51,'TACITUS / PRAXIS',21,'#5fe0cd',650,extra='letter-spacing="3"')
text(1552,51,'POLICY  ·  KNOWLEDGE  ·  SYSTEMS',17,'#9fb3c8',500,'end',extra='letter-spacing="2"')
text(48,111,'From contested evidence to reviewable judgment.',43,'#f2f6fa',600)
text(48,148,'Sources, ideas, relationships and analytical methods — connected, with uncertainty kept visible.',22,'#a6bbce')
line(48,176,1552,176,'#476078',.65)

# Layered graph field: quiet structural planes behind a deliberately dense topology.
for i in range(4):
    y=231+i*108
    add(f'<path d="M75,{y+20} L870,{y-29} L1120,{y+118} L313,{y+166} Z" fill="#112333" fill-opacity=".2" stroke="#45657a" stroke-opacity=".23"/>')
add('<ellipse cx="570" cy="480" rx="590" ry="290" fill="url(#halo)"/>')

clusters = [
    ('SOURCES',210,310,'#62cce5',34),
    ('ACTORS',520,285,'#62d5bc',29),
    ('COMMITMENTS',910,312,'#edb271',29),
    ('CLAIMS',280,489,'#f1c86d',33),
    ('ALTERNATIVES',965,518,'#eaa2bd',26),
    ('TIME & EVENTS',238,664,'#91b9fb',28),
    ('METHODS',666,671,'#bcb3f2',32),
]
points=[]
for label,cx,cy,color,count in clusters:
    cluster=[]
    for i in range(count):
        angle=i*2.399963+rng.uniform(-.18,.18)
        radius=math.sqrt((i+1)/count)*rng.uniform(80,134)
        p=(cx+math.cos(angle)*radius,cy+math.sin(angle)*radius*.72)
        cluster.append(p)
    points.append(cluster)

# Fine local links and cross-layer relations. No node/edge total is presented as product scale.
for ci,cluster in enumerate(points):
    color=clusters[ci][3]
    for i,p in enumerate(cluster):
        for j in rng.sample([j for j in range(len(cluster)) if j!=i],3):
            q=cluster[j]
            line(*p,*q,color,.18,1)
        if i%3==0:
            dest=points[(ci+1)%len(points)][(i*3)%len(points[(ci+1)%len(points)])]
            line(*p,*dest,'#7a9baa',.13,1)
        if i%5==0:
            line(*p,612,470,color,.21,1.2)
    for i,(x,y) in enumerate(cluster):
        circle(x,y,3.2 if i%5 else 5,color,.65 if i%4 else .95)
        if i%9==0:
            circle(x,y,9,'none',1,extra=f'stroke="{color}" stroke-opacity=".28"')

# Selected paths rise out of the dense structure.
for a,b,c in [(0,3,'#f1c86d'),(1,2,'#62d5bc'),(3,4,'#eaa2bd'),(5,2,'#91b9fb'),(6,4,'#bcb3f2')]:
    _,x,y,_,_=clusters[a]; _,xx,yy,_,_=clusters[b]
    add(f'<path d="M{x},{y} Q{(x+xx)/2},{(y+yy)/2-110} {xx},{yy}" fill="none" stroke="{c}" stroke-opacity=".55" stroke-width="2"/>')
for label,cx,cy,color,count in clusters:
    w=max(144,len(label)*12+28)
    rect(cx-w/2,cy-22,w,44,'#0a1724',color,5)
    text(cx,cy+7,label,19,color,650,'middle',extra='letter-spacing="1"')

circle(612,470,91,'#112d36',.8,extra='stroke="#62d5bc" stroke-opacity=".36"')
circle(612,470,73,'#102833',1,extra='stroke="#7af1d6" stroke-width="1.5"')
text(612,449,'REVIEWED',18,'#8de7d6',600,'middle',extra='letter-spacing="2"')
text(612,481,'CONTEXT',29,'#f0f8f6',650,'middle')
text(612,508,'human judgment',16,'#accdc7',400,'middle')

def chip(x,y,label,color):
    width=len(label)*9.5+22
    rect(x,y,width,30,'#0a1623','#2b4255',4)
    text(x+11,y+21,label,17,color)
chip(85,207,'documents · source spans','#83d8ed')
chip(449,209,'institutions · interests','#8ce3d0')
chip(850,217,'terms · conditions','#f0c493')
chip(75,548,'allegation ↔ denial','#f4d990')
chip(839,588,'competing hypotheses','#edb6cb')
chip(87,754,'occurred ≠ recorded','#abc8fa')
chip(586,754,'assumptions · critique','#cec7fa')

# Nine named architecture layers, matching the public reference design.
rect(1177,205,375,583,'#0c1b29','#2b4357',10)
text(1201,241,'ONE CONTEXT · NINE LAYERS',18,'#d9e7f1',600,extra='letter-spacing="1"')
layers=[('01','Evidence','sources · excerpts','#62cce5'),('02','Claims','attribution · disputes','#f1c86d'),('03','Situation','actors · relationships','#62d5bc'),('04','Temporal','events · two clocks','#91b9fb'),('05','Ontology','types · meaning','#77cdd7'),('06','Reasoning','methods · alternatives','#bcb3f2'),('07','Memory','versions · lineage','#a7bac9'),('08','Governance','permissions · review','#95dca9'),('09','Runtime','instructions · constraints','#5fe0cd')]
for i,(num,label,note,color) in enumerate(layers):
    y=278+i*55
    line(1200,y+37,1528,y+37,'#284256',.55)
    text(1201,y+10,num,17,color,500,family='Consolas,monospace')
    text(1242,y+9,label,22,'#e2ecf4',550)
    text(1242,y+30,note,17,'#9fb5c9')

# The analytical destination is explicit, rather than a graph for its own sake.
line(48,822,1552,822,'#476078',.65)
text(48,858,'ILLUSTRATIVE POLICY READOUT',18,'#99afc4',600,extra='letter-spacing="2"')
cards=[(48,'CONCLUSION · CAVEATED','Dialogue remains possible.','Suspension and willingness to talk coexist.','#62d5bc'),(556,'OPEN QUESTION','What can be verified?','An allegation and a denial remain distinct.','#f1c86d'),(1064,'IDEA TO TEST','Clarify verification terms.','Link next steps to evidence and review.','#91b9fb')]
for x,kicker,title,subtitle,color in cards:
    rect(x,878,488,112,'#0e2030','#294255',7)
    add(f'<rect x="{x}" y="878" width="4" height="112" fill="{color}"/>')
    text(x+22,904,kicker,16,color,650,extra='letter-spacing="1"')
    text(x+22,938,title,25,'#eef5fa',550)
    text(x+22,969,subtitle,18,'#adbdcc')
text(48,1028,'Conceptual architecture · fictional Nordalia scenario · not live telemetry',17,'#91a7bb')
text(1552,1028,'DESIGNED FOR INSPECTION',16,'#5fe0cd',550,'end',extra='letter-spacing="2"')
add('</svg>')
OUT.parent.mkdir(exist_ok=True)
OUT.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(f'Rendered {OUT.name} ({OUT.stat().st_size:,} bytes)')

# A separate portrait composition keeps the same story legible on GitHub mobile.
parts=[]
rng=random.Random(29)
add('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 1330" role="img" aria-labelledby="title desc">')
add('<title id="title">TACITUS / PRAXIS — a layered policy knowledge map</title><desc id="desc">A conceptual graph connects sources, actors, claims, time and methods to reviewed context. Nine layers lead to a caveated conclusion, a verification question and an idea to test. Fictional policy scenario, not live telemetry.</desc>')
rect(0,0,760,1330,'#08131f','#2a4154',14)
text(34,48,'TACITUS / PRAXIS',25,'#5fe0cd',650,extra='letter-spacing="2"')
text(34,105,'Evidence. Context.',43,'#f2f6fa',600)
text(34,158,'Reviewable judgment.',43,'#f2f6fa',600)
line(34,188,726,188,'#476078',.65)
mobile_clusters=[('SOURCES',167,295,'#62cce5'),('ACTORS',570,295,'#62d5bc'),('CLAIMS',145,480,'#f1c86d'),('TIME',220,623,'#91b9fb'),('METHODS',579,581,'#bcb3f2')]
mobile_points=[]
for _,x,y,color in mobile_clusters:
    group=[]
    for i in range(27):
        a=i*2.399963
        radius=math.sqrt((i+1)/27)*rng.uniform(78,126)
        group.append((x+math.cos(a)*radius,y+math.sin(a)*radius*.72))
    mobile_points.append(group)
for k,group in enumerate(mobile_points):
    color=mobile_clusters[k][3]
    for i,p in enumerate(group):
        for j in rng.sample(range(len(group)),3):
            line(*p,*group[j],color,.25,1.4)
        if i%3==0:
            line(*p,*mobile_points[(k+1)%5][i],'#7292a8',.2,1.1)
        if i%4==0:
            line(*p,390,449,color,.35,1.4)
    for i,(x,y) in enumerate(group):
        circle(x,y,3.5 if i%4 else 5,color,.8)
for name,x,y,color in mobile_clusters:
    w=len(name)*17+30
    rect(x-w/2,y-24,w,48,'#0a1724',color,5)
    text(x,y+10,name,28,color,650,'middle')
circle(390,449,91,'#102833',1,extra='stroke="#7af1d6" stroke-width="1.6"')
text(390,429,'REVIEWED',22,'#8de7d6',600,'middle')
text(390,469,'CONTEXT',32,'#f0f8f6',650,'middle')
text(34,726,'NINE CONNECTED LAYERS',24,'#a5bbce',600,extra='letter-spacing="1"')
for i,(num,label,note,color) in enumerate(layers):
    x=34+(i%3)*237; y=750+(i//3)*60
    rect(x,y,219,48,'#0e2030','#294255',5)
    text(x+12,y+32,label,27,color,550)
for i,(_,kicker,title,subtitle,color) in enumerate(cards):
    y=958+i*101
    rect(34,y,692,86,'#0e2030','#294255',6)
    add(f'<rect x="34" y="{y}" width="4" height="86" fill="{color}"/>')
    text(55,y+27,kicker,21,color,600)
    text(55,y+64,title,33,'#eef5fa',550)
text(34,1288,'Conceptual map · fictional scenario',24,'#91a7bb')
text(34,1316,'Not a live product screenshot',22,'#91a7bb')
add('</svg>')
mobile=OUT.with_name('policy-knowledge-map-mobile.svg')
mobile.write_text('\n'.join(parts)+'\n',encoding='utf-8')
print(f'Rendered {mobile.name} ({mobile.stat().st_size:,} bytes)')
