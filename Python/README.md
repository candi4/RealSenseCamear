# Python Wrapper for Realsense
How to use RealSense camera using Python


## How to use
I'm using `python 3.8`.
```shell
pip install pyrealsense2==2.53.1.4623
```

## Codes
### resolution.py
It prints the possible resolutions from the camera using realsense2.

## TroubleShooting
### L515 doesn't work
```shell
Traceback (most recent call last):
  File "example.py", line 6, in <module>
    pipeline.start()
RuntimeError: No device connected
```
L515 doesn't work with recent version of realsense2. So I installed previous version for L515.
```shell
pip install pyrealsense2==2.53.1.4623
```
* References
  * [L515 not detected in realsense-viewer v2.36.0 with OS Ubuntu 18.04](https://github.com/IntelRealSense/librealsense/issues/7224#issuecomment-2336138129)
    ```
    Support for the L515 camera was removed in version 2.54.1 onwards of the RealSense SDK (librealsense) and the RealSense Viewer, because L515 is a retired camera model.
    ```
  * [Intel® RealSense™ Discontinues LiDAR, FA and Tracking Product Lines, Focuses on Stereo Vision (September 2, 2021)](https://www.framos.com/en/news/intel-realsense-discontinues-lidar-fa-and-tracking-product-lines-focuses-on-stereo-vision)

## References
* [SDK 2.0 code samples Wrappers Python](https://dev.intelrealsense.com/docs/python2)
* [How to align confidence matrix from L515 with RGB image?](https://github.com/IntelRealSense/librealsense/issues/8655)
  ```
  The IR stream and confidence stream are perfectly aligned with the depth stream.
  ```