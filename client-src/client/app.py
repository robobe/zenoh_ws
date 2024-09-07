import zenoh

from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int64, float64

import time

@dataclass
class String(IdlStruct):
   data: str

@dataclass
class Special(IdlStruct):
   a: int64
   b: float64
   c: str



config_dict = {
   "mode": "client",
   "connect": {
         "endpoints": ["udp/{}:{}".format("172.19.0.3", 7447)]
   },
   # "scouting": {
   #    "multicast": {
   #       "enabled": False
   #    }
   # }

}

session = zenoh.open(zenoh.config.Config().from_obj(config_dict))

s = String(data="hello world").serialize()
# s = Special(a=6,b=7.5,c="lol").serialize()

while True:
    # session.put('information', s)
    session.put('string_demo', s)
    time.sleep(1)