# polestar2MQTT
This is a small tool that requests the information from polestar.com and sends the vehicle information to a MQTT Broker

## Disclaimer
This tool uses the [pypolestar](https://github.com/leeyuentuen/pypolestar) library in its 1.1.1 version. I don't like Home Assistant so i had to do my own workaround to get the values in my MQTT Broker

## Installation and run
#### Local
```shell
$ git clone https://github.com/FreakErn/polestar2mqtt.git
$ cd polestar2mqtt
$ pip install -r requirements.txt
$ git clone --branch 1.1.1 https://github.com/leeyuentuen/pypolestar.git
$ ./polestar2mqtt -s -c --polestar-email "email@example.com" --polestar-password "my password" --mqtt-host mqtt.local
```
(*notes* adding the pypolestar to the requirements did not work)

#### Docker
```docker
docker run --restart=unless-stopped \
  --name polestar2mqtt \
  -e POLESTAR2MQTT_POLESTAR_EMAIL=my-polestar-email@example.com \
  -e POLESTAR2MQTT_POLESTAR_PASSWORD=my-secure-password \
  -e POLESTAR2MQTT_MQTT_HOST=mqtt.local \
  -e POLESTAR2MQTT_MQTT_SINGLE=1 \
  -e POLESTAR2MQTT_MQTT_CACHE=1 \
  -e POLESTAR2MQTT_VERBOSE=1 \
  freakern/polestar2mqtt:latest
```

I recommend using the "single" and the "cache" parameter, then each value will be send individually.

## Help

#### Shell Parameter (--help)
```shell
usage: POLESTAR2MQTT [-h] [-d] [-v] --polestar-email POLESTAR_EMAIL [--polestar-password POLESTAR_PASSWORD] [-i REQUEST_INTERVAL] [-s] [--mqtt-single-separator MQTT_SINGLE_SEPARATOR] [-c] [--mqtt-host MQTT_HOST] [--mqtt-port MQTT_PORT] [--mqtt-topic MQTT_TOPIC]
                     [--mqtt-client-id MQTT_CLIENT_ID] [--mqtt-user MQTT_USER] [--mqtt-password MQTT_PASSWORD]

options:
  -h, --help            show this help message and exit

Global:
  -d                    Enable Debug Mode (default: False)
  -v                    (Verbose) Talk to me baby (default: False)

Polestar:
  --polestar-email POLESTAR_EMAIL
                        Polestar email
  --polestar-password POLESTAR_PASSWORD
                        Polestar password (default: gXko4rD6xVtu=xjjkoqbcbxS)
  -i REQUEST_INTERVAL, --request-interval REQUEST_INTERVAL
                        The request interval (default: 60)

MQTT:
  Information needed for the MQTT Connection

  -s, --mqtt-single     Send each value individually to the MQTT Broker (default: False)
  --mqtt-single-separator MQTT_SINGLE_SEPARATOR
                        Separator for the single (-s) parameter. If it is a slash, you'll be able to subscripe just to subtopics (default: /)
  -c, --cache           Cache the send values (works best in single (-s) mode) (default: False)
  --mqtt-host MQTT_HOST
                        MQTT Host to connect to (default: localhost)
  --mqtt-port MQTT_PORT
                        MQTT port to connect to (default: 1883)
  --mqtt-topic MQTT_TOPIC
                        MQTT Topic to publish to (default: POLESTAR2MQTT)
  --mqtt-client-id MQTT_CLIENT_ID
                        MQTT Client-ID (default: POLESTAR2MQTT)
  --mqtt-user MQTT_USER
                        MQTT user to connect to (default: None)
  --mqtt-password MQTT_PASSWORD
                        MQTT password to connect to (default: None)
``````

#### Docker ENV Vars
| ENV Variable Name                     | Description                                                                                               | Default          | Required |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------|----------|
| POLESTAR2MQTT_DEBUG                   | Enable Debug Mode                                                                                         | False            | False    |
| POLESTAR2MQTT_VERBOSE                 | Enable Verbose Mode                                                                                       | False            | False    |
| POLESTAR2MQTT_POLESTAR_EMAIL          | Polestar email                                                                                            |                  | True     |
| POLESTAR2MQTT_POLESTAR_PASSWORD       | Polestar Password                                                                                         |                  | True     |
| POLESTAR2MQTT_REQUEST_INTERVAL        | The request interval                                                                                      |                  | False    |
| POLESTAR2MQTT_MQTT_SINGLE             | Send each value individually to the MQTT Broker                                                           | False            | False    |
| POLESTAR2MQTT_MQTT_SINGLE_SEPARATOR   | Separator for the single (-s) parameter. If it is a slash, you\'ll be able to subscripe just to subtopics | /                | False    |
| POLESTAR2MQTT_MQTT_CACHE              | Cache the send values (works best in single (-s) mode)                                                    | False            | False    |
| POLESTAR2MQTT_MQTT_HOST               | MQTT Host to connect to                                                                                   | localhost        | False    |
| POLESTAR2MQTT_MQTT_PORT               | MQTT port to connect to                                                                                   | 1883             | False    |
| POLESTAR2MQTT_MQTT_TOPIC              | MQTT Topic to publish to                                                                                  | polestar2mqtt    | False    |
| POLESTAR2MQTT_MQTT_CLIENT_ID          | MQTT Client-ID                                                                                            | polestar2mqtt    | False    |
| POLESTAR2MQTT_MQTT_USER               | MQTT user to connect to                                                                                   |                  | False    |
| POLESTAR2MQTT_MQTT_PASS               | MQTT password to connect to                                                                               |                  | False    |

#### Thanks
to @leeyuentuen and @dgomes for the awesome work at the [polestar_api](https://github.com/leeyuentuen/polestar_api)! You guys are awesome!