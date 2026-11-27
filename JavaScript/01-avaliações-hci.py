"""
Módulo 01: Interação Humano-Computador (IHC) e Avaliação de Interfaces
Adaptação executável do README.md (01-avaliações-hci) para o PyCharm.

Como rodar:
    1. Abra este arquivo no PyCharm.
    2. Clique com o botão direito no editor > Run 'modulo01_ihc'
       (ou use o botão verde ▶ no topo).

Requisitos: apenas Python 3.8+ (Tkinter já vem instalado).
"""

import tkinter as tk
from tkinter import messagebox

# ----------------------------------------------------------------------
# DADOS (edite aqui para mudar o conteúdo da página)
# ----------------------------------------------------------------------
TITULO = "Módulo 01: Interação Humano-Computador (IHC) e Avaliação de Interfaces"

BADGES = [
    ("Status", "Completed", "#4c1"),
    ("Norma", "ISO 9241", "#fe7d37"),
    ("Instituição", "CEUB", "#800080"),
]

VISAO_GERAL = (
    "Este diretório contém avaliações práticas com foco na interação "
    "humano-computador (IHC), heurísticas de usabilidade, diretrizes de "
    "acessibilidade (WCAG) e normas ergonômicas (ISO 9241) aplicadas a "
    "sistemas de software acadêmicos do mundo real."
)

TABELA_CABECALHO = ("Projeto/Atividade", "Descrição", "Link")
TABELA_LINHAS = [
    (
        "Auditoria do Portal do Aluno da CEUB",
        "Avaliação abrangente de UX/UI e ISO 9241 do portal do aluno da UniCEUB.",
        "ceub-portal-audit/",
    ),
]

RESULTADOS = [
    "Identificação dos elementos de entrada e saída da interface.",
    "Avaliação da usabilidade do software, prevenção de erros e atrito cognitivo.",
    "Analisando implementações de acessibilidade (leitores de tela, contraste, navegação multimodal).",
    "Aplicação dos princípios ergonômicos da norma ISO 9241 (Eficácia, Eficiência e Satisfação).",
]

# ----------------------------------------------------------------------
# ESTILO
# ----------------------------------------------------------------------
COR_FUNDO = "#ffffff"
COR_TEXTO = "#1f2328"
COR_BORDA = "#d1d9e0"
COR_LINK = "#0969da"
COR_CODIGO_BG = "#eff1f3"

FONTE_H1 = ("Segoe UI", 22, "bold")
FONTE_H2 = ("Segoe UI", 17, "bold")
FONTE_TEXTO = ("Segoe UI", 11)
FONTE_NEGRITO = ("Segoe UI", 11, "bold")
FONTE_BADGE = ("Verdana", 8)
FONTE_CODIGO = ("Consolas", 10)


