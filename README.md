## Framework for Testing WAFs (FTW)
[![Build Status](https://travis-ci.org/CRS-support/ftw.svg?branch=master)](https://travis-ci.org/fastly/ftw)
[![PyPI version](https://badge.fury.io/py/ftw.svg)](https://badge.fury.io/py/ftw)

##### Purpose
This project was created by researchers from ModSecurity and Fastly to help provide rigorous tests for WAF rules. It uses the OWASP Core Ruleset V3 as a baseline to test rules on a WAF. Each rule from the ruleset is loaded into a YAML file that issues HTTP requests that will trigger these rules. Users can verify the execution of the rule after the tests are issued to make sure the expected response is received from an attack

Goals / Use cases include:

* Find regressions in WAF deployments by using continuous integration and issuing repeatable attacks to a WAF
* Provide a testing framework for new rules into ModSecurity, if a rule is submitted it MUST have corresponding positive & negative tests
* Evaluate WAFs against a common, agreeable baseline ruleset (OWASP)
* Test and verify custom rules for WAFs that are not part of the core rule set

For our 1.0 release announcement, check out the [OWASP CRS Blog](https://coreruleset.org/20170810/testing-wafs-ftw-version-1-0-released/)

## Installation
* `git clone https://github.com/CRS-support/ftw.git`
* `cd ftw`
* `virtualenv env && source ./env/bin/activate` 
* `pip install -r requirements.txt`
* `py.test -s -v test/test_default.py --ruledir=test/yaml`

## Writing your first tests
The core of FTW is it's extensible `yaml` based tests. This section lists a few resources on how they are formatted, how to write them and how you can use them.
 
OWASP CRS wrote a great [blog post](https://coreruleset.org/20170915/writing-ftw-test-cases-for-owasp-crs/) describing how FTW tests are written and executed. 

[YAMLFormat.md](https://github.com/CRS-support/ftw/blob/master/docs/YAMLFormat.md) is ground truth of all `yaml` fields that are currently understood by FTW.

After reading these two resources, you should be able to get started in writing tests. You will most likely be checking against status code responses, or web request responses using the `log_contains` directive. For integrating FTW to test regexes within your WAF logs, refer to [ExtendingFTW.md](https://github.com/CRS-support/ftw/blob/master/docs/ExtendingFTW.md)

## Provisioning Apache+Modsecurity+OWASP CRS
If you require an environment for testing WAF rules, there has been one created with Apache, Modsecurity and version 3.0.0 of the OWASP core ruleset. This can be deployed by:

* Checking out the repository: ``git clone https://github.com/fastly/waf_testbed.git``
* Typing ```vagrant up```
