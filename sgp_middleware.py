#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import re
from pathlib import Path

PASTA = os.path.expanduser("~/sgp/episodios")

def listar_episodios():
    path = Path(PASTA)
    arquivos = sorted(path.glob("episodio_*.md"))
    return {"total": len(arquivos), "episodios": [f.name for f in arquivos]}

def buscar_cena(ep, cena, sufixo=""):
    arquivo = Path(PASTA) / f"episodio_{str(ep).zfill(2)}.md"
    if not arquivo.exists():
        return {"erro": f"Episódio {ep} não encontrado"}
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    padrao = rf"^{re.escape(str(cena))}(?:\s|$)"
    linhas = conteudo.split('\n')
    
    for i, linha in enumerate(linhas):
        if re.match(padrao, linha.strip()):
            texto = [linhas[i]]
            for j in range(i+1, len(linhas)):
                if re.match(r"^\d+(?:\s|$)", linhas[j].strip()):
                    break
                texto.append(linhas[j])
            return {"sucesso": True, "conteudo": '\n'.join(texto).strip()}
    
    return {"erro": f"Cena {cena}{sufixo} não encontrada"}

if __name__ == "__main__":
    print("\n🎬 SGP - MIDDLEWARE DE PRODUÇÃO\n")
    print("=" * 70)
    
    print("\n📋 Episódios encontrados:")
    resultado = listar_episodios()
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
    
    print("\n" + "=" * 70)
    print("✓ Sistema pronto!")
