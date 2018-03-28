import random
import time
import sys
import iothub_client
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue

# String containing Hostname, Device Id & Device Key in the format
CONNECTION_STRING = "HostName=no-66-project.azure-devices.net;DeviceId=FirstPythonDevice;SharedAccessKey=F4i7ZcBdENZjup6pEB+/wOK5ppsGzZF6ytJCbmVRtYI="
# choose HTTP, AMQP or MQTT as transport protocol
PROTOCOL = IoTHubTransportProvider.MQTT
MESSAGE_TIMEOUT = 5000
SEND_CALLBACKS = 0
MSG_TXT = "{\"deviceId\": \"FirstPythonDevice\",\"blink frequency\": %s}"

def send_confirmation_callback(message, result, user_context):
    global SEND_CALLBACKS

def iothub_client_init():
    # prepare iothub client
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    # set the time until a message times out
    client.set_option("messageTimeout", MESSAGE_TIMEOUT)
    client.set_option("logtrace", 0)
    client.set_option("product_info", "HappyPath_Simulated-Python")
    return client

def iothub_client_telemetry_sample_run(blink_frequency=0):
    
    try:
        client = iothub_client_init()
        message_counter = 0

        msg_txt_formatted = MSG_TXT % (blink_frequency) #time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # messages can be encoded as string or bytearray
        if (message_counter & 1) == 1:
            message = IoTHubMessage(bytearray(msg_txt_formatted, 'utf8'))
        else:
            message = IoTHubMessage(msg_txt_formatted)
        """# optional: assign ids
        message.message_id = "message_%d" % message_counter
        message.correlation_id = "correlation_%d" % message_counter
        # optional: assign properties
        prop_map = message.properties()
        prop_text = "PropMsg_%d" % message_counter
        prop_map.add("Property", prop_text)"""

        client.send_event_async(message, send_confirmation_callback, message_counter)
        print ( "IoTHubClient.send_event_async accepted message [%d] for transmission to IoT Hub." % message_counter )

        status = client.get_send_status()
        print ( "Send status: %s" % status )
        time.sleep(5)

        status = client.get_send_status()
        print ( "Send status: %s" % status )

        message_counter += 1

    except IoTHubError as iothub_error:
        print ( "Unexpected error %s from IoTHub" % iothub_error )
        return
    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "Simulating a device using the Azure IoT Hub Device SDK for Python" )
    print ( "    Protocol %s" % PROTOCOL )
    print ( "    Connection string=%s" % CONNECTION_STRING )

    iothub_client_telemetry_sample_run()