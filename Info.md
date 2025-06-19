NOTION_API_KEY=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
# Notion
Write in my Notion MCP Demo the list of @hyperparameters.yaml 

# Whole Workflow
- launch a run on ai server tool with hyperparameters specified in @hyperparameters.yaml  
- get the results and format them in expected format
- fill them in @RESULTS_REPORT.md  and a new Notion page
- Upload the markdown file to GCP with GCP Server tool to the appropriate bucket knowing that my username is "ray" 
- Send a system notification about training status and results