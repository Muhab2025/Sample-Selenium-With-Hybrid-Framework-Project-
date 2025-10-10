pytest test_cases -rA -m smoke
:: pytest test_cases -rA -m regression
:: pytest test_cases -rA -m "smoke or regression"
:: pytest test_cases -rA -m smoke --html="./reports/HTMLReportName.html"
:: pytest test_cases -rA
pause "Press any key to continue..."