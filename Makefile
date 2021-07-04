PROGRAM_NAME := tests.py

INPUT_V := 500 2500 5000
INPUT_K := 3 5 7

all:
	rm -r results; mkdir results

	for v in $(INPUT_V); do \
		for k in $(INPUT_K); do \
			python3 $(PROGRAM_NAME) $$v $$k;  \
		done; \
	done