class PaginaIHC(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Módulo 01 – IHC e Avaliação de Interfaces")
        self.geometry("980x760")
        self.minsize(640, 480)
        self.configure(bg=COR_FUNDO)

        self._labels_quebra = []  # labels cujo wraplength acompanha a janela
        self._criar_area_rolavel()
        self._montar_pagina()

    # ------------------------------------------------------------------
    # Área com barra de rolagem
    # ------------------------------------------------------------------
    def _criar_area_rolavel(self):
        self.canvas = tk.Canvas(self, bg=COR_FUNDO, highlightthickness=0)
        barra = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=barra.set)

        barra.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.conteudo = tk.Frame(self.canvas, bg=COR_FUNDO)
        self._janela = self.canvas.create_window(
            (0, 0), window=self.conteudo, anchor="nw"
        )

        self.conteudo.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.bind("<Configure>", self._ao_redimensionar)

        # Roda do mouse (Windows/macOS e Linux)
        self.bind_all("<MouseWheel>", self._rolar)
        self.bind_all("<Button-4>", lambda e: self.canvas.yview_scroll(-1, "units"))
        self.bind_all("<Button-5>", lambda e: self.canvas.yview_scroll(1, "units"))

    def _rolar(self, evento):
        self.canvas.yview_scroll(int(-evento.delta / 120), "units")

    def _ao_redimensionar(self, evento):
        self.canvas.itemconfigure(self._janela, width=evento.width)
        largura_texto = max(evento.width - 100, 200)
        for lbl, desconto in self._labels_quebra:
            lbl.configure(wraplength=largura_texto - desconto)

    # ------------------------------------------------------------------
    # Componentes reutilizáveis
    # ------------------------------------------------------------------
    def _texto(self, pai, texto, fonte=FONTE_TEXTO, desconto=0, **kw):
        lbl = tk.Label(
            pai, text=texto, font=fonte, bg=COR_FUNDO, fg=COR_TEXTO,
            justify="left", anchor="w", **kw,
        )
        self._labels_quebra.append((lbl, desconto))
        return lbl

    def _separador(self, pai, pady=(4, 12)):
        tk.Frame(pai, bg=COR_BORDA, height=1).pack(fill="x", pady=pady)

    def _titulo_secao(self, pai, texto):
        self._texto(pai, texto, FONTE_H2).pack(fill="x", pady=(10, 0))
        self._separador(pai, pady=(4, 10))

    def _badge(self, pai, rotulo, valor, cor):
        quadro = tk.Frame(pai, bg=COR_FUNDO)
        tk.Label(quadro, text=rotulo, font=FONTE_BADGE, bg="#555555",
                 fg="white", padx=6, pady=2).pack(side="left")
        tk.Label(quadro, text=valor, font=FONTE_BADGE, bg=cor,
                 fg="white", padx=6, pady=2).pack(side="left")
        return quadro

    # ------------------------------------------------------------------
    # Montagem da página
    # ------------------------------------------------------------------
    def _montar_pagina(self):
        margem = tk.Frame(self.conteudo, bg=COR_FUNDO)
        margem.pack(fill="both", expand=True, padx=40, pady=24)

        # Título
        self._texto(margem, TITULO, FONTE_H1).pack(fill="x")
        self._separador(margem)

        # Badges
        linha_badges = tk.Frame(margem, bg=COR_FUNDO)
        linha_badges.pack(fill="x", pady=(0, 8))
        for rotulo, valor, cor in BADGES:
            self._badge(linha_badges, rotulo, valor, cor).pack(side="left", padx=(0, 6))

        # Visão geral
        self._titulo_secao(margem, "📌  Visão geral")
        self._texto(margem, VISAO_GERAL).pack(fill="x", pady=(0, 10))
        self._separador(margem, pady=(6, 6))

        # Estrutura de subpastas e projetos
        self._titulo_secao(margem, "📂  Estrutura de subpastas e projetos")
        self._montar_tabela(margem)
        self._separador(margem, pady=(16, 6))

        # Resultados de aprendizagem
        self._titulo_secao(margem, "🎯  Principais Resultados de Aprendizagem")
        for item in RESULTADOS:
            linha = tk.Frame(margem, bg=COR_FUNDO)
            linha.pack(fill="x", pady=2)
            tk.Label(linha, text="•", font=FONTE_TEXTO, bg=COR_FUNDO,
                     fg=COR_TEXTO).pack(side="left", anchor="n", padx=(8, 8))
            lbl = self._texto(linha, item, desconto=40)
            lbl.pack(side="left", fill="x", expand=True)

    def _montar_tabela(self, pai):
        tabela = tk.Frame(pai, bg=COR_BORDA)
        tabela.pack(fill="x")
        tabela.columnconfigure(0, weight=3, uniform="col")
        tabela.columnconfigure(1, weight=4, uniform="col")
        tabela.columnconfigure(2, weight=2, uniform="col")

        # Cabeçalho
        for c, titulo in enumerate(TABELA_CABECALHO):
            cel = tk.Frame(tabela, bg=COR_FUNDO)
            cel.grid(row=0, column=c, sticky="nsew", padx=(1, 1 if c == 2 else 0), pady=1)
            self._texto(cel, titulo, FONTE_NEGRITO, desconto=560).pack(
                fill="x", padx=12, pady=10)

        # Linhas
        for r, (projeto, descricao, link) in enumerate(TABELA_LINHAS, start=1):
            c0 = tk.Frame(tabela, bg=COR_FUNDO)
            c1 = tk.Frame(tabela, bg=COR_FUNDO)
            c2 = tk.Frame(tabela, bg=COR_FUNDO)
            c0.grid(row=r, column=0, sticky="nsew", padx=(1, 0), pady=(0, 1))
            c1.grid(row=r, column=1, sticky="nsew", padx=(1, 0), pady=(0, 1))
            c2.grid(row=r, column=2, sticky="nsew", padx=1, pady=(0, 1))

            self._texto(c0, projeto, FONTE_NEGRITO, desconto=560).pack(
                fill="x", padx=12, pady=10)
            self._texto(c1, descricao, desconto=420).pack(
                fill="x", padx=12, pady=10)

            lbl_link = tk.Label(
                c2, text=link, font=FONTE_CODIGO, bg=COR_CODIGO_BG, fg=COR_LINK,
                cursor="hand2", padx=4, pady=1,
            )
            lbl_link.pack(anchor="w", padx=12, pady=10)
            lbl_link.bind("<Enter>", lambda e, w=lbl_link: w.configure(font=FONTE_CODIGO + ("underline",)))
            lbl_link.bind("<Leave>", lambda e, w=lbl_link: w.configure(font=FONTE_CODIGO))
            lbl_link.bind("<Button-1>", lambda e, l=link: self._abrir_link(l))

    # ------------------------------------------------------------------
    # Ações
    # ------------------------------------------------------------------
    def _abrir_link(self, caminho):
        messagebox.showinfo(
            "Projeto",
            f"Pasta do projeto:\n./{caminho}\n\n"
            "Aqui você pode abrir outra janela, uma pasta ou um relatório.",
        )


def main():
    app = PaginaIHC()
    app.mainloop()


if __name__ == "__main__":
    main()