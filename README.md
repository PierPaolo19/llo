# Camera2 API Enabler - Samsung Galaxy M31 (Exynos)

A **Magisk module** that enables the Camera2 API (HAL3) on **Exynos-based Samsung Galaxy M31** (SM-M315F) rooted devices running Android 10, 11, or **12 (One UI 4.x)**.

---

## Requirements

| Requirement | Details |
|---|---|
| Device | Samsung Galaxy M31 (SM-M315F) - **Exynos 9611** variant |
| Root | [Magisk](https://github.com/topjohnwu/Magisk) **v24.0 or newer** |
| Android | Android 10 / One UI 2.x through **Android 12 / One UI 4.x** |

> **Note:** This module is *not* compatible with the Snapdragon (Qualcomm) variant of the M31.

---

## Android 12 (One UI 4.x) compatibility

Android 12 / One UI 4.x introduced several changes that affect Camera2 enablement:

| Change | How the module handles it |
|---|---|
| Camera properties moved to `persist.vendor.camera.*` namespace | Both the legacy and vendor namespaces are set in `system.prop` |
| `debug.camera.hal3` / `debug.camera.zsl` properties required | Added to `system.prop` |
| Camera HAL reads `/odm/etc/camera/` before `/vendor/etc/camera/` | `system/odm/etc/camera/camera_config.xml` overlay added |
| Magisk v24+ required for correct Magic Mount behaviour on A12 | `minMagisk=24000` enforced in `module.prop` |
| Samsung camera provider process name changed (AIDL HAL) | `service.sh` kills all known provider process names |

---

## What it does

| Change | How |
|---|---|
| Sets `persist.camera.HAL3.enabled=1` (A10/A11) | `system.prop` + `post-fs-data.sh` |
| Sets `persist.vendor.camera.HAL3.enabled=1` (A12) | `system.prop` + `post-fs-data.sh` |
| Sets `debug.camera.hal3=1` and `debug.camera.zsl=1` (A12) | `system.prop` |
| Overrides vendor camera configuration | `system/vendor/etc/camera/camera_config.xml` |
| Overrides ODM camera configuration (A12) | `system/odm/etc/camera/camera_config.xml` |
| Ensures properties survive across reboots | `service.sh` |

---

## Installation

1. Download the latest release ZIP from the [Releases](../../releases) page.
2. Open **Magisk** → **Modules** → tap the **+** (install from storage) button.
3. Select the downloaded ZIP and let Magisk flash it.
4. **Reboot** your device.
5. Open any Camera2-compatible app (e.g., [Camera2 API Probe](https://play.google.com/store/apps/details?id=com.airbeat.device.inspector)) to verify that the hardware level is now `FULL` or `LIMITED`.

---

## Uninstallation

Open **Magisk** → **Modules**, locate the module, tap **Remove**, and reboot.

---

## File structure

```
camera2_exynos_m31.zip
├── META-INF/
│   └── com/google/android/
│       ├── update-binary              # Installer shell script (with SDK check)
│       └── updater-script             # Magisk marker
├── system/
│   ├── vendor/
│   │   └── etc/
│   │       └── camera/
│   │           └── camera_config.xml  # HAL3 / Camera2 config overlay (A10/A11/A12)
│   └── odm/
│       └── etc/
│           └── camera/
│               └── camera_config.xml  # HAL3 / Camera2 config overlay (A12 ODM)
├── module.prop                        # Module metadata (minMagisk=24000)
├── system.prop                        # System properties (legacy + vendor namespaces)
├── post-fs-data.sh                    # Early-boot property application + ODM copy
└── service.sh                         # Late-boot property enforcement + HAL restart
```

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Camera app crashes after install | Reboot once more; if it persists, remove the module and reboot |
| Camera2 API still shows LEGACY on Android 12 | Ensure your Magisk version is v24.0+; try flashing a One UI 4.x-compatible GCam port as a secondary test |
| Camera2 API still shows LEGACY on Android 10/11 | Some firmware versions ignore vendor XML overlays; try a dedicated camera HAL patcher |
| Module not appearing in Magisk | Ensure you are using Magisk v24.0+ and that the ZIP is not corrupted |
| "minMagisk" error during install | Update Magisk to v24.0 or newer before flashing this module |

---

## Disclaimer

This module modifies low-level camera subsystem properties. Use at your own risk. The author is not responsible for any damage to your device or data.
