all: 
	pdflatex Oppgave.tex
	biber Oppgave
	pdflatex Oppgave.tex
	open Oppgave.pdf
