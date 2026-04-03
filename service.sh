#!/system/bin/sh
# service.sh - runs after the system has fully booted.
# Ensures Camera2 / HAL3 properties persist and restarts the camera
# service if it was started before the module's post-fs-data hook ran.

MODDIR="${0%/*}"

# Wait for the system to finish booting before acting
until [ "$(getprop sys.boot_completed)" = "1" ]; do
    sleep 2
done

# Give cameraserver a short grace period, then re-apply properties
sleep 3

SDK=$(getprop ro.build.version.sdk)

# Re-apply properties at runtime using resetprop (Magisk built-in)
apply_props() {
    while IFS='=' read -r key value; do
        case "$key" in
            ''|\#*) continue ;;
        esac
        resetprop "$key" "$value"
    done < "$MODDIR/system.prop"
}

[ -f "$MODDIR/system.prop" ] && apply_props

# Android 12 (SDK 31+): also copy camera config to /odm/etc/camera/ if present.
# This is a late-boot fallback: post-fs-data.sh attempts the same copy early in
# boot, but Magic Mount may not have propagated the overlay at that stage on all
# devices.  Running the copy here (post-boot) guarantees the file is present
# before cameraserver is restarted below.
if [ "$SDK" -ge 31 ] 2>/dev/null; then
    ODM_CAM_DIR="/odm/etc/camera"
    ODM_CFG="$MODDIR/system/odm/etc/camera/camera_config.xml"
    if [ -d "$ODM_CAM_DIR" ] && [ -f "$ODM_CFG" ]; then
        cp -f "$ODM_CFG" "$ODM_CAM_DIR/camera_config.xml" 2>/dev/null || true
    fi
fi

# If cameraserver is running, restart it so it picks up the new properties.
# On Android 12, the process may be named "android.hardware.camera.provider" or
# "cameraserver" depending on the HAL transport (AIDL vs HIDL).
for proc in cameraserver "android.hardware.camera.provider@2.4-service_64" \
            "android.hardware.camera.provider@2.5-service_64" \
            "vendor.samsung.hardware.camera.provider@4.0-service"; do
    CAM_PID=$(pidof "$proc" 2>/dev/null)
    if [ -n "$CAM_PID" ]; then
        kill "$CAM_PID" 2>/dev/null
    fi
done
