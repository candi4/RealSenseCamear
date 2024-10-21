# Python Wrapper for Realsense
How to use RealSense camera using Python


## How to use
I'm using `python 3.8`.
```shell
pip install pyrealsense2==2.53.1.4623
```

## TroubleShooting
### L515 doesn't work
```shell
Traceback (most recent call last):
  File "example.py", line 6, in <module>
    pipeline.start()
RuntimeError: No device connected
```
L515 doesn't work with recent version of realsense2. I installed previous version for L515.
```shell
pip install pyrealsense2==2.53.1.4623
```
* References
  * [L515 not detected in realsense-viewer v2.36.0 with OS Ubuntu 18.04](https://github.com/IntelRealSense/librealsense/issues/7224#issuecomment-2336138129): "Support for the L515 camera was removed in version 2.54.1 onwards of the RealSense SDK (librealsense) and the RealSense Viewer, because L515 is a retired camera model."
  * [Cannot access the L515 camera using the python pyrealsense2 library](https://support.intelrealsense.com/hc/en-us/community/posts/18459878622995-Cannot-access-the-L515-camera-using-the-python-pyrealsense2-library-on-a-Rasberry-Pi4)
