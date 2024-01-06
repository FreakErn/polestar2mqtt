import argparse
import os


def get_args():
    ap = argparse.ArgumentParser(prog="POLESTAR2MQTT", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    global_group = ap.add_argument_group("Global")
    global_group.add_argument('-d',
                              action='store_true',
                              default=os.environ.get(key='POLESTAR2MQTT_DEBUG') or False,
                              dest='debug',
                              help='Enable Debug Mode'
                              )
    global_group.add_argument('-v',
                              action='store_true',
                              default=os.environ.get(key='POLESTAR2MQTT_VERBOSE') or False,
                              dest='verbose',
                              help='(Verbose) Talk to me baby'
                              )

    polestar_group = ap.add_argument_group("Polestar")
    polestar_group.add_argument('--polestar-email',
                              default=os.environ.get(key='POLESTAR2MQTT_POLESTAR_EMAIL') or argparse.SUPPRESS,
                              dest='polestar_email',
                              help='Polestar email',
                              required=not os.environ.get(key='POLESTAR2MQTT_POLESTAR_EMAIL'),
                              )
    polestar_group.add_argument('--polestar-password',
                              default=os.environ.get(key='POLESTAR2MQTT_POLESTAR_PASSWORD') or argparse.SUPPRESS,
                              dest='polestar_password',
                              help='Polestar password',
                              required=not os.environ.get(key='POLESTAR2MQTT_POLESTAR_PASSWORD')
                              )
    polestar_group.add_argument('-i', '--request-interval',
                              default=os.environ.get(key='POLESTAR2MQTT_REQUEST_INTERVAL') or 10,
                              dest='request_interval',
                              help='The request interval',
                              type=int
                              )

    mqtt_group = ap.add_argument_group("MQTT", "Information needed for the MQTT Connection")
    mqtt_group.add_argument('-s', '--mqtt-single',
                            action='store_true',
                            default=os.environ.get(key='POLESTAR2MQTT_MQTT_SINGLE') or False,
                            dest='mqtt_single',
                            help='Send each value individually to the MQTT Broker'
                            )
    mqtt_group.add_argument('--mqtt-single-separator',
                            default=os.environ.get(key='POLESTAR2MQTT_MQTT_SINGLE_SEPARATOR') or "/",
                            dest='mqtt_single_separator',
                            help='Separator for the single (-s) parameter. If it is a slash, you\'ll be able to subscripe just to subtopics'
                            )
    mqtt_group.add_argument('-c', '--cache',
                            action='store_true',
                            default=os.environ.get(key='POLESTAR2MQTT_MQTT_CACHE') or False,
                            dest='mqtt_cache',
                            help='Cache the send values (works best in single (-s) mode)'
                            )
    mqtt_group.add_argument('--mqtt-host',
                            default=os.environ.get(key='POLESTAR2MQTT_MQTT_HOST') or 'localhost',
                            dest='mqtt_host',
                            help='MQTT Host to connect to'
                            )
    mqtt_group.add_argument('--mqtt-port',
                            default=os.environ.get(key='POLESTAR2MQTT_MQTT_PORT') or '1883',
                            dest='mqtt_port',
                            help='MQTT port to connect to',
                            type=int
                            )
    mqtt_group.add_argument('--mqtt-topic',
                            default=os.environ.get(key='POLESTAR2MQTT_MQTT_TOPIC') or 'polestar2mqtt',
                            dest='mqtt_topic',
                            help='MQTT Topic to publish to',
                            required=False)
    mqtt_group.add_argument('--mqtt-client-id',
                            default=os.environ.get(key='POLESTAR2MQTT_MQTT_CLIENT_ID') or 'polestar2mqtt',
                            dest='mqtt_client_id',
                            help='MQTT Client-ID',
                            required=False
                            )
    mqtt_group.add_argument('--mqtt-user',
                            default=os.environ.get(key='POLESTAR2MQTT_MQTT_USER') or None,
                            dest='mqtt_user',
                            help='MQTT user to connect to',
                            required=False,
                            )
    mqtt_group.add_argument('--mqtt-password',
                            default=os.environ.get(key='POLESTAR2MQTT_MQTT_PASS') or None,
                            dest='mqtt_password',
                            help='MQTT password to connect to',
                            required=False,
                            )

    args = ap.parse_args()
    return args