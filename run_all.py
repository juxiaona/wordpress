from base.testrunner import TestRunner
from base.sendmail import SendMail

if __name__ == '__main__':
	
	run_all=TestRunner("./testcases","Auto Test Report","Test case execution")
	run_all.run()


