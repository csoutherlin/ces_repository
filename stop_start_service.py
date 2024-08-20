import win32serviceutil

def stop_service(service_name):
    try:
        win32serviceutil.StopService(service_name)
        print(f"Service '{service_name}' stopped successfully.")
    except Exception as e:
        print(f"Error stopping service '{service_name}': {e}")

def start_service(service_name):
    try:
        win32serviceutil.StartService(service_name)
        print(f"Service '{service_name}' started successfully.")
    except Exception as e:
        print(f"Error starting service '{service_name}': {e}")

# Example usage
if __name__ == "__main__":
    service_to_manage = "DiagTrack"  # Replace with the actual service name
    action = input("Enter 'start' or 'stop' to manage the service: ")
    
    if action.lower() == "start":
        start_service(service_to_manage)
    elif action.lower() == "stop":
        stop_service(service_to_manage)
    else:
        print("Invalid action. Please enter 'start' or 'stop'.")
