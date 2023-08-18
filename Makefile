.PHONY: format
format:
	@rye run ruff check . --select I --fix-only --exit-zero
	@rye run black .

.PHONY: format-check
format-check:
	@rye run ruff check . --select I
	@rye run black --check .

.PHONY: lint
lint:
	@rye run ruff check .
	@rye run mypy --show-error-codes .

.PHONY: test
test:
	@rye run pytest tests

.PHONY: pre-commit
pre-commit: format lint test
