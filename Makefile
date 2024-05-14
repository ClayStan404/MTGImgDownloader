PYTHON = python3  # Adjust if you use a different interpreter

run:
	$(PYTHON) src/getMTGPic.py

clean:
	rm -f imgs/*.jpg  # Remove all downloaded JPEG images
	rm -rf cardList

rebuild: clean run

.PHONY: run clean

