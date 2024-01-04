import json
import logging
import time

from collections.abc import MutableMapping
from paho.mqtt import client as mqtt_client


_LOGGER = logging.getLogger(__name__)

class mqtt_helper:
    def __init__(self):
        self.first_reconnect_delay = 1
        self.reconnect_rate = 2
        self.max_reconnect_count = 12
        self.max_reconnect_delay = 60
        self.mqttclient = None
        self.mqttcache = {}

    def connect_mqtt(self, broker, port, client_id, username=None, password=None):

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        def on_disconnect(client, userdata, rc):
            _LOGGER.info("Disconnected with result code: %s", rc)
            reconnect_count, reconnect_delay = 0, self.first_reconnect_delay
            while reconnect_count < self.max_reconnect_count:
                _LOGGER.info("Reconnecting in %d seconds...", reconnect_delay)
                time.sleep(reconnect_delay)

                try:
                    client.reconnect()
                    _LOGGER.info("Reconnected successfully!")
                    return
                except Exception as err:
                    _LOGGER.error("%s. Reconnect failed. Retrying...", err)

                reconnect_delay *= self.reconnect_rate
                reconnect_delay = min(reconnect_delay, self.max_reconnect_delay)
                reconnect_count += 1
            _LOGGER.info("Reconnect failed after %s attempts. Exiting...", reconnect_count)

        # Set Connecting Client ID
        self.mqttclient = mqtt_client.Client(client_id)
        self.mqttclient.username_pw_set(username, password)
        self.mqttclient.on_connect = on_connect
        self.mqttclient.on_disconnect = on_disconnect
        self.mqttclient.connect(broker, port)

    def flatten(self, d: MutableMapping, parent_key: str = '', sep: str = '/') -> MutableMapping:
        items = []
        if isinstance(d, MutableMapping):
            for k, v in d.items():
                new_key = parent_key + sep + k if parent_key else k
                if isinstance(v, (MutableMapping, list)):
                    items.extend(self.flatten(v, new_key, sep=sep).items())
                else:
                    items.append((new_key, v))
        elif isinstance(d, list):
            index = 0
            for v in d:
                new_key = parent_key + sep + str(index) if parent_key else str(index)
                if isinstance(v, (MutableMapping, list)):
                    items.extend(self.flatten(v, new_key, sep=sep).items())
                else:
                    items.append((new_key, v))
        return dict(items)


    def send_data(self, base_topic, data_to_send, mqtt_cache, mqtt_single, mqtt_single_separator):
        
        _LOGGER.debug("Cache %s", self.mqttcache)
        if mqtt_single:
            data_to_send = self.flatten(data_to_send, sep=mqtt_single_separator)
            for k, v in data_to_send.items():
                topic_to_use = base_topic + "/" + str(k)
                if not mqtt_cache or (mqtt_cache and (k not in self.mqttcache or self.mqttcache[k] != str(v))):
                    value_to_use = str(v)
                    _LOGGER.info("Send %s -> %s", topic_to_use, value_to_use)
                    self.mqttclient.publish(topic_to_use, value_to_use)
                    self.mqttcache[k] = value_to_use
                else:
                    _LOGGER.debug("Found %s in cache, skip!", topic_to_use)
        else:
            _LOGGER.debug(data_to_send)
            self.mqttclient.publish(base_topic, json.dumps(data_to_send, default=str))