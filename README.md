# Find the Bad: Model 3
This is an introductory lab for doing log analysis with Kibana.  It should only require the installation of Docker and Docker Compose. 

## Disclaimer
This lab is based on real data containing actual malicious indicators.  If you attempt to do things such as find and run files, or visit network entities that occur in these logs, you do so at your own risk.

## Setup
1) Download and install [Docker](https://www.docker.com/get-started).
2) Download and install [Docker Compose](https://docs.docker.com/compose/install/) (On Windows Docker Compose should be bundled with the Docker installer, so this step shouldn't be required).
3) Download or clone this repository.
4) Open up a command prompt, make your way to this repository folder on your local machine and run `docker-compose up`.
5) When `docker-compose up` is finished bringing the containers up, open a browser and navigate to `http://localhost:5601` to access the Kibana instance.

`compose-and-kibana.gif` shows steps four and five in action.

## The Lab
This lab is to start getting you comfortable with Kibana for analysis and familiar with the types of questions that you would try to answer when you find signs of a compromise.  A Dashboard called `VT Hunting` has been created that should provide you the information you need to get started.

### Questions
1) What is the name of the malicious file that has executed?
2) What strain of malware does it appear to be?
3) What does this malware typically do?
4) When was this malware run and by which user on what computer? (Hint: Try pinning a `Dashboard` filter and viewing it in `Discover`)
5) What process wrote the malicious file to disk and when?

### Useful Links
- [What are MD5, SHA-1, and SHA-256 Hashes, and How Do I Check Them?](https://www.howtogeek.com/67241/htg-explains-what-are-md5-sha-1-hashes-and-how-do-i-check-them/)
- [VirusTotal](https://www.virustotal.com/gui/home/upload)
- [Sysmon Events List](https://docs.microsoft.com/en-ca/sysinternals/downloads/sysmon#events)
- [Sysmon Event ID 1 Fields](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=90001)
- [Sysmon Event ID 11 Fields](https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=90011)
- [Kibana Dashboard](https://www.elastic.co/guide/en/kibana/current/dashboard.html)
- [Kibana Discover](https://www.elastic.co/guide/en/kibana/current/discover.html)

### Solution
Available [here](https://findthebad.com/model-3/).