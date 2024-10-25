import pyrealsense2 as rs

# RealSense 파이프라인 초기화
pipeline = rs.pipeline()
config = rs.config()

# 연결된 장치로부터 가능한 스트림 프로파일 얻기
pipeline_wrapper = rs.pipeline_wrapper(pipeline)
pipeline_profile = config.resolve(pipeline_wrapper)
device = pipeline_profile.get_device()
sensors = device.query_sensors()
print(sensors)

print("Available resolutions for color and depth streams:")

for sensor in sensors:
    print()
    print(sensor)
    for profile in sensor.get_stream_profiles():
        if profile.is_video_stream_profile():
            video_profile = profile.as_video_stream_profile()
            stream_type = video_profile.stream_type()
            print(stream_type, end="")

            width = video_profile.width()
            height = video_profile.height()
            fps = video_profile.fps()
            print(f"    {width}x{height} @ {fps} FPS")
