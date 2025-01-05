

generate:
	@echo "Generating the project..."
	if [ ! -d env ]; then python3 -m venv env; fi
	@echo "Project generated."
	
clean:
	@echo "Cleaning the project..."
	rm -rf env
	@echo "Project cleaned."
