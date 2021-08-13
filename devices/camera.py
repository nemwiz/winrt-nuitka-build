import asyncio
import platform

if platform.system() == 'Windows':
    import winrt.windows.devices.enumeration as windows_devices

VIDEO_DEVICES = 4


class Camera:

    def add_camera_information(self, camera_indexes: list) -> list:
        platform_name = platform.system()
        cameras = []

        if platform_name == 'Windows':
            cameras_info_windows = asyncio.run(self.get_camera_information_for_windows())

            for camera_index in camera_indexes:
                camera_name = cameras_info_windows.get_at(camera_index).name.replace('\n', '')
                cameras.append({'camera_index': camera_index, 'camera_name': camera_name, 'is_active': False})

            return cameras

    async def get_camera_information_for_windows(self):
        return await windows_devices.DeviceInformation.find_all_async(VIDEO_DEVICES)


camera = Camera()
