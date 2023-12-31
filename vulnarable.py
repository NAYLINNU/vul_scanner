#!/usr/bin/env python
import scanner

target_url = "http://192.168.251.6/dvwa/"
links_to_ignore = ["http://192.168.251.6/dvwa/logout.php"]
data_dict = {"username": "admin", "password": "password", "Login": "submit"}

vuln_scanner = scanner.Scanner(target_url, links_to_ignore)
vuln_scanner.session.post("http://192.168.251.6/dvwa/login.php", data=data_dict)

vuln_scanner.crawl()
vuln_scanner.run_scanner()

#forms = vuln_scanner.extract_form("http://192.168.159.6/dvwa/vulnerabilities/xss_r/")

#response = vuln_scanner.test_xss_in_link( "testtest","http://192.168.159.6/dvwa/vulnerabilities/xss_r/?name=test")
#print(response)