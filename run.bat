@echo off
call venv\scripts\activate
pytest -v -s --html .\reports\test_results.html .\test_cases
rem pytest -v -s -m "regression" --html .\reports\test_results.html 
rem pytest -v -s -m "regression" --html .\reports\test_results.html 
rem pytest -v -s -m "sanity and regression" --html .\reports\test_results.html 
rem pytest -v -s -m "sanity or regression" --html .\reports\test_results.html 
pause


#note
#if you want any another way remove rem from starting