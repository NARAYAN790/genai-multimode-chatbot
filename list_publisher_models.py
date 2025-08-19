from google.cloud import aiplatform 
 
project_id = "pranay-469217" 
location = "us-central1" 
 
def list_publisher_models(): 
    client = aiplatform.gapic.PublisherModelServiceClient(client_options={"api_endpoint": f"{location}-aiplatform.googleapis.com"}) 
    parent = f"projects/{project_id}/locations/{location}" 
    models = client.list_publisher_models(parent=parent) 
 
    print("\n=== Available Publisher Models (Gemini etc.) ===\n") 
    for model in models: 
        print(model.name, "| Display Name:", model.display_name) 
 
if __name__ == "__main__": 
    list_publisher_models()
