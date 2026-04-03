# Camera2 API Enabler – Samsung Galaxy M31 (Exynos)

A **Magisk module** that enables the Camera2 API (HAL3) on **Exynos-based Samsung Galaxy M31** (SM-M315F) rooted devices.

---

## Requirements

| Requirement | Details |
|---|---|
| Device | Samsung Galaxy M31 (SM-M315F) – **Exynos 9611** variant |
| Root | [Magisk](https://github.com/topjohnwu/Magisk) v20.4 or newer |
| Android | Android 10 / One UI 2.x or later |

> **Note:** This module is *not* compatible with the Snapdragon (Qualcomm) variant of the M31.

---

## What it does

| Change | How |
|---|---|
| Sets `persist.camera.HAL3.enabled=1` | `system.prop` + `post-fs-data.sh` |
| Enables Camera2 API full-support flags | `system.prop` |
| Overrides vendor camera configuration | `system/vendor/etc/camera/camera_config.xml` |
| Ensures properties survive across reboots | `service.sh` |

---

## Installation

1. Download the latest release ZIP from the [Releases](../../releases) page.
2. Open **Magisk** → **Modules** → tap the **⊕** (install from storage) button.
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
│       ├── update-binary          # Installer shell script
│       └── updater-script         # Magisk marker
├── system/
│   └── vendor/
│       └── etc/
│           └── camera/
│               └── camera_config.xml  # HAL3 / Camera2 config overlay
├── module.prop                    # Module metadata
├── system.prop                    # System properties (HAL3 flags)
├── post-fs-data.sh                # Early-boot property application
└── service.sh                     # Late-boot property enforcement
```

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Camera app crashes after install | Reboot once more; if it persists, remove the module and reboot |
| Camera2 API still shows LEGACY | Some Samsung firmware versions ignore vendor XML overlays – try a different camera HAL patcher or GCam port |
| Module not appearing in Magisk | Ensure you are using Magisk v20.4+ and that the ZIP is not corrupted |

---

## Disclaimer

This module modifies low-level camera subsystem properties.  Use at your own risk.  The author is not responsible for any damage to your device or data.