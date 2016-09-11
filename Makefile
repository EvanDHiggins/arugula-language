GRAMMAR=Arugula.g4
ANTLR=java -Xmx500M -cp "/usr/local/lib/antlr-4.5-complete.jar:$CLASSPATH" org.antlr.v4.Tool
ANTLRARGS=-Dlanguage=Python3 -no-listener -visitor

antlr: $(GRAMMAR)
	$(ANTLR) $(ANTLRARGS) $^

.PHONY: clean
clean:
	rm Arugula.tokens ArugulaLexer.py ArugulaLexer.tokens ArugulaListener.py ArugulaVisitor.py ArugulaParser.py
