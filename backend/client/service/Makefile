# https://stackoverflow.com/questions/5950395/makefile-to-compile-multiple-c-programs
targets = srv
all: $(targets)


$(targets): %: %.c
	@mkdir -p out
	$(CC) $(CFLGAS) -o out/$@ $<

clean:
	rm -f out/$(targets)
