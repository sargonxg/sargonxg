#!/usr/bin/env python3
"""Render the reviewed public project map without querying private repositories."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render(data):
    projects = data['projects']
    names = [row['repository'] for row in projects]
    if len(names) != len(set(names)):
        raise ValueError('Duplicate public project')
    for row in projects:
        if row['source_url'] != 'https://github.com/' + row['repository']:
            raise ValueError('Repository/source URL mismatch')
        if row.get('visibility') != 'public':
            raise ValueError('Only explicitly verified public projects may be rendered')
        if row['repository'].split('/', 1)[0] not in {'sargonxg', 'TACITUS-me'}:
            raise ValueError('Unexpected project owner')
    allowed = {'CORE','FRONT_DOOR','PUBLIC_REFERENCE','PROFILE','DOMAIN_RESEARCH','PAUSE_PARALLEL_PRODUCT','BOUNDED_RESEARCH','REFERENCE_ONLY','ARCHIVE_AFTER_PRESERVATION','PERSONAL','ARCHIVE_AFTER_EXTRACTION','KEEP_ARCHIVED'}
    for row in projects:
        if row.get('proposed_lifecycle') not in allowed or row.get('lifecycle_executed') is not False:
            raise ValueError('Lifecycle proposals require a known role and an explicit unexecuted state')
    lines = ['# Public TACITUS project map', '',
             f"Reviewed {data['reviewed_on']}. {len(projects)} public TACITUS repositories/profiles. Private repositories are excluded. Two independent public personal projects are linked separately below.", '',
             'Start with the [reference pipeline](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open), '
             '[Workbench](https://github.com/sargonxg/tacitus-workbench), '
             '[historical research kit](https://github.com/sargonxg/Syria-political-analysis), or the separate '
             '[invited App](https://app.tacitus.me/). '
             '[Product direction and top 20 actions](GROWTH_PLAN.md).', '',
             'Retirement candidates have historical-purpose notices; archival is pending required access/dependency checks. No permanent deletion is planned. Current source, native experiments and hosted acceptance remain separate. '
             'Original upstream licenses and source rights apply. PRAXIS is a separate paused workspace.', '']
    sections = [
        ('Current first-party source and proposed roles', lambda row: not row['archived'] and not row['fork']),
        ('Upstream forks: evaluate the need before maintaining a separate fork', lambda row: not row['archived'] and row['fork']),
        ('Archived references: preserved history', lambda row: row['archived']),
    ]
    def safe(value): return str(value).replace('|', '\\|').replace('\n', ' ')
    for title, predicate in sections:
        lines += ['## ' + title, '', '| Repository | Purpose and boundary | Proposed role | Next useful action |', '| --- | --- | --- | --- |']
        for row in projects:
            if predicate(row):
                name = row['repository']
                lines.append(f"| [{name}]({row['source_url']}) | {safe(row['description'])} | {safe(row['proposed_lifecycle'])} | {safe(row['next_useful_action'])} |")
        lines.append('')
    lines += ['## Independent personal work', '',
              '[Poetry](https://github.com/sargonxg/Poetry-I-Like) and '
              '[Baroque Music Room](https://github.com/sargonxg/Baroque-music-room) keep their own purpose and identity. '
              'Neither is an archival/deletion or TACITUS-branding proposal.', '',
              '## Maintain this map', '',
              'The source is [data/public-projects.json](../data/public-projects.json). '
              'Confirm public visibility and inspect the source before updating it. '
              'Run `python scripts/build_project_catalog.py` and the public-catalogue tests. '
              'A lifecycle proposal must remain explicitly unexecuted until a separately authorized operation is completed; '
              'editing this catalogue never archives or deletes a repository.', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    data = json.loads((ROOT / 'data/public-projects.json').read_text(encoding='utf-8'))
    output = ROOT / 'docs/PUBLIC_PROJECT_MAP.md'
    output.write_text(render(data), encoding='utf-8')
    print(f"Rendered {len(data['projects'])} public projects to {output.relative_to(ROOT)}")
