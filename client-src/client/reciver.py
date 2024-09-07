import zenoh
import signal
from dataclasses import dataclass
from pycdr2 import IdlStruct
from pycdr2.types import int64, float64
from zenoh.session import Reliability
import logging



logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

log = logging.getLogger()

@dataclass
class String(IdlStruct):
   data: str

config_dict = {
   "mode": "peer",
   "connect": {
         "endpoints": ["udp/{}:{}".format("172.19.0.3", 7447)]
   },
   # "scouting": {
   #    "multicast": {
   #       "enabled": False
   #    }
   # }

}

def handler(data):
    message = String.deserialize(data.payload)
    log.info(f">> [Subscriber] Received {message.data}")

session = zenoh.open(zenoh.config.Config().from_obj(config_dict))

sub = session.declare_subscriber("pub_string", handler,  reliability=Reliability.RELIABLE())

signal.pause()