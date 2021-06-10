# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Device class for EFR32 Pigweed Lighting device."""
from gazoo_device import decorators
from gazoo_device import detect_criteria
from gazoo_device import gdm_logger
from gazoo_device.base_classes import silabs_efr32_device
from gazoo_device.capabilities import pwrpc_common_default
from gazoo_device.capabilities import pwrpc_light_default
from gazoo_device.utility import pwrpc_utils

# TODO(b/185956488): Remove conditional imports of Pigweed
try:
  # pylint: disable=g-import-not-at-top
  # pytype: disable=import-error
  from button_service import button_service_pb2
  from device_service import device_service_pb2
  from lighting_service import lighting_service_pb2
  # pytype: enable=import-error
except ImportError:
  button_service_pb2 = None
  device_service_pb2 = None
  lighting_service_pb2 = None

logger = gdm_logger.get_logger()
_REGEXES = {"BOOT_UP": r"<efr32 > chip-efr32-lighting-example starting",}
_BOOTUP_TIMEOUT = 10  # seconds
_RPC_TIMEOUT = 10  # seconds


class EFR32PigweedLighting(silabs_efr32_device.SilabsEFR32Device):
  """Device class for EFR32PigweedLighting devices.

  This device class is for the Pigweed lighting application running on
  the Silabs EFR32 platform:
  https://github.com/project-chip/connectedhomeip/blob/master/examples/lighting-app/efr32/README.md
  """
  DETECT_MATCH_CRITERIA = {
      detect_criteria.PigweedQuery.product_name: "j-link",
      detect_criteria.PigweedQuery.manufacturer_name: "silicon_labs",
      detect_criteria.PigweedQuery.app_type:
          pwrpc_utils.PigweedAppType.LIGHTING.value,
  }
  DEVICE_TYPE = "efr32pigweedlighting"
  _OWNER_EMAIL = "gdm-authors@google.com"
  _COMMUNICATION_KWARGS = {"protobufs": (button_service_pb2,
                                         lighting_service_pb2,
                                         device_service_pb2),
                           "baudrate": silabs_efr32_device.BAUDRATE}

  def __init__(self,
               manager,
               device_config,
               log_file_name=None,
               log_directory=None):
    super().__init__(
        manager,
        device_config,
        log_file_name=log_file_name,
        log_directory=log_directory)
    self._regexes.update(_REGEXES)

  @decorators.DynamicProperty
  def firmware_version(self):
    """Firmware version of the device."""
    return self.pw_rpc_common.software_version

  @decorators.LogDecorator(logger)
  def reboot(self, no_wait: bool = False):
    """Reboots the device.

    Args:
      no_wait: Return before reboot completes.
    """
    self.pw_rpc_common.reboot(no_wait=no_wait,
                              rpc_timeout_s=_RPC_TIMEOUT,
                              bootup_logline_regex=self.regexes["BOOT_UP"],
                              bootup_timeout=_BOOTUP_TIMEOUT)

  @decorators.LogDecorator(logger)
  def factory_reset(self, no_wait: bool = False):
    """Factory resets the device.

    Args:
      no_wait: Return before factory_reset completes.
    """
    self.pw_rpc_common.factory_reset(
        no_wait=no_wait,
        rpc_timeout_s=_RPC_TIMEOUT,
        bootup_logline_regex=self.regexes["BOOT_UP"],
        bootup_timeout=_BOOTUP_TIMEOUT)

  @decorators.CapabilityDecorator(pwrpc_common_default.PwRPCCommonDefault)
  def pw_rpc_common(self):
    """PwRPCCommonDefault capability to send RPC command."""
    return self.lazy_init(
        pwrpc_common_default.PwRPCCommonDefault,
        device_name=self.name,
        switchboard_call=self.switchboard.call,
        switchboard_call_expect=self.switchboard.call_and_expect)

  @decorators.CapabilityDecorator(pwrpc_light_default.PwRPCLightDefault)
  def pw_rpc_light(self):
    """PwRPCLight capability to send RPC commands."""
    return self.lazy_init(pwrpc_light_default.PwRPCLightDefault,
                          device_name=self.name,
                          switchboard_call=self.switchboard.call)
