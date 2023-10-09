import json
import openai

def lambda_handler(event, context):
    try:
        
        def checkHeliconeAuthAndReturnToken(check):
            wrongHeliconeAuth="error"
            if check=="Bearer sk-helicone-kjll5bq-ywceloy-ujfo7ea-5jh7wwq":
                return check
            elif check!="Bearer sk-helicone-kjll5bq-ywceloy-ujfo7ea-5jh7wwq":
                return wrongHeliconeAuth
                
        Helicone_User_Id = event["headers"]["Helicone-User-Id"]
        Helicone_Auth = event["headers"]["Helicone-Auth"]
        request_data = json.loads(event["body"])  
        prompt = request_data["messages"]
        model= request_data["model"]
        
        # Access the client request URL from the 'event' object
        request_url = event["path"]
        # Use 'request_url' as needed in your code
        print("Client Request URL:", request_url, type(request_url))
        parts = request_url.split("/")
        engineName = parts[-3]  # Get the third-to-last part of the URL
        
        
        if "temperature" in request_data:
            print("temperature is given")
            temperature= request_data["temperature"]
        else:
            print("temperature is not given")
            temperature = 0
        
        if "stop" in request_data:
            stop_as = request_data["stop"]
        else:
            stop_as = ""
        
        openai.api_type  = "azure"
        openai.api_version  = "2023-03-15-preview"
        openai.api_key  = "9fb2f00451004c6e82f33d2e7965099a"
        openai.api_base = "https://oai.hconeai.com"


        output = openai.ChatCompletion.create(
        model= model,
        messages= prompt,
        temperature=temperature,
        headers={
        "Helicone-Auth": checkHeliconeAuthAndReturnToken(Helicone_Auth),
        "Helicone-User-Id": Helicone_User_Id,
        "Helicone-OpenAI-Api-Base": "https://bvruseast.openai.azure.com/",
        
            },
        stop= stop_as,
        engine= engineName
        )
        
        response = {
            "statusCode": 200,
            "body": json.dumps(output),
            "headers": {"Content-Type": "application/json"},
        }
        return response
    
    except Exception as e:
        error_message = str(e)
        print("gfgf",error_message)
        return json.dumps({"error": error_message})