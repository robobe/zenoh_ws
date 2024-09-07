import zenoh

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int64, float64

import time

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

def main():

    session = zenoh.open()
    is_ok = False
    # while True:
    is_ok = not is_ok
    req = SetBoolRequest(data=is_ok).serialize()
    replies = session.get("service_demo", handler=zenoh.Queue(), value=req)
    for reply in replies.receiver:
        reply_callback(reply)
        


    session.close()

main()