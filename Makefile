default: init
	pdflatex -synctex=1 -interaction=nonstopmode "head".tex > /dev/null


init:
ifeq ('$(wildcard include)','')
	mkdir include
	mkdir plots
	mkdir img
endif

clear:
	rm -f head.pdf
	rm -f head.log
	rm -f head.aux
	rm -f head.synctex.gz
	rm -f head.toc