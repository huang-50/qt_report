# Q-tip reporting tool

this is a small report tool. you just need to provide a sql query. running tool to generate email report. You can use this tool with schedule tool like cron or windows task scheduler.

I am writing this tool to test out **copilot**. code and config are more than 400 lines. I finished it in 1 hour with the help of copilot.

while network issue i am not able to finish automation test portion as i planned. i will add it later.

## Installation

### Prerequisites
a workable python 3.6+ environment

pip install -r requirements.txt

### Configuration
1. create report folder under query folder. add your query file as sample report format. you can add multiple query file in report folder.

2. add database connection and email detail in report.yaml. 

## Run report

```sh
    go sample_report_1 
    # replace sample_report_1 with your report folder name 
```

## License

this tool is licensed under Apache License 2.0
