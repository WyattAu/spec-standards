# spec-standards: same verbs everywhere (OMNI-CORE 2, SPEC-CORE SC-9)

TIER ?= s
REGISTRY ?= ../engineering-standards/estate.yml

.PHONY: help lint check audit registry ci

help:
	@echo "lint      - markdownlint over all Markdown (tool optional; SKIP when absent)"
	@echo "check     - scripts/doc-lint.sh \$$TIER (default tier: s)"
	@echo "audit     - scripts/spec-audit.py --repo ."
	@echo "registry  - scripts/spec-audit.py --registry \$$REGISTRY"
	@echo "ci        - check + audit (the gate CI mirrors)"

lint:
	@if command -v markdownlint >/dev/null 2>&1; then \
		markdownlint "**/*.md" --config .markdownlint.json; \
	else \
		echo "SKIP: markdownlint not installed (nix devShell provides it)"; \
	fi

check:
	@./scripts/doc-lint.sh $(TIER)

audit:
	@python3 scripts/spec-audit.py --repo .

registry:
	@if [ -f "$(REGISTRY)" ]; then \
		python3 scripts/spec-audit.py --registry "$(REGISTRY)"; \
	else \
		echo "SKIP: registry not found at $(REGISTRY)"; \
	fi

ci: check audit
