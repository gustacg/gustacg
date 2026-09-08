"""Tira do calendário 3D o radar de contribuições e a linha de estrelas e forks.

O radar mede issue, pull request e review, que não fazem parte do trabalho
deste perfil, e a linha de estrelas e forks mede repositório público, que é
uma fração pequena do que existe. Ficam o calendário e o total.
"""
import glob
import re

for caminho in glob.glob("profile-3d-contrib/*.svg"):
    svg = open(caminho, encoding="utf-8").read()
    eixo = svg.find('<g class="axis">')
    fim_radar = svg.find("</polygon></g>")
    if eixo > 0 and fim_radar > 0:
        inicio_radar = svg.rfind('<g transform="translate(', 0, eixo)
        svg = svg[:inicio_radar] + svg[fim_radar + len("</polygon></g>"):]
    svg = re.sub(
        r'<g transform="translate\(608, 802\), scale\(2\)">.*?x="772"[^>]*>[^<]*(?:<title>[^<]*</title>)?</text>',
        "",
        svg,
        flags=re.S,
    )
    # A pizza de linguagens só enxerga repositório público, então mente sobre o todo.
    total = svg.find('<g><text style="font-size: 32px; font-weight: bold;" x="384"')
    inicio_pizza = svg.rfind('<g transform="translate(40, 520)">', 0, total)
    if inicio_pizza > 0:
        fim_pizza = svg.find("</path></g></g>", inicio_pizza) + len("</path></g></g>")
        svg = svg[:inicio_pizza] + svg[fim_pizza:]
    open(caminho, "w", encoding="utf-8").write(svg)
    print(caminho, "radar" if eixo > 0 else "sem radar", len(svg))
