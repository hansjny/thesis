all: 
	pdflatex Oppgave.tex
	biber Oppgave
	pdflatex Oppgave.tex
	open Oppgave.pdf
clean:
	rm Oppgave.aux Oppgave.bbl Oppgave.bcf Oppgave.blg Oppgave.log Oppgave.toc Oppgave.run.xml Oppgave.lof
