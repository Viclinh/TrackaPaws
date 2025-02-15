import json
import sys

class ContextHandler:
    def __init__(self, context):
        if isinstance(context, str):
            try:
                self.context = json.loads(context)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON string provided as context: {e}")
        elif isinstance(context, dict):
            self.context = context
        else:
            raise TypeError("Context must be a JSON string or a dictionary.")

    def run(self):
        response = {}
        try:
            ##############################
            # TODO: Add user code here. #
            #############################
            response["status"] = "success"
            response["data"] = {}
        except Exception as e:
            response["status"] = "error"
            response["message"] = str(e)
        
        print(json.dumps(response, indent=2))

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("Missing required argument: context data.")
        
        context_data = sys.argv[1]
        handler = ContextHandler(context_data)
        handler.run()
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}), file=sys.stderr)
        sys.exit(1)