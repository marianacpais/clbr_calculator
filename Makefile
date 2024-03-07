docker:
	docker build -t clbrcalculator:alfa .
	docker run --name clbrcalculator -d -p 8080:8080 clbrcalculator:alfa
