PY = python3
GEN = update.py
include Makefile.git
blog:
	$(PY) $(GEN)
	$(call git_commit)
