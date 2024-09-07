import asyncio
from zenoh import Zenoh
from zenoh.net import Session
import cdr

# Define the ROS2 service message types
@dataclass
class SetBoolRequest(IdlStruct):
   data: bool


@dataclass
class SetBoolResponse(IdlStruct):
   success: bool
   message: str


def reply_callback(reply):
    try:
        message = SetBoolResponse.deserialize(reply.ok.payload)
        print(f">> Received {message}")
    except:
        print(">> Received ERROR")

async def call_ros2_service():
    # Initialize Zenoh session
    z = await Zenoh.open()
    
    # Create a client session
    s = Session(z)
    
    # Define the Zenoh resource path for the service
    service_path = "/ros2/service/my_service"
    
    # Prepare the service request
    request = Trigger_Request()
    
    # Encode the request message
    encoded_request = cdr.encode(request)
    
    # Send the request to the Zenoh resource
    reply = await s.get(service_path, encoded_request)
    
    # Decode the response
    response = cdr.decode(reply.data, Trigger_Response())
    
    print(f"Service response: {response}")
    
    # Close the Zenoh session
    await z.close()

if __name__ == "__main__":
    asyncio.run(call_ros2_service())
