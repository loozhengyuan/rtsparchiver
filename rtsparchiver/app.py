import subprocess

import boto3


class RSTPServer:
    def __init__(self, host, port, username, password, width="1920", height="1080", fps="30", chunk="3600", prefix="cctv"):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.width = width
        self.height = height
        self.fps = fps
        self.chunk = chunk
        self.prefix = prefix

    def stream(self, channel):
        command = self._get_command(channel)
        subprocess.run(command)

    def _get_command(self, channel):
        uri = f"rtsp://{self.host}:{self.port}/Streaming/Channels/{channel}"
        command = [
            "openRTSP",

            # Output to .mp4
            "-4",

            # Notify first data arrival
            "-n",

            # Show QOS statistics
            "-Q",
        ]

        # Set width for video stream
        if self.width:
            command.extend(["-w", self.width])

        # Set height for video stream
        if self.height:
            command.extend(["-h", self.height])

        # Set fps for video stream
        if self.fps:
            command.extend(["-f", self.fps])

        # Set file prefix
        if self.prefix:
            command.extend(["-F", self.prefix])

        # Set data chunk in seconds
        if self.chunk:
            command.extend(["-P", self.chunk])

        # Add credentials
        command.extend(["-u", self.username, self.password])

        # Add uri
        command.extend([uri])

        return command


class S3Uploader:
    def __init__(self, *args, **kwargs):
        self.client = boto3.resource("s3")
        self.bucket = kwargs["bucket"]

    def upload(self, filename):
        self.client.meta.client.upload_file(filename, self.bucket, filename)
