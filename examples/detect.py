from deepstack_sdk import ServerConfig, Detection

config = ServerConfig("http://localhost:5000")
detection = Detection(config)

response = detection.detectObject("detection.jpg", output="detection_output.jpg", min_confidence=0.8, output_font_color=[0,255,0])

for obj in response:
   print("Name: {}, Confidence: {}, x_min: {}, y_min: {}, x_max: {}, y_max: {}".format(obj.label, obj.confidence, obj.x_min, obj.y_min, obj.x_max, obj.y_max))