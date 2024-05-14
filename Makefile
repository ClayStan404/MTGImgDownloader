PYTHON = python3

run:
	if [ ! -d imgs ] ; then mkdir imgs;fi
	$(PYTHON) src/getMTGPic.py

clean:
	rm -f imgs/*.jpg
	rm -rf cardList

rebuild: clean run

.PHONY: run clean

