# ay.by_test

  Steps for automation testing on Python:
1. open cmd in folder
2. git clone https://github.com/metalveor/ay_by_test.git  
3. cd .\ay_by_test\
4. pip install requirements.txt
5. pytest -v --reruns 2 -n 2 --alluredir reports
6. allure serve reports