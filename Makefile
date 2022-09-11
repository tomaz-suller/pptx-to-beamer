.PHONY: all clean

PANDOCK = docker run --rm -v "$$(pwd):/data" -u $$(id -u):$$(id -g) pandoc/latex
PANDOCDIR = templates/pandoc/
PANDOCFLAGS = \
	--from=markdown+rebase_relative_paths \
	--to=beamer \
	--include-in-header=$(PANDOCDIR)/preamble.tex \
	--template=$(PANDOCDIR)/custom.tex \
	--bibliography=$(PANDOCDIR)/bibliography.bib \
	--csl=$(PANDOCDIR)/abnt.csl \
	--citeproc

pdf: $(foreach path,$(wildcard slides/3_manual/*/out.md),$(addsuffix .pdf,$(subst 3_manual,4_beamer_pdf,$(subst /out.md,,$(path)))))

slides/4_beamer_pdf/%.pdf: slides/3_manual/%/out.md
	@echo '>>> Processing $< into $@'
	@$(PANDOCK) $(PANDOCFLAGS) --output=$@ $<

manual: slides/2_interim
	cp -r slides/2_interim slides/3_manual

convert: rename $(wildcard slides/1_renamed/*.pptx)
	docker build . -t python-pptx-converter
	docker run \
		--rm -v $$(pwd):/home/jupyter/repo python-pptx-converter \
			python3 repo/src/pptx_to_md.py \
				repo/slides/1_renamed \
				repo/slides/2_interim

rename: $(wildcard "slides/0_raw/*.pptx")
	python src/rename.py slides/0_raw slides/1_renamed

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf slides/{1_renamed,2_interim,4_beamer_pdf}/*
