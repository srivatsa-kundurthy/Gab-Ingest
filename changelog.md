# Changes

Error: 

Traceback (most recent call last):
  File "/Users/srivatsakundurthy/opt/anaconda3/bin/gabber", line 5, in <module>
    from gabber.client import cli_entrypoint
  File "/Users/srivatsakundurthy/opt/anaconda3/lib/python3.9/site-packages/gabber/client.py", line 22, in <module>
    import undetected_chromedriver.v2 as uc
ModuleNotFoundError: No module named 'undetected_chromedriver.v2'

Correction: 

delete v2

selenium.common.exceptions.WebDriverException: Message: unknown error: cannot connect to chrome at 127.0.0.1:65420
from session not created: This version of ChromeDriver only supports Chrome version 110
Current browser version is 109.0.5414.119

Update chromedriver to latest version



