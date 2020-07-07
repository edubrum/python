	
all:
	@echo "Executing exIf.py"
	@echo " "
	python3 exIf.py
	@echo "-----------------------"
	@echo " "
	@echo "Executing exWhile.py"
	@echo " "
	python3 exWhile.py
	@echo "-----------------------"
	@echo " "
	@echo "Executing permutation.py"
	@echo " "
	python3 permutation.py
	@echo "-----------------------"
	@echo " "
	@echo "Executing exFun.py"
	@echo " "
	python3 exFun.py
	@echo "-----------------------"
	@echo " "
	@echo "Executing exExitCopyPaste.py"
	@echo " "
	python3 exExitCopyPaste.py
	@echo "-----------------------"
	@echo " "
	@echo "Executing exExceptSttmts.py"
	@echo " "
	python3 exExceptSttmts.py
	@echo "-----------------------"
	@echo " "
	@echo "Executing exGuess.py"
	@echo " "
	python3 exGuess.py
	@echo "-----------------------"
	@echo " "
	
install: 
	@bash installingPython3-PIP
