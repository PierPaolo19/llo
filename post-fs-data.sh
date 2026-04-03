#!/system/bin/sh
# post-fs-data.sh - runs early in the boot sequence (filesystem is mounted,
# but before most services start).  Used to apply Camera2 / HAL3 properties
# before the camera service reads them for the first time.

MODDIR="${0%/*}"

# Detect Android SDK version so we can handle property namespaces correctly.
SDK=$(getprop ro.build.version.sdk)

# Re-apply every property from system.prop so they are definitely set
# before cameraserver starts, even on devices that cache prop values early.
apply_props() {
    while IFS='=' read -r key value; do
        # Skip blank lines and comments
        case "$key" in
            ''|\#*) continue ;;
        esac

        # ro.* properties are read-only by default; on Android 12 (SDK 31+)
        # resetprop can still override them at runtime without -n, but we use
        # -n (no-init notification) everywhere to avoid triggering init actions
        # from the property change event during early boot.
        resetprop -n "$key" "$value"
    done < "$MODDIR/system.prop"
}

[ -f "$MODDIR/system.prop" ] && apply_props

# Android 12 (SDK 31+): the vendor camera HAL reads from /odm/etc/camera/ first.
# If the device exposes an ODM partition, mirror the config there too.
# NOTE: This copy also runs in service.sh as a late-boot fallback for devices
# where Magic Mount has not yet propagated the overlay at this early stage.
if [ "$SDK" -ge 31 ] 2>/dev/null; then
    ODM_CAM_DIR="/odm/etc/camera"
    ODM_CFG="$MODDIR/system/odm/etc/camera/camera_config.xml"
    if [ -d "$ODM_CAM_DIR" ] && [ -f "$ODM_CFG" ]; then
        cp -f "$ODM_CFG" "$ODM_CAM_DIR/camera_config.xml" 2>/dev/null || true
    fi
fi
