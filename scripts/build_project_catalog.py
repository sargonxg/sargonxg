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
        if not row['repository'].startswith('sargonxg/'):
            raise ValueError('Unexpected project owner')
    lines = ['# Public project map', '',
             f"Reviewed {data['reviewed_on']}. {len(projects)} public repositories; private projects are excluded.", '',
             'Start with the [political-data reference examples](https://github.com/sargonxg/TACITUS-Knowledge-Pipeline-open), '
             'the [historical research kit](https://github.com/sargonxg/Syria-political-analysis), or '
             'the [local source readers](https://github.com/sargonxg/tacitus-workbench). '
             'Each repository documents its own setup and data boundaries.', '',
             'The descriptions below are proposed repository About text. The map does not certify '
             'live service availability, benchmark performance, or permission to reuse source. '
             'Check the repository license and upstream attribution before reuse. '
             'PRAXIS hosted generation is paused.', '']
    sections = [
        ('Current and experimental first-party projects', lambda row: not row['archived'] and not row['fork']),
        ('Upstream forks retained for research', lambda row: not row['archived'] and row['fork']),
        ('Archived references', lambda row: row['archived']),
    ]
    for title, predicate in sections:
        lines += ['## ' + title, '', '| Repository | Purpose and boundary |', '| --- | --- |']
        for row in projects:
            if predicate(row):
                description = row['description'].replace('|', '\\|').replace('\n', ' ')
                name = row['repository'].split('/', 1)[1]
                lines.append(f"| [{name}]({row['source_url']}) | {description} |")
        lines.append('')
    lines += ['## Maintain this map', '',
              'The source is [data/public-projects.json](../data/public-projects.json). '
              'Update it only after confirming public visibility and reviewing the default-branch README/source. '
              'Run `python scripts/build_project_catalog.py` to regenerate this page. '
              'These descriptions reflect a README and repository-structure review; '
              'they are not a fresh acceptance test of every application.', '']
    return '\n'.join(lines)


if __name__ == '__main__':
    data = json.loads((ROOT / 'data/public-projects.json').read_text())
    output = ROOT / 'docs/PUBLIC_PROJECT_MAP.md'
    output.write_text(render(data))
    print(f"Rendered {len(data['projects'])} public projects to {output.relative_to(ROOT)}")
