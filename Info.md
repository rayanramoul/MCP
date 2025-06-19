# Notion
Write in my Notion MCP Demo the list of @hyperparameters.yaml 

# Whole Workflow
- launch a run on ai server tool with hyperparameters specified in @hyperparameters.yaml  
- get the results and format them in expected format
- fill them in @RESULTS_REPORT.md  and a new Notion page
- Upload the markdown file to GCP with GCP Server tool to gs://runs_ray_mrna
- Send a system notification about training status and results

# Client
Could you list available files in gs://runs