run:
	python discord_client.py

test:
	echo "Testing"
	pytest

release:
	bumpversion patch

release_minor:
	bumpversion minor

release_major:
	bumpversion major
